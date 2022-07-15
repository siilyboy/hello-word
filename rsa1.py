from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


key = RSA.generate(2048) # 实例化密钥对，密钥长度为2048bits
# 生成的私钥公钥都是bytes的数据，这里密钥转不转str都可以 .decode()默认用utf-8把bytes转str
# 私钥 解密
private_key = key.export_key().decode()
print(private_key, len(private_key),type(private_key))
# 公钥 加密
public_key = key.publickey().export_key().decode()
print(public_key, len(public_key),type(public_key))

# string.encode() 直接以默认的utf-8编码string为bytes

public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxLPL6Wd1Scu+GsyQEd/LD/oUI8H2/gg+
gSYPy5EfPQQWeXZFvhfhrRR5EOTBfud4Q93f46+l6Y2AynuALVB7FLL51RTy8eMhF9thUeouL+e7
9oUZZambCUx/Olmec/KO6kabKyFEFY/Zpyp9XyZQiu4dnLouxAv7IqernFKmVNRupkOQ/CECcY9w
KzWkZiASXiLbDUhqA5U1px9HmnYsIW03mG9w6LTvcPlaPPmGFGw36tTHY2lgNE37/VWVC2Lr0I2Z
HSUQbBWxSmyHOJ8MA8rJMzViEhnLTj326aUPo2Vo83Xkq4GN4SnyIw/PhdhiOY0mdiiZ+SDsxgXf
0Hs0YwIDAQAB
-----END PUBLIC KEY-----
"""

data = "Yiri123456"
# 实例化加密套件
public_key = RSA.importKey(public_key)
cipher = PKCS1_OAEP.new(public_key)
# 加密
c_data = cipher.encrypt(data.encode())
print(c_data,len(c_data))
# 解密
private_key = RSA.importKey(private_key)
d_cipher = PKCS1_OAEP.new(private_key) # 解密套件
org_data = d_cipher.decrypt(c_data)
print(org_data.decode())
