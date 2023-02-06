import axios from "axios";
import jwtDecode from "jwt-decode";
import React, { useState } from "react";

const Login = () => {
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [oathR, setOathR] = useState("")

  
        

    const handleSubmit = async() => {
        //const res = await axios.post(, {username, password})

        
        //const res = OAuth();
        //console.log(res)
        
        //const {access_token, token_type} = res.data
        const decodedIdToken = jwtDecode(username)
        console.log("이건 뭐지??   "+username)


        const profile = {id: decodedIdToken.id}
        //console.log("이건 뭐지??   "+profile)
        localStorage.setItem("access_token", username)
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