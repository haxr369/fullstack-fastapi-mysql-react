//Hook  import 
import axios from 'axios';
import { useState, useEffect } from 'react';
import {useSearchParams} from 'react-router-dom';
import './css/IdentyResult.css';
import ShowImgTable  from './ShowImgTable';
//사전에 정의한 데이터를 보여주는 방법 = url 파라미터
//import jwtDecode from "jwt-decode";
import {oAuth,tokenUse} from "../auth";
import { useNavigate } from "react-router-dom";

const IdentyResult =() =>{
    const [searchParams, setSearchParams] =useSearchParams();
    const fileName = searchParams.get('file_name'); 
    const [user_url, setUerUrl] = useState('');
    const [resultData, setResultData] = useState(null);
    const [tokenCheck,setTokenCheck] = useState(null);
    const navigate = useNavigate();

    // 식물 식별을 요청하고 사진들을 얻는다.
    // 유저 입력 사진, 샘플 이미지 3x3  총 10개 이미지들.
    const fetchData = async () => {
        if(fileName=="undefined"){
            console.log("Identy Result filename : "+fileName);
            navigate("/selectimg");
        }
        else if(fileName){
            console.log("filename : "+fileName);
            const result = await axios.get(`/api/v1/results/identy/${fileName}`)
            .then((json) => {
              setResultData(json.data);
              //console.log(json.data);
            });
          await axios.get(`/api/v1/items/userImg/${fileName}`, {
              responseType: 'blob'
          }).then(response => {
              const url = URL.createObjectURL(new Blob([response.data]));
              setUerUrl(url);
          });
        }
        else{
            console.log("Identy Result filename : "+fileName);
            navigate("/selectimg");
        }
        
      };
    
    const checkAccess =  async () => {
        const token = localStorage.getItem('access_token');
        if(token){
            const tokenUse_result = await tokenUse(token);
            setTokenCheck(tokenUse_result)
            console.log("토큰 확인 결과 "+tokenUse_result);
            
            return tokenUse_result;
        }
        else{
            console.log("토큰부터 받으세요.")
            navigate("/selectimg");
        }
    };

    const resetToken = async () =>{
        console.log("리셋 토큰!!");
        localStorage.removeItem('access_token');
        setTokenCheck(null);
        await oAuth();
        navigate("/selectimg");
    };

    useEffect(() => {

        if(tokenCheck){ //tokenCheck가 null이 아닌 경우. checkAccess가 수행된 것.
            console.log(tokenCheck);
            if(tokenCheck === "tokenExpiration"){ //토큰 유효기간 만료
                resetToken();}
            else if(tokenCheck === "ok"){ //유효한 토큰이 들어온 경우.
                fetchData();}  
        }    
        else{
            checkAccess();
        }
      },[tokenCheck]);
    
    if(tokenCheck === "gpuWating"){
        setTimeout(() => resetToken(), 60000*2);
        return (
            <div>
                너무 많이 GPU 서비스를 사용했습니다.<p/>
                2분간 기다린 후에 새로고침 해주세요.
            </div>
        );
    }
    else if (!resultData) {
        return <div>Loading...</div>;
    }
    

    const getImage = () => {
        axios.get(`/api/v1/items/userImg/${fileName}`, {
            responseType: 'blob'
        }).then(response => {
            console.log("이미지 얻어!!")
            const url = URL.createObjectURL(new Blob([response.data]));
            setUerUrl(url);
        });
    };
    
    /**
     * 틀을 만들자.!
     * 이미지 크기 화면에 맞도록.
     * 컴포넌트 반복을 이용해서 top1 ~ 3까지 요소를 화면에 출력
     * (추가) 이미지를 누르면 이미지 확대 기능을 가질 수 있을까..?
     * (추가) 식물 비교 페이지도 만들어 보자..!
     *  <p>{fileName}</p> 
     */

    const tops = ["top1","top2","top3"];
    const topsList = tops.map(top => (
        <ShowImgTable result = {resultData['results'][top]}
        />
    ));
    
        return (
        
            <div>
                <div className='userContain'>
                    <h2 className = 'userImgTitle'>식별 식물</h2>
                    <div className='userImgContain'>
                        <img className='userImg'  alt="user img" src={user_url} />
                    </div>
                </div>
                
                <div className='resultTable'>
                    <h4 className = 'resultImgTitle'>가장 유사한 식물들</h4> 
                </div>
    
                <div className='imgTable'>
                    {topsList}
                </div>
            
            </div>
        );

    

};

export default IdentyResult;