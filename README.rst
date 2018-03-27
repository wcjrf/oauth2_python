=========
py-oauth2
=========

A Python wrapper for the OAuth 2.0 specification

Installation
------------

pip::
    
    pip install py-oauth2


easy_install::

    easy_install py-oauth2


Usage Examples
--------------

Demo for Google
---------------
Get user info::

    from pyoauth2 import Client

    CLIENT_ID = ''
    CLIENT_SECRET = ''
    REDIRECT_URL = ''
    SCOPE = 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email'

    client = Client(CLIENT_ID, CLIENT_SECRET,
                    site='https://www.googleapis.com/oauth2/v1',
                    authorize_url='https://accounts.google.com/o/oauth2/auth',
                    token_url='https://accounts.google.com/o/oauth2/token')

    print '-' * 80
    authorize_url = client.auth_code.authorize_url(redirect_uri=REDIRECT_URL, scope=SCOPE)
    print 'Go to the following link in your browser:'
    print authorize_url

    code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
    code = code.strip()
    access_token = client.auth_code.get_token(code, redirect_uri=REDIRECT_URL)
    print 'token', access_token.headers

    print '-' * 80
    print 'get user info' 
    ret = access_token.get('/userinfo')
    print ret.parsed


Demo for Douban
---------------
Get access_token::

    from pyoauth2 import Client

    KEY = ''
    SECRET = ''
    CALLBACK = ''

    client = Client(KEY, SECRET, 
                    site='https://api.douban.com', 
                    authorize_url='https://www.douban.com/service/auth2/auth',
                    token_url='https://www.douban.com/service/auth2/token')

    authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, scope='shuo_basic_w,douban_basic_common')

    access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK)


Get data::

    ret = access_token.get('/v2/user/~me')
    print ret.parsed

Upload image::

    ret = access_token.post('/shuo/v2/statuses/', text='content from py-oauth2', files={ 'image': open('/path/pic.jpg')})
    print ret.parsed


More:

`Examples <https://github.com/liluo/py-oauth2/wiki>`_

`Demo for Google <https://github.com/liluo/py-oauth2/wiki/Google>`_

`Demo for Douban(auth with code) <https://github.com/liluo/py-oauth2/wiki/Douban>`_

`Demo for Douban(auth with token) <https://github.com/liluo/py-oauth2/wiki/Douban2>`_

`Demo for Douban(auth with password) <https://github.com/liluo/py-oauth2/wiki/Douban3>`_

`Demo for GitHub <https://github.com/liluo/py-oauth2/wiki/GitHub>`_

`Demo for Weibo  <https://github.com/liluo/py-oauth2/wiki/Weibo>`_

`Demo for QQ  <https://github.com/liluo/py-oauth2/wiki/QQ-OAuth-2.0>`_

`Demo for Taobao  <https://github.com/liluo/py-oauth2/wiki/Taobao-OAuth-2.0>`_

`Demo for Box.com  <https://github.com/liluo/py-oauth2/wiki/Box.com>`_

`Demo for Instagram  <https://github.com/liluo/py-oauth2/wiki/Instagram>`_

Submitting a Pull Request
-------------------------
* Fork the repository.
* Create a topic branch.
* Implement your feature or bug fix.
* Add, commit, and push your changes.
* Submit a pull request.
