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
 * 
 * 
 * 아래 코드처럼 다른 컴포넌트에서 onRemove를 실행시키면 
 * DeleteComment 함수를 실행할 수 있다.
 * const onRemove = async () => {
    const rep = await DeleteComment({Comment_id : 19, WriteUser_id : 1});
    alert(rep.message);
  }
 * 
 */

    const {Comment_id, WriteUser_id} = props;

    try{
        // 사용자 로그인 확인.
        const userInfo = await checkToken();
        // 로그인이 안돼있는 등 사용자 인증 문제가 존재.
        if(userInfo === -1 || parseInt(userInfo.User_id) === -1){
            console.log("로그인 안됨.");
            return -1;
        } 
        const token = localStorage.getItem('access_token');
        // 작성자와 사용자의 id가 다르다면 문제 발생.
        if(WriteUser_id !== parseInt(userInfo.User_id)) {
            console.log("글쓴이 : "+WriteUser_id);
            console.log("사용자 : "+userInfo.User_id);
            return -1;
        }
        const data = {"Comment_id": Comment_id, 
                        "User_id": WriteUser_id};
        const response = await axios.delete('/api/v1/comment/delete', {
            headers: {
                Authorization: `Bearer ${token}`
            },
            data: data
            });
        
        return response.data;
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