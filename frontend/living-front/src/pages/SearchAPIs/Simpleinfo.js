import React, { useState, useEffect } from 'react';
import axios from "axios";

const Simpleinfo = (props) => {
  /**
   * ^^^props^^^^
   * Species
   * onSearchSimple
   * 
   */
  const [data, setData] = useState('');
  const [Species, setSpecies] = useState('');

  

  useEffect(() => {
    setSpecies(props.Species);
    if(data !== ''){
      props.onSearchSimple(data);
    }
   
    },[data]);

  const handleDataUpdate= () => {
    const fetchData = async () => {
      if(Species !== ''){
        try{
            console.log("Species name : "+Species);
            const result = await axios.get(`/api/v1/search/simpleinfo/${Species}`)
            .then((json) => {
                //console.log(json.data);
                setData(json.data);
            });
        }
        catch (ex){
            alert("없는 식물 ."+Species);
            //navigate("/selectimg");
        } 
      }
      else{
        console.log('종을 입력 받지 못했다.');
      }
    };
    const reu =  fetchData();
    console.log('자식 컴포넌트');
    console.log(data);
  };

  return (
      <div>
        <p>Data: {Species}</p>
        <button onClick={handleDataUpdate}>Search Data</button>
        
      </div>
    );

};

export default Simpleinfo;
