import React, { useState, useEffect } from 'react';
import axios from "axios";

const Detailinfo = (props) => {
  /**
   * ^^^props^^^^
   * Species
   * onSearchDetail
   * 
   */
  const [data, setData] = useState('');
  const [Species, setSpecies] = useState('');

  

  useEffect(() => {
    setSpecies(props.Species);
    if(data !== ''){
      props.onSearchDetail(data);
    }
   
    },[data]);

  const handleDataUpdate= () => {
    const fetchData = async () => {
      if(Species !== ''){
        try{
            console.log("Species name : "+Species);
            const result = await axios.get(`/api/v1/search/detailinfo/${Species}`)
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

    fetchData();
  };

  return (
      <div>
        <p>Data: {Species}</p>
        <button onClick={handleDataUpdate}>Search Species Detail</button>
        
      </div>
    );

};

export default Detailinfo;
