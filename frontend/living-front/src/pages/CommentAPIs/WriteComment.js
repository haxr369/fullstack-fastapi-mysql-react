import axios from "axios";
import  PropTypes  from "prop-types";
import checkToken from '../auth/checkToken';

const WriteComment = async props => {
    /**
   * ^^^props^^^^
   * Compare_id, comment
   * 
   * 비교 팁 댓글을 DB에 작성하기.
   * 
   * 정상적인 유저는 checkToken에서
   * User_id(int), User_nickname(str), Access_count(int)를 출력한다.
   */

    const {comment, Compare_id} = props;

    try{
        // 사용자 로그인 확인.
        const userInfo = checkToken();
        // 로그인이 안돼있는 등 사용자 인증 문제가 존재.
        if(userInfo === -1 || parseInt(userInfo.User_id) === -1) return -1;
        const token = localStorage.getItem('access_token');
        const data = {"Contents": comment, 
                        "Compare_id": Compare_id, 
                        "User_id":parseInt(userInfo.User_id)};
        const response = await axios.post('/api/v1/comment/create',
             data,
             {
                headers: {
                  Authorization: `Bearer ${token}`,
                },
              });
        console.log("응답", response);
        return response;
    }
    catch (ex){
        console.log(ex);
        return -1;
    }

}

WriteComment.propTypes = {
    comment : PropTypes.string,
    Compare_id : PropTypes.number
}

export default WriteComment;