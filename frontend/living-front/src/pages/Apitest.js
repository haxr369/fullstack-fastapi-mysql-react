import {useState, useEffect} from 'react';
import axios from 'axios';
import checkToken from "./auth/checkToken";

const Apitest = () => {
  
  const [data, setData] = useState('');

  useEffect(()=>{
    checkToken();
    
    
  },[]);


  //비동기적으로 get요청을 하고 데이터를 받아온다.
  const onClick = async ()=> {
    try{
      console.log("test...");
      //비동기적으로 get한 데이터를 response에 입력
      const response = await axios.get('/api/v1/items/apitest')
      .then((result) =>{
        console.log(result);
      }) 
      setData(response);
      
    } catch(e){
      console.log(e);
    }
    
  };//{data && <textarea rows={7} value={JSON.stringify(data,null,2)} readOnly={true}/>}

  return (
    <div>
      <div>
        <button onClick={onClick}>
        불러오기
        </button>
      </div>
      {data}
    </div>
  );

};
export default Apitest;