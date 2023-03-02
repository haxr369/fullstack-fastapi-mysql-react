import { useState, useEffect } from 'react';
import {useSearchParams} from 'react-router-dom';
import './css/SearchPlant.css';
import Slider from "react-slick";
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import axios from 'axios';
import logo from '../statics/img/nuti.jpeg';

const DetailPlant = props => {
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
                속씨식물문 쌍떡잎식물강 쐐기풀목 느릅나무과에 속하는 낙엽활엽수이다. 분류에서 보듯이 느릅나무와 친척간. 한자어로는 회화나무와 마찬가지로 괴목(槐木)이라고도 한다. 한국, 일본, 대만, 중국에 주로 분포한다.

다 자라면 높이는 20~35 m, 지름은 약 3 m에 이른다. 가지가 사방으로 고르게 퍼져서 위에서 보면 나무가 둥근 모양을 이루고, 잎이 많고 무성해서 넓은 나무 그늘을 만들기 때문에 정자나무로 많이 심었다. 나무껍질은 회백색이다. 꽃은 5월에 주로 핀다. 열매는 일그러진 원 모양이며 10월에 주로 익는다.

잘 자란다면 1천 년 이상 사는 나무라 우리나라에서는 총 14그루가 천연기념물로 지정되었다. 은행나무(19그루)와 소나무(19그루) 다음으로 많다. 이는 국가적으로도 신라시대부터 느티나무를 신성시해 벌채를 금지해 온 나무이기 때문이기도 하다.
                </div>
            </div>
            <div className='lifeContain'>
                <h3 className = 'lifeTitle'>생활사</h3>
                <div className='lifeTimeline'>
                        꽃 피는 월 (MM)	꽃 지는 월 (MM)	열매 맺는 월 (MM)	낙과하는 월 (MM)
                </div>
            </div>
            <div className='microContain'>
                <h3 className = 'microTitle'>잎의 초미세 구조</h3>
                    <img className='microImg' src='/logo512.png' alt='Description of image' />
                
            </div>




        </div>

    )

};

export default DetailPlant;