from fastapi import APIRouter

from api.api_v1.endpoints import  login , items,  users, search #, auth, results

api_router = APIRouter()
api_router.include_router(login.router,  prefix="/login",tags=["login"])
#api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
#api_router.include_router(results.router, prefix="/results", tags=["results"])
api_router.include_router(search.router, prefix="/search", tags=["search"])
#api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
