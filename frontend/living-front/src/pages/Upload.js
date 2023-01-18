import axios from "axios";
import React from "react";
import { useState } from "react";
import './css/selectimg.css';

const Upload =() => {
    const [files, setFiles] =useState('');

    //받은 이미지를 file state에 저장하기
    const onLoadFile = (e) => {
        const file = e.target.files;
        console.log(file);
        setFiles(file);
    }
    
    //file에 저장한 이미지를 form 형식으로 파싱하고,
    // axios를 이용해서 서버에 전송
    const handleClick = (e) => {
        const formdata = new FormData();
        formdata.append('uploadImage', files[0]);   

        const config = {
            Headers:{
                'content-type' : 'multipart/form-data',
            },
        };
        //api 주소로 formdata를 config 형식으로 보낸다.
        axios.post('api', formdata, config);
        console.log('이미지 전송!!')
    };



    return (
    <>
        <div className="upload_wrap">
            <from className="upload_input">
                <input style={{display:"none"}} type= "file" id ="folderimage" accept="img/*" onChange={onLoadFile}   />
                <label htmlFor="folderimage" className="folder_contain" >
                <img className="cameraImg" htmlFor="image" alt="사진기로 찍어서 보내기" src={require("./statics/img/folderImg.png")}/>
                </label>
            </from>
        </div>
        
        <button onClick={handleClick}>저장하기</button>
    </>
    );

};
/**
 *             <from className="upload_input">
                <input style={{display:"none"}} type= "file" id ="cameraimage" accept="img/*" onChange={onLoadFile}   />
                <label htmlFor="cameraimage">
                    <div className="folder_contain">
                        <img className="cameraImg" htmlFor="image" alt="사진기로 찍어서 보내기" src={require("./statics/img/cameraImg.png")}/><br/>
                        <div>사진기로 찍어서 보내기</div>
                    </div>
                </label>
            </from>
 * 
 */
export default Upload;


