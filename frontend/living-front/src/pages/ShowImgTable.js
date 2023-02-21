import axios from 'axios';
import { useState, useEffect } from 'react';
import {useSearchParams} from 'react-router-dom';
import './css/ShowImgTable.css';
import Slider from "react-slick";
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';

const ShowImgTable = props => {
    const {result} = props;

    const [rows, setRows] = useState('');
    const settings = {
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplaySpeed: 2000,
        pauseOnHover: true
      };
      
    const [imgUrl, setImgUrl] = useState([]);

    const getImages = async () => {
        for(let i=0; i<result['PlantImgs'].length; i++){
            await axios.get(`backend-livinglab/api/v1/items/twoImg/${result['Species']}/${result['PlantImgs'][i]}`, {
                responseType: 'blob'
                }).then(response => {
                    console.log("이미지 얻어!!");
                    const newurl = URL.createObjectURL(new Blob([response.data]));
                    setImgUrl(imgUrl => [...imgUrl, {id:i, imgurl:newurl}]);
                    //console.log(imgUrl.length);
                });
    
        }

    }
    useEffect(() => {
        //console.log(result);
        getImages();
       
        
    //useEffect는 의존성 배열안의 값이 변하면 항상 재생성된다.
    //만약 빈 배열이라면 화면이 랜더링될 때 생성된다.
    //내가 의존성 배열에 imgUrl을 넣는다면,넣을 때마다 재생성되니까 한번넣으면 3번 재생성되는 무한 랜더링이 발생한다...
/**
 *         if(i<result['plantImgs'].length){
            const j = i+1;
            setI(j);
        }
 */
      }, []);
    
    const imgList = imgUrl.map(imgs => 
        <img className="imgContent" key = {imgs.id}   alt={imgs.id} src={imgs.imgurl} />
    );

/**
 * 
 */
    return (
        <div className='topContain'>
            <h3 className='topName'> {result["Species"]}</h3> <h2 className="topPercent"> {result["Percent"].toFixed(2)*100}%</h2>
            <h5 className= 'topNameFG'> {result["Family"]} {result["Genus"]} </h5>
            <div className = "imgSlid">
                    <Slider {...settings}>
                        {imgList}
                    </Slider>
            </div>
     
        </div>
    );
};

export default ShowImgTable;
