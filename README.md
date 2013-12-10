Flask-AuthApi
=============

Flask-AuthApi is for simple API service authentication.

Install
====

  pip install https://github.com/kkzhang/Flask-AuthApi
  
Usage
====
  
It is quite simple.

* Set API_AUTH_KEYS in flask config
* Add decorator `auth_required()` below `app.route()`

add key=xxxx to url to authroize access
