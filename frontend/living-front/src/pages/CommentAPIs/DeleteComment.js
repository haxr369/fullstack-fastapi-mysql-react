import axios from "axios";
import  PropTypes  from "prop-types";
import checkToken from '../auth/checkToken';

const DeleteComment = async props => {
/**
 * ^^^props^^^^
 * Compare_id, WriteUser_id
 * 
 * 비교 팁 댓글을 DB에서 삭제하기.
 * 
 * 정상적인 유저는 checkToken에서
 * User_id(int), User_nickname(str), Access_count(int)를 출력한다.
 */
    const {Comment_id, WriteUser_id} = props;

    try{
        // 사용자 로그인 확인.
        const userInfo = checkToken();
        // 로그인이 안돼있는 등 사용자 인증 문제가 존재.
        if(userInfo === -1 || parseInt(userInfo.User_id) === -1) return -1;
        const token = localStorage.getItem('access_token');
        // 작성자와 사용자의 id가 다르다면 문제 발생.
        if(WriteUser_id !== parseInt(userInfo.User_id)) return -1;
        const data = {"Comment_id": Comment_id, 
                        "User_id": WriteUser_id};
        const response = await axios.post('/api/v1/comment/delete',
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

DeleteComment.propTypes = {
    Comment_id : PropTypes.number,
    WriteUser_id : PropTypes.number
}


export default DeleteComment;