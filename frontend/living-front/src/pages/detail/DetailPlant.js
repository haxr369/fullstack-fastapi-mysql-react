import { useState, useEffect } from 'react';
import {useNavigate, useLocation} from 'react-router-dom';
import './css/DetailPlant.css';
import Slider from "react-slick";
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import axios from 'axios';
import logo from '../statics/img/nuti.jpeg';
import DetailPlantInfo from '../APIs/DetailPlantInfo';
import SearchBar from '../dictionary/SearchBar';

const DetailPlant = () => {
    const [searchDetail, setSearchDetail] = useState(null);
    const navigate = useNavigate();
    const location = useLocation();
    const params = new URLSearchParams(location.search);
    const species = params.get('species');

    useEffect(() => {
        console.log(species);
        const runAsync = async () =>{
            //console.log("서치바의 쿼리 : "+searchTemp);
            console.log("props의 타입 : "+typeof(species));
            if(typeof(species) !== 'string'){
                navigate("/");
            }

            const result = await DetailPlantInfo(species);
            //console.log("검색 결과");
            //console.log(result.data);
            
            console.log(result.data);
            if(result === -1){
                alert("저희가 잘 모르는 식물입니다.");
                navigate("/");
            }
            setSearchDetail(result.data);

          }
      
        runAsync();

    }, []);

    if(!searchDetail){
        return 'Loding ...'
    }
    
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
    
    
    const wiki_link = `https://ko.wikipedia.org/wiki/${species}`;
    const namu_link= `https://namu.wiki/w/${species}`;

    return (
        <div className='contentMain'>
            <div className='title'>
                <div className='tileContain'>
                    <h1 className = 'contentTitle'>{species}</h1>
                    <h3 className = 'contentSub'>{searchDetail.Family_name} {searchDetail.Genus_name}</h3>
                </div>
                <div className='outsideContain'>
                    <h3 className='outsideTitle'>외부 자료 링크</h3>
                    <a href={wiki_link} className='outsideWiki'>wiki백과</a> <p style={{"margin":0}}/>
                    <a href={namu_link} className='outsideNamu'>나무위키백과</a>
                </div>
            </div>
            <hr/>

            <div className='plantContain'>
                <img className ='plantImg' src={logo} alt='Description of plant' />
            </div>

            <div className='overviewContain'>
                <h3 className = 'overviewTitle'>개요</h3>
                <div className='overviewContent'>
                {searchDetail.Describe}
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