from pyoauth2 import Client

KEY = ''
SECRET = ''
CALLBACK='https://lewistest2.herokuapp.com/callback'

client = Client(KEY, SECRET,
                site='https://app.procore.com',
                authorize_url='https://app.procore.com/oauth/authorize',
                token_url='https://app.procore.com/oauth/token')

print ('-' * 80)
authorize_url = client.auth_code.authorize_url(redirect_uri=CALLBACK)
print ('Go to the following link in your browser:')
print (authorize_url)
print ('-' * 80)

code = input('Enter the verification code and hit ENTER when you\'re done:')
code = code.strip()
access_token = client.auth_code.get_token(code, redirect_uri=CALLBACK, parse='query')
print ('token', access_token.headers)

print ('-' * 80)
print ('get user info')
ret = access_token.get('/user')
print (ret.parsed)

print ('-' * 80)
print ('create a repos')
ret = access_token.post('/user/repos', name='test_repo', headers={'content-type': 'application/json'})
print (ret.parsed)
