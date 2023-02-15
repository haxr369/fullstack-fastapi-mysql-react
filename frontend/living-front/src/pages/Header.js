import React from "react";
import './css/header.css';
import { Link } from 'react-router-dom';

const Header = () =>{
  
    return (    
        <div className="header">

            <h3>시민참여형 도시 식물 데이터 구축</h3>
        <hr  className="header-bar"/>
        <ul className="nav-menu"> 
            <li className="nav-item"><Link to="/">홈</Link></li>
            <li className="nav-item"><Link to="/login">로그인</Link></li>
            <li className="nav-item"><Link to="/selectimg">식물 식별</Link></li>
            <li className="nav-item"><Link to="/apitest">API 테스트</Link></li>
        </ul>
        <hr className="header-bar2"/>
        </div>
    );
}


export default Header;