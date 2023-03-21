import React, { useState, useEffect } from 'react';
import SearchPlantAPI from '../APIs/SearchPlantAPI';  
/**
 * 
 * searchTerm 변수는 현재 검색어
 * onSearchSubmit 함수는 검색어를 제출할 때 호출된다.
 * 
 */
const SearchBar = ({ onSearchSubmit }) => { 
  const [searchTemp, setSearchTemp] = useState(''); // 임시 검색어

  const handleQuery = () => {

    const runAsync = async () =>{
      //console.log("서치바의 쿼리 : "+searchTemp);
      const result = await SearchPlantAPI(searchTemp);
      //console.log("검색 결과");
      //console.log(result.data);
      onSearchSubmit(result.data);
    }

    runAsync();
    
  }

  const handleWord = e => { //검색어를 입력하는 과정
    const query = e.target.value
    setSearchTemp(query);
  }

  /**
   *  
   * 
   * 
   */
  return (
    <div className="search-div">
      <input
        type="text"
        value={searchTemp}
        onChange={handleWord}
        placeholder="Search for plants"
        className="search-input"
      />
      <button onClick={handleQuery} type="submit" className="search-button">
        Search
      </button>
    </div>
  );
};

export default SearchBar;