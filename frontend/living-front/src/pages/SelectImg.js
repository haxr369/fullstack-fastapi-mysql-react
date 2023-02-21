import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useState } from "react";
import './css/selectimg.css';
import axios from "axios";
import folder from "./statics/img/folderImg.png";
import checkToken from "./auth/checkToken";

const SelectImg = () => {
  const navigate = useNavigate();

  const [files, setFiles] =useState(null);            //보내는 데이터
  const [imgFile, setImgFile] = useState(folder);   //보여주는 데이터

  //받은 이미지를 file state에 저장하기
  const onLoadFile = (e) => {
      const file = e.target.files;
      console.log(file[0].name)
      console.log(file)
      const file_ext = getExtensionOfFilename(file[0].name)
      const date = Date.now()
      const ch_name = ip+'_'+date+file_ext;
      const new_file = createFile([file[0]],ch_name);

      console.log(new_file.name);
      setFiles(new_file);
      
      const reader = new FileReader();
      reader.readAsDataURL(file[0]);
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
    const formData = new FormData();
    formData.append('file', files);   
    await axios({
      method: 'post',
      url: 'http://211.188.69.4:8005/api/v1/items/userImg',
      data: formData,
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }).then( () => {

      const file_info = {
        ip_name : ip,
        file_name : files.name,
      }; 
      
      axios({
        method: 'post',
        url: 'http://211.188.69.4:8005/api/v1/items/userImgInfo',
        data: file_info,
        headers: {
          'Content-Type': 'application/json',
        },
      }).then(
        res =>{
          console.log("보내기 성공");
          navigate("/identyResults?file_name="+files.name);
        }
      ).catch( err => {
        console.log("이미지 정보 보내기 실패");
        
      });

    }).catch( err => {
      console.log("이미지 파일 보내기 실패");
      alert("이미지를 보내지 못했습니다. 다시 시도해주세요.");
      navigate("/selectimg");
    });
    

    
    
  }
  


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