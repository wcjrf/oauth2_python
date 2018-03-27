from pyoauth2 import Client

KEY = '7e2d747e91a7c32b0f9af8c60c8864f2bc075ed6117f713980584c40c826f46a'
SECRET = '5537a8755dd49e2ab5cdcb4ec70349080d4b44da0464033f5df619bf122376a7'
CALLBACK = 'https://lewistest2.herokuapp.com/callback'

client = Client(KEY, SECRET,
                site='https://app.procore.com',
                authorize_url='/oauth/authorize',
                token_url='/oauth/token')

print '-' * 80
authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK, scope='user,public_repo')
print 'Go to the following link in your browser:'
print authorize_url
print '-' * 80

code = raw_input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK, parse='query')
print 'token', access_token.headers

print '-' * 80
print 'get user info'
ret = access_token.get('/user')
print ret.parsed

print '-' * 80
print 'create a repos'
ret = access_token.post('/user/repos', name='test_repo', headers={'content-type': 'application/json'})
print ret.parsed
