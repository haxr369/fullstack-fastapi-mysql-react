import React, { useState, useEffect } from 'react';
import axios from 'axios';

function WriteComment({ user, handleCommentSubmit }) { // id 전달 부분 삭제 , props에 유저 id정보 가져오는 부분 추가해야함

    const [comment, setComment] = useState("");


    const handleCommentChange = (e) => {
        setComment(e.target.value);
    };
    const handleSubmit = async (event) => {
        event.preventDefault();

        handleCommentSubmit(comment);

        setComment("");//

    };
    return (
        <div className="write-comment">
            <form>
                <div className="input-group">
                    <span>user.id</span> {/* user.name등으로 수정할 것 */}
                </div>
            </form>
            <textarea placeholder="댓글" value={comment} onChange={handleCommentChange} />
            <button type="submit" onClick={handleSubmit}>글쓰기</button>
        </div>
    );
}

function Comment({ data, props }) {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [password, setPassword] = useState("");
    const [isUserComment, setIsUserComment] = useState(false);
    const [modalVisible, setModalVisible] = useState(false);

    useEffect(() => {
        if (data.Comment_id === props.Comment_id) { //comment_id -> user_id로 바꿔야함
            setIsUserComment(true);
        }
    }, [data, props.User_id]);

    const onRemove = (data) => {
        if (isUserComment) {
            setIsModalOpen(true);
            props.onRemove(data.Comment_id);
        }
    };
    const onCancel = () => {
        setIsModalOpen(false);
        setPassword("");
        setModalVisible(false);
    };
    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    function onOffModal() { //모달창 상태를 변경하는 함수입니다.
        if (!modalVisible) {
            setModalVisible(true);
        } else {
            onCancel();
        }
    }
    const handlePasswordSubmit = () => {
        const typedPassword = password;
        props.handlePasswordSubmit(typedPassword);
        setPassword("");
    }
    //  여기서의 password 전달값을 상위 컴포넌트로 줘야함
    return (
        <div className="comment">
            <b>{"익명" + data.Comment_id}: </b> <span>{data.Contents}</span> {/* 유저 닉네임은 api 만들어지면 변경 할 것*/}
            <button onClick={() => { onRemove(data); onOffModal() }}>삭제</button>
            {modalVisible && isModalOpen && (
                <Modal password={password} handlePasswordChange={handlePasswordChange} onConfirm={handlePasswordSubmit} onCancel={onCancel} />
            )}
            {console.log("여기는 댓글 객체 password", password)}

        </div>
    );
}

function CommentList({ datas, onRemove, props }) { //users는 write해준 후 가져오면 된다.
    return (
        <div>
            {datas.map((data) => (
                <Comment
                    data={data}
                    key={data.Comment_id}
                    onRemove={onRemove}
                    props={props}
                />
            ))}
        </div>
    );
}

function CommentBoard({ datas, onRemove, props }) {
    return (
        <div>
            <h3>Comments:</h3>
            <CommentList datas={datas} onRemove={onRemove} props={props} />
        </div>
    );
}

