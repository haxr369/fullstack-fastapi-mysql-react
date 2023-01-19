//Hook  import 
import axios from 'axios';
import { useState, useEffect } from 'react';
import {useSearchParams} from 'react-router-dom';
//사전에 정의한 데이터를 보여주는 방법 = url 파라미터


const IdentyResult =() =>{
    const [searchParams, setSearchParams] =useSearchParams();
    const fileName = searchParams.get('file_name');
    const [url, setUrl] = useState('');
    const [resultData, setResultData] = useState(null);

    useEffect(() => {
        fetch('http://192.168.0.203:8005/api/v1/results/identy/${fileName}')
          .then((response) => response.json())
          .then((json) => setResultData(json));
        
      }, []);

    if (!resultData) {
        return <div>Loading...</div>;
    }


    const onToggleDetail =() => {
        setSearchParams({"file_name": "바람과 함께 사라지다."});
        console.log("파라미터 변경!!!!")
    };
    
    const getImage = () => {
        axios.get(`http://192.168.0.203:8005/api/v1/items/oneImg/${fileName}`, {
            responseType: 'blob'
        }).then(response => {
            console.log("이미지 얻어!!")
            const url = URL.createObjectURL(new Blob([response.data]));
            setUrl(url);
        });
    };
    


    return (
        <div>
            <img
            alt="sample"
            src={url}
            style={{ margin: "auto" }}
            />
            <p>{fileName}</p> 
            <p>파일명은 위에 있습니다.</p>
            <button onClick={getImage}>파라미터 바꾸자</button>
            <div>
                <h3>아래가 식물 식별 결과입니다.</h3>
                <div>
                    <p>{resultData['user_url']}</p> <br/>
                    <p>{resultData['results']['top1']['percent']}</p>
                    <p>{resultData['images']['top1']['plantImgs'][0]}</p>
                </div>

            </div>
        </div>
    );

};

export default IdentyResult;