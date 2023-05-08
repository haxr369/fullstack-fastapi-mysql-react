from fastapi import APIRouter

from api.api_v1.endpoints import  login , items,  users, search, plantcompare, comment,results #, auth, 

api_router = APIRouter()
api_router.include_router(login.router,  prefix="/login",tags=["login"])
#api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(results.router, prefix="/results", tags=["results"])
api_router.include_router(search.router, prefix="/search", tags=["search"])
api_router.include_router(plantcompare.router, prefix="/compare", tags=["compare"])
api_router.include_router(comment.router, prefix="/comment", tags=["comment"])