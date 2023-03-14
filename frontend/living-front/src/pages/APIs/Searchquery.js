import React, { useState, useEffect } from 'react';
import axios from "axios";

const Searchquery = (props) => {
  /**
   * ^^^props^^^^
   * Query
   * onSearchQuery
   * 
   */
  const [data, setData] = useState('');
  const [query, setQuery] = useState('');

  

  useEffect(() => {
    setQuery(props.Query);
    if(data !== ''){
      props.onSearchQuery(data);
    }
   
    },[data]);

  const handleDataUpdate= () => {
    const fetchData = async () => {
      
      try{
          console.log("query : "+query);
          const result = await axios.get(`/api/v1/search/searchquery/${query}`)
          .then((json) => {
              //console.log(json.data);
              setData(json.data);
          });
      }
      catch (ex){
          alert("답변 불가. "+query);
          //navigate("/selectimg");
      } 
      

    };

    const reu =  fetchData();
    console.log('자식 컴포넌트');
    console.log(data);
    
  };

  return (
      <div>
        <p>Data: {query}</p>
        <button onClick={handleDataUpdate}>Search Data</button>
        
      </div>
    );

};

export default Searchquery;
