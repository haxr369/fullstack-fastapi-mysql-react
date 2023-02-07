import axios from "axios";
import jwtDecode from "jwt-decode";
import React, { useState, useEffect } from "react";
import oAuth from "./auth/oAuth"

const Login = () => {


    useEffect( () => {
        console.log("랜더링!!")
        const res = localStorage.getItem('access_token')
        if(res){
            console.log("현재 내가 가지고 있는 "+res)
        }
        else{
            const res = oAuth(); // token localStorage에 저장.
        }
    },[]);

    if(localStorage.getItem('access_token')){
        console.log(localStorage.getItem('access_token'))
    }

    
    const handleSubmit = async() => {
        
        /***
         * 
        console.log(res)

        const {access_token, id_token, refresh_token} = res.data

        const decodedIdToken = jwtDecode(id_token)
        const profile = {email: decodedIdToken.email}

        localStorage.setItem("access_token", access_token)
        localStorage.setItem("refresh_token", refresh_token)
        localStorage.setItem("profile", JSON.stringify(profile))
         * 
         * <div>
                username :
                <input 
                type={"text"}
                value={username}
                onChange={(e) => setUsername(e.target.value)}/>
            </div>
            <div>
                password : 
                <input
                type={"text"}
                value={password}
                onChange={(e) => setPassword(e.target.value)}/>
            </div>
         * 
         */
        
        

    }

    return (
        <div><h2>토큰 테스트!!!</h2>
            
            <button onClick={handleSubmit}>Submit</button>
        </div>
    )
}

export default Login;