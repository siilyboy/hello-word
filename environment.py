import login

publickeyurl = "http://10.1.2.90:5600/rsa"
loginurl = "http://10.1.2.90:5600/sso-token"
username = "myfirstcount"
password = "Yiri123456"
# accessToken = getAccesstoken(username, password)
accessToken = login.getAccesstoken(username, password, publickeyurl, loginurl)
print("helkjasdasdssaj")