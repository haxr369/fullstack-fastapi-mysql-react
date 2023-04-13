import axios from "axios";
import jwtDecode from "jwt-decode";
import React, { useState, useEffect } from "react";
import oAuth from "./auth/oAuth"
import { gpuUse, checkToken } from "./auth";

const Login = () => {


    useEffect( () => {
        console.log("랜더링!!")
        
    },[]);

    if(localStorage.getItem('access_token')){
        console.log(localStorage.getItem('access_token'))
    }

    const handleLogin = async() => {
        const res = localStorage.getItem('access_token')
        if(res){
            console.log("현재 내가 가지고 있는 "+res);
            const rep = await checkToken();
            if(rep.data.User_nickname === "-1"){
                oAuth();
            }
        }
        else{
            const res = oAuth(); // token localStorage에 저장.
        }
    }
    
    const handleSubmit = async() => {
        gpuUse();
    }

    const handleTest = async() => {
        const rep = await checkToken();
        console.log(rep);
    }

    return (
        <div><h2>토큰 테스트!!!</h2>
            <button onClick={handleLogin}>Login</button><p/>
            <button onClick={handleSubmit}>Use GPU</button><p/>
            <button onClick={handleTest}>Test Token</button>
        </div>
    )
}

export default Login;