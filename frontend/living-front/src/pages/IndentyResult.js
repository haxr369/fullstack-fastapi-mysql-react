//Hook  import 
import axios from 'axios';
import { useState, useEffect } from 'react';
import {useSearchParams} from 'react-router-dom';
import './css/IdentyResult.css';
import ShowImgTable  from './ShowImgTable';
//사전에 정의한 데이터를 보여주는 방법 = url 파라미터


const IdentyResult =() =>{
    const [searchParams, setSearchParams] =useSearchParams();
    const fileName = searchParams.get('file_name'); 
    const [user_url, setUerUrl] = useState('');
    const [resultData, setResultData] = useState(null);


    // 식물 식별을 요청하고 사진들을 얻는다.
    // 유저 입력 사진, 샘플 이미지 3x3  총 10개 이미지들.
    useEffect(() => {
        // 아래 fetch가 서버에 식별을 요청하는 것.
        fetch('http://192.168.0.203:8005/api/v1/results/identy/${fileName}')
          .then((response) => response.json())  //json 형태로 식별 결과가 오면,
          .then((json) => setResultData(json));
        
          // 사용자 입력 사진을 서버에서 요청한다.
        axios.get(`http://192.168.0.203:8005/api/v1/items/oneImg/${fileName}`, {
            responseType: 'blob'
        }).then(response => {
            const url = URL.createObjectURL(new Blob([response.data]));
            setUerUrl(url);
        });

      }, []);

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