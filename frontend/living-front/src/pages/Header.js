import './css/header.css';
import { Link } from 'react-router-dom';
import React, { useEffect, useState } from "react";
import checkToken from "./auth/checkToken";
import { oAuth } from './auth';

const Header = () =>{
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [showUserMenu, setShowUserMenu] = useState(false);
    const [userNickName, setUserNickName] = useState("");

    const handleLogin = async () => {
        
        try {
            const resp = await checkToken(); 
            if (resp !== -1 && resp.User_nickname !== '-1') { // 로그인한 상태라면 유저 닉네임 보여주기
                setIsLoggedIn(true);
                setUserNickName(resp.User_nickname);
            }
            else{ // 로그인 안한 상태라면 환영인사 안함.
                console.log("로그아웃 상태.")
                localStorage.removeItem('access_token'); 
                setIsLoggedIn(false);
                setUserNickName("");

                //아래 두줄은 나중에 지워야함.
                oAuth(); //로그인함.
                window.location.replace('/');
            }
        } catch (error) {
            console.error(error);
        }
        

    };


    const handleLogout = () => {
        localStorage.removeItem('access_token');
        setIsLoggedIn(false);
        setUserNickName("");
    }

    
    const continueLogin = async() => {
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

    useEffect( () => {

        handleLogin();
    },[]);

    return (    
        <div className="header">

            <h3>시민참여형 도시 식물 데이터 구축</h3>

            <hr  className="header-bar"/>
            {isLoggedIn ? (
                <div className="user-info">
                <p>안녕하세요, {userNickName}님!</p>
                <button className="user-button" data-nickname={userNickName} onClick={() => setShowUserMenu(!showUserMenu)}>
                    {userNickName}
                </button>
                {showUserMenu && (
                    <div className="user-menu">
                    <button onClick={handleLogout}>로그아웃</button>
                    </div>
                )}
                </div>
                ) : (
                    <p/>
                )}
            <ul className="nav-menu"> 
                <li className="nav-item"><Link to="/">홈</Link></li>
                <li className="nav-item"><Link to="/selectimg">식물 식별</Link></li>
                <li className="nav-item"><Link to="/plantList">식물 검색</Link></li>
            </ul>
            <hr className="header-bar2"/>
        </div>
    );
}


export default Header;