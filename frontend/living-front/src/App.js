import SelectImg from './pages/SelectImg';
import Header from './pages/Header';
import Apitest from './pages/Apitest';
import {Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import IdentyResult from './pages/IndentyResult';
import SearchPlant from './pages/SearchPlant';
import { useEffect, useState } from "react";

const App = () => {
    const [token, setData] = useState('');
  
  //비동기적으로 get요청을 하고 데이터를 받아온다.
  const onClick = async ()=> {
    try{
      
      setData("가보자구~~~~");
      console.log(token);
    } catch(e){
      console.log(e);
    }
    
  };
    
    //<Route path ="/login" element={<Login/>} />
    /**const handleTokenChange = (newToken) => {
        setToken(newToken);
    }
    **/

    return (
        <>
        <button onClick={onClick}> 버튼!!!</button>
        <Header/>
        <Routes>
            
            <Route path="/" element={<Home/>}/>
            <Route path="/apitest" element={<Apitest token={token}/>}/>
            <Route path="/selectimg" element={<SelectImg />}/>
            <Route path ="/identyResults" element={<IdentyResult/>} />

            <Route path ="/searchplant" element={<SearchPlant/>} />

        </Routes>
        </>
    );
  


};
export default App;