function CommentBlock() {
    const [datas, setDatas] = useState([]);
    const [targetUser, setTargetUser] = useState(null);


    async function getData(id) {
        try {
            await axios.get(`/api/v1/comment/list/${id}`).then((response) => {

                setDatas(response.data);
                console.log("getData 로그", response);
            });
        } catch (error) {
            console.error(error);
        }
    }

    async function postData(data) {
        try {
            const token = localStorage.getItem('access_token');
            const response = await axios.post('/api/v1/comment/create',
                data,
                {
                    headers: {
                        Authorization: `Bearer ${token}`,
                    },
                });
            console.log("응답", response);
            window.location.replace("/commentTest")
        } catch (error) {
            console.error("에러응답", error);
        }
    };


    async function deleteData(Ddata) {
        try {
            //console.log("삭제로그: ", data)
            const token = localStorage.getItem('access_token');
            const data = {
                "Comment_id": Ddata.Comment_id,
                "User_id": 1
            }
            await axios.delete('/api/v1/comment/delete',
                {
                    data: data,
                    headers: {
                        Authorization: `Bearer ${token}`,
                    }
                }).then((response) => {
                    console.log("데이터 삭제");
                    //console.log(response);
                });
        } catch (error) {
            console.error(error);
        }
    };


    //새로고침시 댓글리스트 가져오기
    useEffect(() => {
        getData(3); //id 값에 해당하는 거로 상위 컴포넌트의 props를 가져오기
    }, []);
    /*
      useEffect(() => {
        getData(compare_plant.id);
      }, [compare_plant.id]); 챗gpt가 일케하래
    */

    const handleCommentSubmit = (comment) => {

        if (comment !== "") {
            const newData = { Contents: comment, Compare_id: 3, User_id: 2 } //user id는 user 구축 후 추가, compare id 수정해야함
            postData(newData);
            getData(3);
        }
        else {
            alert('코멘트를 작성해주세요');
        }
    };

    const handlePasswordSubmit = (typedPassword) => {
        if (!targetUser) {
            alert("Error");
        }
        //console.log(password, targetUser.Comment_id)
        console.log("전달된 pw1", typedPassword)
        if (typedPassword === String(targetUser.Comment_id)) { //유저 비번에 대한 정보는 api 만들어야하므로 일단 코멘트 아디로
            setDatas(datas.filter((data) => data.Comment_id !== targetUser.Comment_id));
            //댓글 삭제 api 가져와야함
            deleteData(targetUser);
            console.log(datas);
        } else {
            alert('비밀번호가 일치하지 않습니다');
        }
    };

    const onRemove = (id) => {
        const target = datas.find((data) => data.Comment_id === id); //comment_id -> user_id로 변경해야

        if (!target) {
            alert('해당하는 댓글이 없습니다');
            return;
        }
        setTargetUser(target);
    };


    var modal_props = { onRemove: onRemove, handlePasswordSubmit: handlePasswordSubmit, Comment_id: 6 } //삭제 타겟 수정해야
    return (
        <div>
            <WriteComment handleCommentSubmit={handleCommentSubmit} />
            <CommentBoard datas={datas} onRemove={onRemove} props={modal_props} />
        </div>
    );
}

function Modal({ password, handlePasswordChange, onConfirm, onCancel }) {
    return (
        <div className="modal">
            <div className="modal-content">
                <input type="text" placeholder="비밀번호" value={password} onChange={handlePasswordChange} />
                <div className="modal-buttons">
                    <button onClick={onConfirm}>확인</button>
                    <button onClick={onCancel}>취소</button>
                </div>
            </div>
        </div>
    );
}

function ComparePicture({ pic1, pic2 }) { //그림들은 나중에 옵젝으로 가져와서 이름 descript시에 써먹어야함
    return (
        <div className="picture-container">
            <div className="picture">
                <img src={require(`./statics/img/${pic1}`)} alt="Left" />
                <p>왼쪽</p>
            </div>
            <div className="picture">
                <img src={require(`./statics/img/${pic2}`)} alt="Right" />
                <p>오른쪽</p>
            </div>
        </div>
    );
}

function CompareTips({ tips }) {
    return (
        <div className="compare-tips">
            <h2>Comparison Tips</h2>
            <ul>
                {tips.map((tip, index) => (
                    <li key={index}>
                        <h3>{tip.title}</h3>
                        <p>{tip.content}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
}

function CommentTest() {
    const tips = [
        { title: 'Tip 1', content: 'This is the content for Tip 1.' },
        { title: 'Tip 2', content: 'This is the content for Tip 2.' },
        { title: 'Tip 3', content: 'This is the content for Tip 3.' },
    ];

    return (
        <div className="container">
            <ComparePicture className="compare-picture" pic1='logo192.png' pic2='logo512.png' /> {/*이미지 경로에 맞게 설정 다시*/}
            <div className="compare-container">
                <CompareTips className="compare-tips" tips={tips} />
                <CommentBlock className="comment" />
            </div>
        </div>
    );
}

export default CommentTest;