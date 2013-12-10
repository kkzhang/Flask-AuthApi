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
* Create a ApiAuth instance

        from flask.ext.apiauth import ApiAuth
        auth = ApiAuth(app)

* Add decorator `auth.auth_required()` below `app.route()`

then you can add key=xxxx to url to authroize access
