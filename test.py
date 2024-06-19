# encoding=utf-8
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15

# 把我公布的签名复制到这里
signature = b'T/eHFZF3UXkBuEJ7LDfrnYyGRKquT3PffI86nrdJBpan1DNxCIPisBpuBk+Auy1nSzhyj0xlF84dlhN6TZe9ejftyqqZOx78snAb0eph8lSz/6kAPqxsAH32Czdgt+RnldXAchBUw/saijp12AuByY4pPsdqUmKURl6hFr9+4WJcbU9i1OGlobzTrEXMCHt8TWH4Mi+6kzEqXbevetaI5MrYaSMjSs6W8lLLYV2akKkUANgRhtxzha1/MBQ76bWUdjJOZPfUhkWGdN3joFdeoPpDvioN4Z7LwA/v4XW/k+OLOXpByu6EMfvBaT7+dkNbaZ4nF4f/ZXr4ULIhQvJqPw=='

with open("hasaki-public-key.pem") as f:
    pub_key = f.read()
    rsa_key_obj = RSA.importKey(pub_key)
    signer = pkcs1_15.new(rsa_key_obj)

with open("test.pdf", "rb") as f:
    pdfs = f.read()
    digest = SHA256.new(pdfs)
    print(digest.hexdigest())
    try:
        signer.verify(digest, base64.b64decode(signature))
        print('Valid signature')
    except ValueError:
        print('Invalid signature')
