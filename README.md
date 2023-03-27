# University of Seoul CVLAB's Livinglab
fullstack-fastapi-mysql-react

## 개발목표
1. 사용자가 식물 분류 모델을 사용할 수 있도록 한다.
2. 식물 백과 사전으로 식물 정보를 얻을 수 있도록 한다.

## 기술 스택
도커를 이용해서 프록시, 프론트, 백, DB 서버를 운용한다.<p/>
프록시는 Nginx를, Frontend는 React를 사용하고, Backend는 Fastapi를, 그리고 DB는 Mysql을 사용한다.

## 관계형 데이터 모델링
![RDB_model drawio (3)](https://user-images.githubusercontent.com/53365713/227878482-74a7ec90-dbde-45d9-807d-7a9d0c200462.png)



<p/>
웹크롤러로 모은 사진과 서울숲 답사를 하면서 찍은 사진을 Sample image DB에 넣었다.<p/> 
식물 백과 DB와 Micro image에는 서울시립대 환경원예학과에서 제공한 데이터를 넣었다. <p/>

## Classifier
사전 학습된 MAE를 식물 데이터로 전이학습한 모델.


