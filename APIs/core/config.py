import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, validator

"""
템플릿에서는 postgres DB를 사용하지만
우리는 mysql을 사용한다.

"""
class Settings(BaseSettings):

    ML_PARMS : str = "/code/app/ML/outside/checkpoint-27.pth"
    CATEGORY_INFO : str = "/code/app/ML/outside/cat_info.json"
    SAMPLES_V1 : str = "/code/app/Sample_images/test/"


    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "rkwmdkrkwmdkrkwmdk" #secrets.token_urlsafe(32)

    ALGORITHM = "HS256"
    # 60 minutes * 24 hours * 8 days = 8 days || 토큰 유효기간 = 2분
    ACCESS_TOKEN_EXPIRE_MINUTES = 2
    SERVER_NAME: str = 'livinglab-with-fastapi'
    SERVER_HOST: str = 'backend-livinglab'  #AnyHttpUrl = 'http://172.28.0.2:8005'
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'

    BACKEND_CORS_ORIGINS: List[str] = ["http://localhost", "http://211.188.69.4:3000/",
                                              "frontend-livinglab", 
                                              "http://local.dockertoolbox.tiangolo.com"]

    UPLOAD_DIRECTORY : str = '/code/app/Uploaded_images'
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = 'react-fastapi-mysql'
    

    MYSQL_HOST: str = 'db'
    MYSQL_USER: str = 'apiman'
    MYSQL_PASSWORD: str = '0601'
    MYSQL_DB: str = 'plantLab'
    SQLALCHEMY_DATABASE_URI: str = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True) #MYSQL DSN의 유효성 검사.
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        
        user_name = values.get("MYSQL_USER")
        user_pwd = values.get("MYSQL_PASSWORD")
        db_host = values.get("MYSQL_HOST")
        #db_port = '3306'
        db_name = values.get('MYSQL_DB')
        DATABASE = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8'%( #DB를 선언하기 위한 표준 사용법. DB url 선언
            user_name,
            user_pwd,
            db_host,
            db_name,
        )
        return DATABASE
    

    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None

    @validator("EMAILS_FROM_NAME")
    def get_project_name(cls, v: Optional[str], values: Dict[str, Any]) -> str:
        if not v:
            print("values : ",values)
            return values["PROJECT_NAME"]
        return v

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    @validator("EMAILS_ENABLED", pre=True)
    def get_emails_enabled(cls, v: bool, values: Dict[str, Any]) -> bool:
        return bool(
            values.get("SMTP_HOST")
            and values.get("SMTP_PORT")
            and values.get("EMAILS_FROM_EMAIL")
        )

    EMAIL_TEST_USER: EmailStr = "test@example.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = 'first@example.com'
    FIRST_SUPERUSER_PASSWORD: str= '0601'
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True


settings = Settings()