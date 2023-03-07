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

    const TEST_TOKEN_ENDPOINT = "/api/v1/login/testToken"

    const headers = {
        'accept': 'application/json',
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    };

    

    try {
        console.log("토큰 테스트 시작!!")
        const resp = await axios.get(TEST_TOKEN_ENDPOINT,  {
            headers
        })
        //const decodedJson = jwtDecode(resp);
        console.log(resp);
        if(resp.data['User_id']===-1){
            console.log("토큰 유효기간 만료");
            console.log("리셋 토큰!!");
            localStorage.removeItem('access_token');
            oAuth();
            return "ok"
        }

        if(resp.data['Access_count']  < limit_access){
            console.log(resp.data['Access_count']+"번 요청함");
            console.log("GPU 제한 안함");
            return "ok";
        }
        else{
            console.log(resp.data['Access_count']+"번 요청함");
            console.log("GPU 서비스 중지");
            return "gpuWating";
        }

    } catch (error) {
        console.error(error);
        return error;
    };
}

export default checkToken;