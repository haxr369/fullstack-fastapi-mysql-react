import React from 'react';
/**
 * 
 * searchTerm 변수는 현재 검색어
 * onSearchSubmit 함수는 검색어를 제출할 때 호출된다.
 * 
 */
const SearchBar = ({ searchTerm, onSearchTerm, onSearchSubmit }) => { 
  
  return (
    <div className="search-div">
      <input
        type="text"
        value={searchTerm}
        onChange={onSearchTerm}
        placeholder="Search for plants"
        className="search-input"
      />
      <button onClick={onSearchSubmit} type="submit" className="search-button">
        Search
      </button>
    </div>
  );
};

export default SearchBar;