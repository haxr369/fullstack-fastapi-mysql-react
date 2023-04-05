import axios from "axios"
import jwtDecode from "jwt-decode";

const gpuUse = async () => {
    const limit_access = 30;
    const token = localStorage.getItem('access_token');
    if (token) {
      const decodedIdToken = jwtDecode(token);
      //const timestamp = parseInt(new Date().getTime()/1000);
      console.log(decodedIdToken);
      //console.log(timestamp);
    }

    const USE_TOKEN_ENDPOINT = "/api/v1/login/usetoken"

    const headers = {
        accept: "application/json",
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      };
    /**
    const formdata = {
        grant_type: "password",
        username: "haxr",
        password: "1234"
    };
     */

    try{
      const result = axios.post(USE_TOKEN_ENDPOINT, null, {
        headers: headers,
      })
      return result;
    }
    catch (ex) {
        console.log(ex);
        return -1;
    }
    /**
    const accessCountUp = () => {
        return 
          .then((res) => {
            console.log(res);
            if (res.data.User_id === -1) {
              console.log("토큰 유효기간 만료");
              return "tokenExpiration";
            }
      
            if (res.data.Access_count  > limit_access) {
              console.log("GPU 제한 페이지");
              return "gpuWating";
            }
      
            if (res.data.Access_count> 0) {
              console.log(res.data.Access_count + "번 요청함");
              console.log("GPU 제한 안함");
              return 'ok';
            }
          })
          .catch((error) => {
            console.error(error);
            return error;
          });
      };

    try {
        accessCountUp();
    } catch (error) {
        console.error(error);
        return error;
    }
     */
};

export default gpuUse;