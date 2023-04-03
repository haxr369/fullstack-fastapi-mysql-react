import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import './css/selectimg.css';
import axios from "axios";
import folder from "../statics/img/folderImg.png";
import checkToken from "../auth/checkToken";
import imageCompression from 'browser-image-compression';
import jwtDecode from "jwt-decode";

const SelectImg = () => {
  const navigate = useNavigate();
  const [files, setFiles] =useState(null);            //보내는 데이터
  const [imgFile, setImgFile] = useState(folder);   //보여주는 데이터

  async function handleImage(imageFile) {

  
    const options = {
      maxSizeMB: 0.2,
      maxWidthOrHeight: 1000
    }
    try {
      const compressedFile = await imageCompression(imageFile, options);
      //const objectURL = URL.createObjectURL(compressedFile)
      return compressedFile;

    } catch (error) {
      console.log(error);
      return 0;
    }
  
  }
  

  //받은 이미지를 file state에 저장하기
  const onLoadFile = async(e) => {
      
      const file = e.target.files[0];
      console.log(file.name);
      const file_ext = getExtensionOfFilename(file.name)
      const date = Date.now()
      const ch_name = ip+'_'+date+file_ext;
      const new_file = new File([file], ch_name, { type: file.type });
      console.log(new_file.name);

      try {
        const compressedFile = await handleImage(new_file);
        if(compressedFile === 0){
          console.log("압축 못함");
        } else {
          setFiles(compressedFile);
        }
      } catch (error) {
        console.log(error);
      }
      //console.log(files.size/1024/1024);
      //console.log(file)
      
      //setFiles(new_file);

      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onloadend =() =>{
        setImgFile(reader.result);
      }
  };

  const [ ip , setIp ] = useState('initalIp');

  useEffect(() => {
    axios.get('https://geolocation-db.com/json/')
    .then((res) => {
      setIp(res.data.IPv4)
      
      //console.log(ip);
    });

    checkToken();
    
  },[]);


const sendImg = async () => {
  const token = localStorage.getItem('access_token');
  
  const decodedIdToken = jwtDecode(token);

  const formData = new FormData();
  console.log("보내는 파일 크기 : "+files.size/1024);
  console.log("보내는 파일 이름"+files.name);
  console.log("유저 id : "+decodedIdToken['sub']);
  //formData.append('file', files,files.name);
  formData.append('file', files[0]);
  formData.append('UserNickName', decodedIdToken['sub']);
  
  const item = await axios({
    method: 'post',
    url: '/api/v1/items/uploadImg',
    data: formData,
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  }).then(() => {
    console.log('이미지 업로드 성공');
  }).catch((err) => {
    console.log('이미지 업로드 실패');
    alert(err);
    alert('이미지를 보내지 못했습니다. 다시 시도해주세요.');
    navigate('/selectimg');
  });
  //navigate(`/identyResults?file_name=${files.name}`);
  navigate('/identyResults', {state: {file_name: files.name}});
  
};

  const handleClick = async (e) => {


    if(files){
      sendImg();
    }
    else{
      alert("이미지를 보내지 못했습니다. 다시 시도해주세요.");
    }
    setImgFile(folder);
    
    
  };
  
  function getExtensionOfFilename(filename) {
  
    var _fileLen = filename.length;

    /** 
     * lastIndexOf('.') 
     * 뒤에서부터 '.'의 위치를 찾기위한 함수
     * 검색 문자의 위치를 반환한다.
     * 파일 이름에 '.'이 포함되는 경우가 있기 때문에 lastIndexOf() 사용
     */
    var _lastDot = filename.lastIndexOf('.');

    // 확장자 명만 추출한 후 소문자로 변경
    var _fileExt = filename.substring(_lastDot, _fileLen).toLowerCase();

    return _fileExt;
  };

  const createFile = (bits, name) => {
      try {
          // If this call fails, we go for Blob
          return new File(bits, name);
      } catch (e) {
          // If we reach this point a new File could not be constructed
          var myBlob = new Blob(bits);
          myBlob.lastModified = new Date();
          myBlob.name = name;
          return myBlob;
      }
  };
  return (
    
    <div className="imgContainer">
      <h1 className="title"> 식물 사진 식별</h1>
      <div className="subtitle"><h3 > 식별할 식물 사진을 선택하세요.</h3></div>
      <div className="cameraContain">
          <from className="upload_input">
              <input style={{display:"none"}} type= "file" id ="folderimage" accept="image/*" onChange={onLoadFile}   />
              <label htmlFor="folderimage" className="folder_contain" >
              <img className="cameraImg" htmlFor="image" alt="사진기로 찍어서 보내기" 
                  src={imgFile}/>
              </label>
          </from>
        <div >사진 선택하기</div>
      
      </div>
      <button onClick={handleClick}>식별하기</button>
    </div>  
    
    
  );

};

export default SelectImg;