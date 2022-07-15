import requests

def getPublicKey(url):

    req = requests.request('post',url=url)
    return  req.text

if __name__ == '__main__':
    publicKey = getPublicKey("http://10.1.2.90:5600/rsa")
    print(publicKey)