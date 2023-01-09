"""
api에서 DB를 CRUD 할 때 사용하는 클래스를 정의
이 클래스는 모델과 스키마를 이용해서 DB의 CRUD를 구현

user = session.query(UserTable).filter(UserTable.id == uid).delete()
위 쿼리문에서 UserTable 같이 DB 모델은 인자로 주기 때문에
어떤 DB의 테이블도 유연하게 CRUD할 수 있다.

"""