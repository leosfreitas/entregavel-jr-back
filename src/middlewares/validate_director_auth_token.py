import os
import jwt
from fastapi import Request, Response, HTTPException

def validade_director_auth_token(request: Request, response: Response):
    token = request.cookies.get("director_auth_token")
    if not token:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    try:
        payload = jwt.decode(token.split(" ")[1], os.getenv("DIRECTOR_JWT_SECRET"), algorithms=["HS256"])
        director_id = payload.get("id")
        director_email = payload.get("email")
        request.state.auth_payload = {"director_id": director_id, "director_email": director_email}

    except jwt.PyJWTError:
        response.delete_cookie("director_auth_token")

        raise HTTPException(status_code=401, detail="Invalid JWT token")
    
    return True