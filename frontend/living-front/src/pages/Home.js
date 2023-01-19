import { Link } from "react-router-dom";

const Home =() =>{
    return (
        <div>
            <h2>
                첫 시작 페이지
            </h2>
            <p>가장 먼저 보여지는 페이지입니다.</p>
            <Link to="/apitest"> API 서버와 연결 테스트</Link><br/>
            <Link to="/selectimg"> 이미지 전송 테스트</Link><br/>
        </div>
    );
};

export default Home;