import {useState} from 'react';
import axios from 'axios';
import SelectImg from './pages/SelectImg';
import Header from './pages/Header';
import Apitest from './pages/Apitest';
import {Route, Routes } from 'react-router-dom';
import Home from './pages/Home';


const App = () => {

    return (
        <>
        <Header/>
        <Routes>
            <Route path="/" element={<Home/>}/>
            <Route path="/apitest" element={<Apitest/>}/>
            <Route path="/selectimg" element={<SelectImg/>}/>

        </Routes>
        </>
    );
  


};
export default App;