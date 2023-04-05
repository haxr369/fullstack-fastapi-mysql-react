import axios from "axios"
import jwtDecode from "jwt-decode";

const checkToken = async () => {
    const limit_access = 30;
    const token = localStorage.getItem('access_token');
    if (token) {
      const decodedIdToken = jwtDecode(token);
      //const timestamp = parseInt(new Date().getTime()/1000);
      console.log(decodedIdToken);
      //console.log(timestamp);
    }
    const TEST_TOKEN_ENDPOINT = "/api/v1/login/testToken"
    const headers = {
        'accept': 'application/json',
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
    };
    try{    
        const result = await axios.get(TEST_TOKEN_ENDPOINT,  {
            headers
        });
        return result;
    }
    catch (ex) {
        console.log(ex);
        return -1;
    }
}
export default checkToken;