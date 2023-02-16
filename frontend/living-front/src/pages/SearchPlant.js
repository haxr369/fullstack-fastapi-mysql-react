import { useState, useEffect } from 'react';
import {useSearchParams} from 'react-router-dom';
import './css/SearchPlant.css';
import Slider from "react-slick";
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import axios from 'axios';
import logo from './statics/img/logo512.png';

const SearchPlant = props => {
    const {result} = props;
    /**
     * const settings = {
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplaySpeed: 2000,
        pauseOnHover: true
      };

    const [imgUrl, setImgUrl] = useState([]);
    useEffect(() => {
        console.log(result['plantNo']);
        for(let i=0; i<result['plantImgs'].length; i++){
            axios.get(`http://192.168.0.203:8005/api/v1/items/twoImg/${result['plantNo']}/${result['plantImgs'][i]}`, {
                responseType: 'blob'
                }).then(response => {
                    console.log("이미지 얻어!!");
                    const newurl = URL.createObjectURL(new Blob([response.data]));
                    setImgUrl(imgUrl => [...imgUrl, {id:i, imgurl:newurl}]);
                    console.log(imgUrl.length);
                });
    
        }
    }, []);
    
    const imgList = imgUrl.map(imgs => 
        <img className="imgContent" key = {imgs.id}   alt={imgs.id} src={imgs.imgurl} />
    );
     * 
     * 
     * <Slider {...settings}>
                            {imgList}
                        </Slider>
     */
    
    const stages = [    { stage: "Seed", start: 0, end: 3 },    
                    { stage: "Sprout", start: 3, end: 7 },    
                    { stage: "Growth", start: 7, end: 12 },    
                    { stage: "Maturity", start: 12, end: 15 },    
                    { stage: "Decay", start: 15, end: 18 }  ];
         
    return (
        <div className='contentMain'>
            <div className='title'>
                <div className='tileContain'>
                    <h1 className = 'contentTitle'>느티나무</h1>
                    <h3 className = 'contentSub'>느티나무과 느티나무속</h3>
                </div>
                <div className='outsideContain'>
                    <h3 className='outsideTitle'>외부 자료 링크</h3>
                    <a href="https://ko.wikipedia.org/wiki/느티나무" className='outsideWiki'>wiki백과</a> <p style={{"margin":0}}/>
                    <a href="https://namu.wiki/w/느티나무" className='outsideNamu'>나무위키백과</a>
                </div>
            </div>
            <hr/>
            <div className='plantContain'>
                <img className ='plantImg' src={logo} alt='Description of plant' />
                
            </div>
            <div className='overviewContain'>
                <h3 className = 'overviewTitle'>개요</h3>
                <div className='overviewContent'>
                    1999년 2월 23일에 전주에서 태어난 오찬솔은 1남 1녀 중 첫째로 꿋꿋하게 살아왔다.거센 폭풍 같은 삶을 산 오찬솔을 결국 느티나무 개요를 쓰게되는데...
                </div>
            </div>
            <div className='lifeContain'>
                <h3 className = 'lifeTitle'>생활사</h3>
                <div className='lifeTimeline'>
                    여기에 식물의 timeline을 그릴 것
                </div>
            </div>
            <div className='microContain'>
                <h3 className = 'microTitle'>잎의 초미세 구조</h3>
                    <img className='microImg' src='/logo512.png' alt='Description of image' />
                
            </div>




        </div>

    )

};

export default SearchPlant;