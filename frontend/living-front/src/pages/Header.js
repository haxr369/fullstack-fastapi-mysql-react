import './css/header.css';
import { Link } from 'react-router-dom';
import React, { useEffect, useState } from "react";
import checkToken from "./auth/checkToken";

const Header = () =>{
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    const [showUserMenu, setShowUserMenu] = useState(false);
    const [userNickName, setUserNickName] = useState("");

    const handleLogin = async () => {
        const token = localStorage.getItem('access_token');
        if (token) {
        try {
            const resp = await checkToken();
            console.log(resp);
            if (resp.User_nickname !== '-1') {
                setIsLoggedIn(true);
                setUserNickName(resp.User_nickname);
            }
            else{
                localStorage.removeItem('access_token');
                setIsLoggedIn(false);
                setUserNickName("");
            }
        } catch (error) {
            console.error(error);
        }
        }
    };


    const handleLogout = () => {
        localStorage.removeItem('access_token');
        setIsLoggedIn(false);
        setUserNickName("");
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