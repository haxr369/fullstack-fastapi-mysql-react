import axios from "axios"
import jwtDecode from "jwt-decode";
import oAuth from "./oAuth"

const checkToken = async () => {
    const limit_access = 30;
    const token = localStorage.getItem('access_token');
    if (token) {
      const decodedIdToken = jwtDecode(token);
      console.log(decodedIdToken);
    }

    const TEST_TOKEN_ENDPOINT = "http://192.168.0.203:8005/api/v1/login/testToken"

    const headers = {
        'accept': 'application/json',
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    };

    

    try {
        const resp = await axios.get(TEST_TOKEN_ENDPOINT,  {
            headers
        });

        if(resp.data['id']===-1){
            console.log("토큰 유효기간 만료");
            console.log("리셋 토큰!!");
            localStorage.removeItem('access_token');
            oAuth();
            return "ok"
        }


        if(resp.data['access'] * 1 > 0){
            console.log(resp.data['access']+"번 요청함");
            console.log("GPU 제한 안함");
            return "ok";
        }

    } catch (error) {
        console.log(error);
        //oAuth();
        return error;
    }
};

export default checkToken;