import axios from "axios"

const oAuth  =  async () => {

    //`.env.local` 파일을 통해 환경 변수를 사용할 수 있음 --> NEXT_PUBLIC으로 시작해야 next app이 인식을 함
    const OAUTH_TOKEN_ENDPOINT = "/api/v1/login/access-token"
    const OAUTH_CLIENT_ID = "haxr"
    const OAUTH_CLIENT_SECRET = "1234"

    // bearer 인증으로 보내기
    const encode = (
        `${OAUTH_CLIENT_ID}:${OAUTH_CLIENT_SECRET}`
    ).toString("base64");

    console.log(encode);
    const headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        
    }; //Authorization: `Base64 ${encode}`

    const formdata = {
        grant_type: "password",
        username : "haxr",
        password : "1234"
    };
    try {
        const resp = await axios.post(
            OAUTH_TOKEN_ENDPOINT,formdata,{
                headers
            }).then((json) => {
                //console.log("token받고 난후!!"+json);
                //console.log(json.data['access_token']);
                if(json.data['access_token']){
                    console.log("토큰 저장!!")
                    localStorage.setItem('access_token',json.data['access_token']);
                }
            });
        
        return resp;
    }
    catch (ex) {
        console.log(ex);
        return -1;
    }
    
    
}

export default oAuth;