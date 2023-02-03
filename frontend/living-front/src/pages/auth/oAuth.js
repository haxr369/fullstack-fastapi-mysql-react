import axios from "axios"

const oAuth  =  async() => {

    //`.env.local` 파일을 통해 환경 변수를 사용할 수 있음 --> NEXT_PUBLIC으로 시작해야 next app이 인식을 함
    const OAUTH_TOKEN_ENDPOINT = "http://192.168.0.203:8005/api/v1/login/access-token"
    const OAUTH_CLIENT_ID = "haxr"
    const OAUTH_CLIENT_SECRET = "1234"

    // bearer 인증으로 보내기
    const encode = (
        `${OAUTH_CLIENT_ID}:${OAUTH_CLIENT_SECRET}`
    ).toString("base64");

    console.log(encode);
    const headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        Authorization: `Base64 ${encode}`
    };

    const formdata = {
        grant_type: "password",
        username : "haxr",
        password : "1234"
    };
    
    const resp = await axios.post(
        OAUTH_TOKEN_ENDPOINT,formdata,{
            headers
        });
    
    return resp;
    
}

export default oAuth;