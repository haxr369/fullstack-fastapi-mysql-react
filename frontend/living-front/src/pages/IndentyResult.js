//Hook  import 
import axios from 'axios';
import { useState, useEffect } from 'react';
import {useSearchParams, Redirect} from 'react-router-dom';
import './css/IdentyResult.css';
import ShowImgTable  from './ShowImgTable';
//사전에 정의한 데이터를 보여주는 방법 = url 파라미터
import jwtDecode from "jwt-decode";
import oAuth from "./auth/oAuth"
import tokenUse from "./auth/Tokenuse"

const IdentyResult =() =>{
    const [searchParams, setSearchParams] =useSearchParams();
    const fileName = searchParams.get('file_name'); 
    const [user_url, setUerUrl] = useState('');
    const [resultData, setResultData] = useState(null);
    const [token,setToken] = useState(null);

    // 식물 식별을 요청하고 사진들을 얻는다.
    // 유저 입력 사진, 샘플 이미지 3x3  총 10개 이미지들.
    const fetchData = async () => {
        const result = await axios.get(`http://192.168.0.203:8005/api/v1/results/identy/${fileName}`)
          .then((json) => {
            setResultData(json.data);
            //console.log(json.data);
          });
        await axios.get(`http://192.168.0.203:8005/api/v1/items/oneImg/${fileName}`, {
            responseType: 'blob'
        }).then(response => {
            const url = URL.createObjectURL(new Blob([response.data]));
            setUerUrl(url);
        });
      };
    
    const checkAccess = async () => {
        const token = localStorage.getItem('access_token');
        if(token){
            const decodedIdToken = jwtDecode(token);
            //console.log("디코드 토큰"+decodedIdToken);
            const tokenUse_result = await tokenUse(token);
            setToken(tokenUse_result)
            console.log("토큰 확인 결과 "+tokenUse_result);
            /**if(tokenUse_result === null){
                console.log(tokenUse_result);
                return (
                    <div>
                        너무 많이 GPU 서비스를 사용했습니다.<p/>
                        잠시만 기다려주세요.
                    </div>
                );
            }**/
        }
        else{
            return (
                <>
                <Redirect to={{
                                    pathname: '/selectimg'
                                  }}
                    />
                </>
            );
        }
    };

    useEffect(() => {
        fetchData();
        checkAccess();
        
        
      },[]);
    

    if (!resultData) {
        return <div>Loading...</div>;
    }
    

    const getImage = () => {
        axios.get(`http://192.168.0.203:8005/api/v1/items/oneImg/${fileName}`, {
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
    
    if(token){
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
    }
    else{
        return (
            <div>
                너무 많이 GPU 서비스를 사용했습니다.<p/>
                잠시만 기다린 후에 새로고침 해주세요.
            </div>
        );
    }
    

};

export default IdentyResult;