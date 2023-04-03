import axios from "axios"
import jwtDecode from "jwt-decode";
import oAuth from "./oAuth"

const checkToken = async () => {
    const limit_access = 30;
    const token = localStorage.getItem('access_token');
    if (token) {
      const decodedIdToken = jwtDecode(token);
      const timestamp = parseInt(new Date().getTime()/1000);
      console.log(decodedIdToken);
      console.log(timestamp);
    }

    const TEST_TOKEN_ENDPOINT = "/api/v1/login/testToken"

    const headers = {
        'accept': 'application/json',
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    };


    const testToken = async () => {
        await axios.get(TEST_TOKEN_ENDPOINT,  {
            headers
        }).then( res => {
            console.log(res);
            if(res.data.User_id === -1){
                console.log("토큰 유효기간 만료");
                console.log("리셋 토큰!!");
                localStorage.removeItem('access_token');
                oAuth();
                return "ok"
            }

            return res;
        }).catch( err => {
            if(err.request.status === 403){
                console.log("토큰 유효기간 만료");
                console.log("리셋 토큰!!");
                localStorage.removeItem('access_token');
                oAuth();
            }
        })
    }



    try {
        console.log("토큰 테스트 시작!!")
        const resp = testToken();
        //const decodedJson = jwtDecode(resp);
        
        //console.log(resp.status);

        
        

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