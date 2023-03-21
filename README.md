# University of Seoul CVLAB's Livinglab
fullstack-fastapi-mysql-react

## 개발목표
1. 사용자가 식물 분류 모델을 사용할 수 있도록 한다.
2. 식물 백과 사전으로 식물 정보를 얻을 수 있도록 한다.

## 기술 스택
도커를 이용해서 프록시, 프론트, 백, DB 서버를 운용한다.<p/>
프록시는 Nginx를, Frontend는 React를 사용하고, Backend는 Fastapi를, 그리고 DB는 Mysql을 사용한다.

## 개념적 데이터 모델링
![ER다이어그램 drawio](https://user-images.githubusercontent.com/53365713/222315523-9e87d12a-1c07-4027-9a35-2dcb5cb64165.png)

## 관계형 데이터 모델링
![RDB_model drawio](https://user-images.githubusercontent.com/53365713/222414405-2779ca10-f2a0-48d5-95c0-69f237585482.png)


<p/>
웹크롤러로 모은 사진과 서울숲 답사를 하면서 찍은 사진을 Sample image DB에 넣었다.<p/> 
식물 백과 DB와 Micro image에는 서울시립대 환경원예학과에서 제공한 데이터를 넣었다. <p/>

## Classifier
사전 학습된 MAE를 식물 데이터로 전이학습한 모델.


