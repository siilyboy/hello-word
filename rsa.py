import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import requests

def getPublicKey(url):

    req = requests.post(url=url)
    return  req.text

def RsaEncrypt(plaintext, publickey):
    text = bytes(plaintext, encoding="utf8")
    rsakey = RSA.importKey(publickey)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    cipher_text = base64.b64encode(cipher.encrypt(text))
    return cipher_text


# def decode_content(text):
#     decodeStr = base64.b64decode(text)  # cipher_text是上面rsa加密的内容
#     prikey = Cipher_pkcs1_v1_5.new(RSA.importKey(private_key))
#     encry_text = prikey.decrypt(decodeStr, b'rsa', expected_pt_len=0)
#     encry_value = encry_text.decode('utf8')
#     print(encry_value)  # abcdefgh


if __name__ == '__main__':
    publickey = getPublicKey("http://10.1.2.90:5600/rsa")
    plaintext = "123456Abc"
    res = RsaEncrypt(plaintext, publickey)
    print(res)