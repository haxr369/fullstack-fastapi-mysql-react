import React, { useState, useEffect } from 'react';
import PlantList from './PlantList';         //plants 데이터 리스트를 이용해서 식물 막대표를 그리는 컴포넌트.
import Pagination from './Pagination';      
import SearchBar from './SearchBar';
//import { getPlants } from './api'; // API 호출 함수

const Plants = () => {
  const [plants, setPlants] = useState(['기본 값','dfhfbh','abc','bcd','dfv','dfgs','dsfs','dfhfbh',
                                        'dfhfbh','기본 값','abc','bcd','dfv','dfgs','dsfs','dfhfbh',
                                        'dfhfbh','abc','기본 값','bcd','dfv','dfgs','dsfs','dfhfbh',
                                        'dfhfbh','abc','bcd','기본 값','dfv','dfgs','dsfs','dfhfbh',
                                        'dfhfbh','abc','bcd','기본 값','dfv','기본 값','dfgs','dsfs','dfhdsfds',
                                        'dfhfbh','abc','bcd','기본 값','dfv','dfgs','dsfs','dfhfbh',
                                        'dfhfbh','abc','bcd','기본 값','dfv','기본 값','dfgs','dsfs','dfhdsfds',
                                        'dfhfbh','abc','bcd','기본 값','dfv','dfgs','dsfs','dfhfbh',
                                        'dfhfbh','abc','bcd','기본 값','dfv','기본 값','dfgs','dsfs','dfhdsfds',
                                        'dfhfbh','abc','bcd','기본 값','dfv','dfgs','dsfs','dfhfbh',
                                        'dfhfbh','abc','bcd','기본 값','dfv','기본 값','dfgs','dsfs','dfhdsfds']); // 식물 데이터
  const [currentPage, setCurrentPage] = useState(1); // 현재 페이지 번호
  const [searchQuery, setSearchQuery] = useState(''); // 검색어

  async function getPlantList(query) {
    //console.log("현재 검색어 :"+query+" 현재 페이지 :"+page);
      const ll =['검색',query];
      return ll;
  }


  useEffect(() => {
    console.log("현재 페이지 "+currentPage);
  }, [currentPage,searchQuery]);

  //화면 하단에 페이지 번호를 누르면 현재 페이지 번호를 바꾸는 함수.
  function handlePageChange(pageNumber){
    setCurrentPage(pageNumber);
  };

  // 검색어를 입력하면 결과를 받아와서 plant data list를 변경하는 함수.
  //query는 검색어
  const handleSearch = () => { 
    //alert(searchQuery);
    getPlantList(searchQuery)
        .then((data) =>{
            console.log(data);
        setPlants(data);
    }).catch((err) =>{
        console.log(err);
    })

    setSearchQuery('');
  };

  const handleWord = e => {
    const query = e.target.value
    setSearchQuery(query);
  }

  /**
   * <SearchBar onSearch={handleSearch} />
      <PlantList plants={plants} />
      {plants.length > 0 && (
        <Pagination
            itemsPerPage={10}
            totalPages={plants.length}
            currentPage={currentPage}
            onPageChange={handlePageChange}
        />
      )}
   * 
   */
  
  return (
    <div>
        <SearchBar onSearchTerm={handleWord} onSearchSubmit={handleSearch} />
        <div className="plant-list">
        {plants.map((plant) => (
            <div>{plant}</div>))}
        </div>
        {plants.length > 0 && (
            <Pagination
                itemsPerPage={10}
                totalPlants={plants.length}
                currentPage={currentPage}
                onPageChange={handlePageChange}
            />)}

    </div>
  );
};

export default Plants;