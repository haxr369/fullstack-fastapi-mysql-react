import axios from "axios"
import jwtDecode from "jwt-decode";

const tokenUse = async () => {
    const limit_access = 30;
    const token = localStorage.getItem('access_token');
    if (token) {
      const decodedIdToken = jwtDecode(token);
      console.log(decodedIdToken);
    }

    const USE_TOKEN_ENDPOINT = "http://192.168.0.203:8005/api/v1/login/usetoken"

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

        if (resp.data['access'] * 1 > limit_access) {
            console.log("GPU 제한 페이지");
            return null;
        } else {
            console.log("GPU 제한 안함");
            return resp;
        }
    } catch (error) {
        console.error(error);
        return null;
    }
};

export default tokenUse;