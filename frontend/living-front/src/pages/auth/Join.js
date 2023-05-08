import axios from "axios"
import jwtDecode from "jwt-decode";

/**
 *  Join({ User_ID: 'Hello', User_PASSWORD: 123 });
 *  위와 같은 방식으로 다른 컴포넌트에서 함수를 호출할 수 있습니다.
 */

const Join = async props => {

    /**
     * 가입할 아이디와 비밀번호를 props로 입력
     * 
     * User_ID
     * User_PASSWORD
     * 
     */
    const {User_nickname, User_PASSWORD} = props;

    try{
        const data = {"User_nickname": User_nickname, 
                        "User_password": User_PASSWORD};
        const response = await axios.post('/api/v1/login/joinService',
            data);
        console.log("응답", response);
        return response;
        
    }
    catch (ex){
        console.log(ex);
        return -1;
    }
}

export default Join;