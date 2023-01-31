import axios from "axios";
import jwtDecode from "jwt-decode";
import React, { useState } from "react";
import oAuth from "./auth/oAuth"

const Login = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")



    const handleSubmit = async() => {
        //const res = await axios.post(, {username, password})

        const res = oAuth({username,password});
        console.log(res)

        const {access_token, id_token, refresh_token} = res.data

        const decodedIdToken = jwtDecode(id_token)
        const profile = {email: decodedIdToken.email}

        localStorage.setItem("access_token", access_token)
        localStorage.setItem("refresh_token", refresh_token)
        localStorage.setItem("profile", JSON.stringify(profile))

    }

    return (
        <div><h2>토큰 테스트!!!</h2>
            <div>
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
            <button onClick={handleSubmit}>Submit</button>
        </div>
    )
}

export default Login;