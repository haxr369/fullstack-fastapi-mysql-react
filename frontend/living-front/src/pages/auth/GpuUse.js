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
    
};

export default gpuUse;