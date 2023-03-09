import axios from "axios"
import jwtDecode from "jwt-decode";

const gpuUse = async () => {
    const limit_access = 30;
    const token = localStorage.getItem('access_token');
    if (token) {
      const decodedIdToken = jwtDecode(token);
      console.log(decodedIdToken);
    }

    const USE_TOKEN_ENDPOINT = "/api/v1/login/usetoken"

    const headers = {
        accept: 'application/json',
        Authorization: `Bearer ${token}`,
        'Content-Type': 'application/json'
    };

    const formdata = {
        grant_type: "password",
        username: "haxr",
        password: "1234"
    };

    try {
        const resp = await axios.post(USE_TOKEN_ENDPOINT, formdata, {
            headers
        });

        if(resp.data['id']===-1){
            console.log("토큰 유효기간 만료");
            return "tokenExpiration"
        }


        if (resp.data['access'] * 1 > limit_access) {
            console.log("GPU 제한 페이지");
            return "gpuWating";
        } 
        
        else if(resp.data['access'] * 1 > 0){
            console.log(resp.data['access']+"번 요청함");
            console.log("GPU 제한 안함");
            return 'ok';
        }

    } catch (error) {
        console.error(error);
        return error;
    }
};

export default gpuUse;