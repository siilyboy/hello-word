import rsa
import requests
import json

def getAccesstoken(username, password, publickeyurl="http://10.1.2.90:5600/rsa", loginurl="http://10.1.2.90:5600/sso-token"):
    """
    publickeyurl是获取公钥的url,默认值：http://10.1.2.90:5600/rsa
    loginurl是登录url，默认值：http://10.1.2.90:5600/sso-token
    """

    #获取公钥
    publickey = rsa.getPublicKey(publickeyurl)
    #
    # #定义密码
    # plaintext = "Yiri123456"

    #加密密码
    key = rsa.RsaEncrypt(password, publickey)

    #定义请求参数headers
    headers = {
        "Content-Type": "application/json",
        # "Host": "10.1.2.90:5600",
        # "Content-Length": "385",
        # "Accept": "application/json, text/plain, */*",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        # "Content-Type": "application/json",
        # "Origin": "http://10.1.2.90:5600",
        # "Referer": "http://10.1.2.90:5600/login",
        # "Accept-Encoding": "gzip, deflate",
        # "Accept-Language": "zh-CN,zh;q=0.9",
        # "Connection": "close"
    }

    #定义请求参数body
    # UserName = "myfirstcount"
    PassWord = key.decode(encoding='utf-8')
    loger = {'UserName': username, 'Password': PassWord}
    #发送请求
    req = requests.post(url=loginurl, headers=headers, json=loger)
    #获取响应对象
    res = req.json()
    # print(res)
    # # res = json.dumps(req)
    return res


if __name__ == '__main__':
    publickeyurl = "http://10.1.2.90:5600/rsa"
    loginurl = "http://10.1.2.90:5600/sso-token"
    username = "yirichongqing"
    password = "123456Abc"
    # accessToken = getAccesstoken(username, password)
    accessToken = getAccesstoken(username, password, publickeyurl, loginurl)

    with open("token.txt", "w+", encoding='UTF-8') as f:
        json.dump(accessToken, f, indent=4)

    with open("token.txt", "r", encoding='UTF-8') as f:
        token = json.load(f)
    # print(token[access_token])
    print(token)
    print(token['access_token'])




    # print(accessToken)
