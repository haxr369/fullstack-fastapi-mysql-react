import React, { useState, useEffect } from 'react';
import PlantList from './PlantList';         //plants 데이터 리스트를 이용해서 식물 막대표를 그리는 컴포넌트.
import SearchPlantAPI from '../APIs/SearchPlantAPI';
//import Pagination from './Pagination';    
import { Link } from 'react-router-dom';
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
  //const [currentPage, setCurrentPage] = useState(1); // 현재 페이지 번호
  //const [totalPage, setTotalPage] = useState(1); // 현재 페이지 번호
  
  const [searchQuery, setSearchQuery] = useState([]); // 검색어

  
  async function getPlantList(page, query) {
    //서버로 검색어와 현재 페이지를 전송해서 총 페이지와 현재 페이지의 데이터를 받아온다.
    //console.log("현재 검색어 :"+query+" 현재 페이지 :"+page);
    const ll =['검색',"검색어"+query,"페이지"+page];
    return ll;
  }


  useEffect(() => {
    const runAsync = async () =>{
      //console.log("서치바의 쿼리 : "+searchTemp);
      const result = await SearchPlantAPI('');
      //console.log("검색 결과");
      //console.log(result.data);
      setSearchQuery(result.data);
    }
    runAsync();
  }, []);

  //화면 하단에 페이지 번호를 누르면 현재 페이지 번호를 바꾸는 함수.
  /**
   * function handlePageChange(pageNumber){
    setCurrentPage(pageNumber);
  };
   */
  

  // 검색어를 입력하면 결과를 받아와서 plant data list를 변경하는 함수.
  //query는 검색어
  const handleSearch = (e) => { 
    //alert(searchQuery);
    console.log("plants");
    console.log(e);
    if (Array.isArray(e)){
      setSearchQuery(e);
    }
    else{
      setSearchQuery([]);
    }
  };

  const plantList = searchQuery.map((plant, index) => <li key={index}>
                          <Link to={`/detailplant?species=${plant['Species_name']}`}>
                            <div>{plant['Species_name']}</div>
                            <div>{plant['Plant_id']}</div>
                            <div>{plant['Genus_name']}</div>
                            <div>{plant['Family_name']}</div>
                        </Link>
                                </li>)

  /**
   * <SearchBar onSearch={handleSearch} />
      <PlantList plants={plants} />
      {plants.length > 0 && (
            <Pagination
                itemsPerPage={10}
                totalPages={totalPage}
                currentPage={currentPage}
                onPageChange={handlePageChange}
            />)}
   * 
   */
  
  return (
    <div>
        <SearchBar className='searchbar' onSearchSubmit={handleSearch} />
        <div className="plant-list">
        {plantList}
        </div>
    </div>
  );
};

export default Plants;