import axios from "axios";
import jwtDecode from "jwt-decode";
import React, { useState, useEffect } from "react";
import oAuth from "./auth/oAuth"
import { gpuUse, checkToken } from "./auth";
import Join from "./auth/Join";
const Login = () => {

    const [nickName, setNickName] = useState('');
    const [passWord, setPassWord] = useState('');

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

    const handleNickname = (event) => {
        setNickName(event.target.value);
        
      };
    const handlePassword = (event) => {
        setPassWord(event.target.value);
      };
    const handleJoin = async() => {

        try{
            console.log(nickName);
            console.log(passWord);
            if (nickName==='' || passWord===''){
                alert('닉네임과 비밀번호를 전부 작성해주세요.');
            }
            else{
                const res = await Join({ User_nickname: nickName, User_PASSWORD: passWord});
                if(res===-1){
                    alert('정상적인 회원가입이 불가합니다.');
                }
            }
            setNickName('');
            setPassWord('');
        }catch(ex){
            console.log(ex);
        }
    }

    return (
        <div><h2>토큰 테스트!!!</h2>
            <button onClick={handleLogin}>Login</button><p/>
            <button onClick={handleSubmit}>Use GPU</button><p/>
            <button onClick={handleTest}>Test Token</button>
            <div>
                <p/>
                <div>---------------회원가입 테스트------------</div>
                
            </div>

            <input type="text" placeholder="닉네임" value={nickName} onChange={handleNickname} />
            <input type="text" placeholder="비밀번호" value={passWord} onChange={handlePassword} />
            <button onClick={handleJoin}>회원가입!!</button>
        </div>
    )
}

export default Login;