# Python standard libraries
import json
import os

import config
import mysqlprovider
from jwt_helper import decode_jwt_token, encode_jwt_token
from user import User  

# Third-party libraries
from flask import Flask, redirect, request, url_for, jsonify, json
from flask_cors import CORS
from flask_login import (
    LoginManager,
    current_user,
    login_required   
)
from oauthlib.oauth2 import WebApplicationClient
import requests
  
# Configuration
GOOGLE_CLIENT_ID = config.GOOGLE_CLIENT_ID
GOOGLE_CLIENT_SECRET = config.GOOGLE_CLIENT_SECRET
GOOGLE_DISCOVERY_URL = (
   config.GOOGLE_DISCOVERY_URL
)

# Flask app setup
app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)

# OAuth 2 client setup
client = WebApplicationClient(GOOGLE_CLIENT_ID)

# add try and except
def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

@app.route("/google_login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
        
    # Prepare and send a request to get tokens! Yay tokens!
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    # token_temp  = token_response.json()
    # print(token_temp)
        # Now that you have tokens (yay) let's find and hit the URL
    # from Google that gives you the user's profile information,
    # including their Google profile image and email
    client.access_token
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    print(userinfo_response)
        # You want to make sure their email is verified.
    # The user authenticated with Google, authorized your
    # app, and now you've verified their email through Google!
    user_info = userinfo_response.json()
    if userinfo_response.json().get("email_verified"):       
        users_email = userinfo_response.json()["email"]
        
        # // Get user from db
        user  = mysqlprovider.get_user(users_email)
        if(user is not None):
            user = User(user['email'],user['fn'],user['ln'], user['user_id'], user['role_id'])      
            encoded_token = encode_jwt_token(user);
      
            return jsonify({"access_token" : encoded_token }), 200   
        else:
            return jsonify({"access_token" : None})            , 400
    else:
        return "User email not available or not verified by Google.", 400    
    

def get_jwt_token(request):
    authorization_header_value = request.headers.get('Authorization')
    if(authorization_header_value != None): 
        jwt_token = authorization_header_value.split(" ")[1]
        return jwt_token
    else:
        return None                

@login_manager.request_loader
def load_user_from_request(request):
    try:
            jwt_token = get_jwt_token(request)
            if(jwt_token != None):
                payload = decode_jwt_token(jwt_token)
           
                # Get user from db
                user = mysqlprovider.get_user(payload["email"])
                user = User(user['email'],user['fn'],user['ln'], user['user_id'], user['role_id']) 
                return user                  
    except os.error as e:        
        return None
    return None    

@app.route("/current-user")
def get_current_user():
    # user = mysqlprovider.get_user(current_user.get_id())
    user = mysqlprovider.get_user("netscho6@gmail.com")
    return json.dumps(user), 200

@app.route("/ping")
def ping():    
    return "Success", 200

@app.route("/ping-auth")
@login_required
def pingAuth():    
    return "message"

@app.route("/google_login")
def google_login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)    

@app.route("/genders")
def get_gender():
    gender = mysqlprovider.get_gender()
    return jsonify(gender), 200

@app.route("/create_basic_user_profile", methods = ['POST'])
def create_basic_user_profile():
    json_data = request.get_json()  
    result  = mysqlprovider.create_user_profile_basic(json_data)

    return jsonify(result), 200

@app.route("/create_address", methods=['POST'])    
def add_address():
    json_data = request.get_json()  
    result  = mysqlprovider.add_address(json_data)
    if( result.__contains__("Error")):
        return jsonify(result) , 400
    return jsonify(result), 200

@app.route("/other_details", methods=['POST'])    
def add_other_details():
    json_data = request.get_json()  
    result  = mysqlprovider.add_other_user_details(json_data)
    if( result.__contains__("Error")):
        return jsonify(result) , 400
    return jsonify(result), 200

@app.route("/")
def index():
    if current_user != None and  current_user.is_authenticated:
        return (
            "<p>Hello, {}! You're logged in! Email: {}</p>"
            "<div><p>Google Profile Picture:</p>"
            '<img src="{}" alt="Google profile pic"></img></div>'
            '<a class="button" href="/logout">Logout</a>'.format(
                current_user.name, current_user.email, current_user.profile_pic
            )
        )
    else:
        return '<a class="button" href="/google_login">Google Login</a>'

if __name__ == "__main__":
    app.run(ssl_context="adhoc")        