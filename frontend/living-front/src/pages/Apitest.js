import {useState, useEffect} from 'react';
import axios from 'axios';
import checkToken from "./auth/checkToken";
import Simpleinfo from './APIs/Simpleinfo';
import Detailinfo from './APIs/Detailinfo';
import Searchquery from './APIs/Searchquery';

const Apitest = () => {
  
  const [data, setData] = useState('');
  const [searchData, setSearchData] = useState('');
  const [simpleinfo, setSimpleinfo] = useState('');
  const [detailinfo, setDetailinfo] = useState('');
  const [queryResult, setQueryResult] = useState([]);

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

  const onSearchClick = async () =>{
    try{
      console.log("search...");

      const response = await axios.get('/api/v1/search/느릅나무')
      .then((result) =>{
        console.log(result);
      }) 
      setSearchData(response);
      
    } catch(e){
      console.log(e);
    }
  }

  const handleDataSimple = (simpleinfo) => {
    console.log('apitest');
    setSimpleinfo(simpleinfo);
    console.log(simpleinfo);
  }

  const handleDataDetail = (simpleinfo) => {
    console.log('apitest');
    setDetailinfo(simpleinfo);
    console.log(simpleinfo);
  }

const handleDataQuery = (queryResult) => {
    console.log('apitest');
    setQueryResult(queryResult);
    console.log(queryResult);
  }



  const plantList = queryResult.map((plant, index) => <li key={index}>{plant}</li>)


  /**
   * <Simpleinfo Species = '가막살나무' onSearchSimple={handleDataSimple} />
      <Detailinfo Species = '가막살나무' onSearchDetail={handleDataDetail} />
      <Detailinfo Species = '가죽나무' onSearchDetail={handleDataDetail} />
      
      <div>{simpleinfo['Species_name']}</div>
      <div>{simpleinfo['Plant_id']}</div>
      <div>{simpleinfo['Genus_name']}</div>
      <div>{simpleinfo['Family_name']}</div>
      <div>---------절취선------------</div>
      <div>{detailinfo['Species_name']}</div>
      <div>{detailinfo['Plant_id']}</div>
      <div>{detailinfo['Bear_fail']}</div>
      <div>{detailinfo['Describe']}</div>
   * 
   */
  return (
    <div>
      <div>
        <button onClick={onClick}>
        불러오기
        </button>
      </div>
      {data}
      <div>
        <div>
          <button onClick={onSearchClick}>
          검색
          </button>
        </div>
        {searchData}
        
      </div>
      <Searchquery Query= '' onSearchQuery = {handleDataQuery}/>
      
      <ul>{plantList}</ul>

      

    </div>
  );

};
export default Apitest;