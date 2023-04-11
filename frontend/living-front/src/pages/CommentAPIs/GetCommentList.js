import axios from "axios";

const GetCommentList = async (Compare_id) => {

    /**
   * ^^^props^^^^
   * Compare_id
   * 비교 팁과 관련된 댓글들을 DB에서 가져오기.
   */

    try{
        console.log("비교팁 ID : "+Compare_id);
        const result = await axios.get(`/api/v1/comment/list/${Compare_id}`);
        return result;
    }    
    catch (ex){
        console.log(ex);
        return -1;
    }

}

export default GetCommentList;