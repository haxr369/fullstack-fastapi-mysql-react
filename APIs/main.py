from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from api.api_v1.api import api_router
from core.config import settings
#import pandas as pd

from crud import crud_plant
from schemas.plant_sch import SimpleSpeciesSCHCreate, DetailSpeciesSCHCreate

app = FastAPI(title='Project title',
            description='Description of your project',
            openapi_url='/api/openapi.json')

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        #allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        #disallow_unlisted_origins =True
    )

"""origins = [
    "http://172.28.0.3:3005",
    "http://172.28.0.3",
    "http://192.168.0.203:3005/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)"""

app.include_router(api_router, prefix=settings.API_V1_STR)
@app.get("/")
async def root():
    return {"message": "/plant 에서 사용자관리"}


#엑셀 내용 DB에 입력
"""def DB_setup():
    filname = "plant_149_DB.xlsx"
    df = pd.read_excel(filname)

    crud_simple = crud_plant.crud_SimpleSpecies
    crud_detail = crud_plant.crud_DetailSpecies

    print(str(df.shape[0])+"개의 식물 발견!!")

    #필요한 열은 1~8열 값.
    for i in range(df.shape[0]):
        Sname = df.iloc[i, 1]
        Gname = df.iloc[i, 2]
        Fname = df.iloc[i, 3]
        blossom = df.iloc[i, 4]
        Ffail = df.iloc[i, 5]
        Bfruit = df.iloc[i, 6]
        Bfail = df.iloc[i, 7]
        Describe = df.iloc[i, 8]

        simpleSCH = SimpleSpeciesSCHCreate(Species_name= Sname,
                                            Genus_name=Gname,
                                            Family_name=Fname)

        detailSCH = DetailSpeciesSCHCreate(
                                            Describe = Describe,
                                            Blossom=blossom,
                                            Flowers_fail =Ffail,
                                            Bear_fruit =  Bfruit,
                                            Bear_fail = Bfail)
        try :
            simple_result = crud_simple.create_with_species(simpleSCH)
            detail_result = crud_detail.create_with_species(detailSCH)
            
        except:
            print("crud 실패!!!")

DB_setup()
"""
