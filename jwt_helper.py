from os import error
import jwt
from user import User
import config


def encode_jwt_token(user : User):
    payload = {
        "email" : user.email,
        "designation" : user.designation,
        "fn" : user.fn,
        "ln" : user.ln,
        "user_id" : user.user_id,
        "project" : config.PROJECT_NAME
    }
    encoded_jwt = jwt.encode ({"some": payload}, "secret", algorithm="HS256")
    return encoded_jwt;

def decode_jwt_token(token): 
    try:   
        decoded_token = jwt.decode(token, "secret", algorithms="HS256")
        payload =  decoded_token["some"];
        return payload;
    except error as e:
        print(e)
        return None                
