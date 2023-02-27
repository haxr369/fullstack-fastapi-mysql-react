import SelectImg from './pages/identify/SelectImg';
import Header from './pages/Header';
import Apitest from './pages/Apitest';
import {Route, Routes } from 'react-router-dom';
import Home from './pages/Home';
import IdentyResult from './pages/identify/IndentyResult';
import Login from './pages/Login';
import SearchPlant from './pages/SearchPlant';

const App = () => {
    return (
        <>
        <Header/>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/apitest" element={<Apitest/>}/>
            <Route path="/selectimg" element={<SelectImg/>}/>
            <Route path ="/identyResults" element={<IdentyResult/>} />
            <Route path ="/login" element={<Login/>} />
            <Route path ="/searchplant" element={<SearchPlant/>} />

        </Routes>
        </>
    );
  


};
export default App;