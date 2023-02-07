import { Link } from "react-router-dom";
import React, { useEffect } from "react";
import oAuth from "./auth/oAuth"

const Home =() =>{

    useEffect( () => {
        console.log("홈페이지")
        const res = localStorage.getItem('access_token')
        if(res){
            console.log("현재 내가 가지고 있는 "+res)
        }
        else{
            oAuth(); // token localStorage에 저장.
        }
    },[]);

    if(localStorage.getItem('access_token')){
        console.log(localStorage.getItem('access_token'))
        
    }


    return (
        <div>
            <h2>
                첫 시작 페이지
            </h2>
            <p>가장 먼저 보여지는 페이지입니다.</p>
            <Link to="/apitest"> API 서버와 연결 테스트</Link><br/>
            <Link to="/selectimg"> 이미지 전송 테스트</Link><br/>
            <Link to="/login"> 로그인</Link><br/>
            <Link to="/searchplant"> 느티나무</Link><br/>
        </div>
    );
};

export default Home;