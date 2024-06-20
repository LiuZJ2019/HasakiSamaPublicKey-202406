import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
import pytest

PUBLIC_KEY = "hasaki-public-key.pem"

def TestBasae(PDF, signature):
    with open(PUBLIC_KEY) as f:
        pub_key = f.read()
        rsa_key_obj = RSA.importKey(pub_key)
        signer = pkcs1_15.new(rsa_key_obj)

    with open(PDF, "rb") as f:
        pdfs = f.read() 
        digest = SHA256.new(pdfs)
        try:
            signer.verify(digest, base64.b64decode(signature))
            return True
        except ValueError:
            print(ValueError)
            return False
        
RES = TestBasae("test.pdf",
                'T/eHFZF3UXkBuEJ7LDfrnYyGRKquT3PffI86nrdJBpan1DNxCIPisBpuBk+Auy1nSzhyj0xlF84dlhN6TZe9ejftyqqZOx78snAb0eph8lSz/6kAPqxsAH32Czdgt+RnldXAchBUw/saijp12AuByY4pPsdqUmKURl6hFr9+4WJcbU9i1OGlobzTrEXMCHt8TWH4Mi+6kzEqXbevetaI5MrYaSMjSs6W8lLLYV2akKkUANgRhtxzha1/MBQ76bWUdjJOZPfUhkWGdN3joFdeoPpDvioN4Z7LwA/v4XW/k+OLOXpByu6EMfvBaT7+dkNbaZ4nF4f/ZXr4ULIhQvJqPw==')
print(RES)

@pytest.mark.parametrize("PDF, signature", [("test.pdf",
                                            'T/eHFZF3UXkBuEJ7LDfrnYyGRKquT3PffI86nrdJBpan1DNxCIPisBpuBk+Auy1nSzhyj0xlF84dlhN6TZe9ejftyqqZOx78snAb0eph8lSz/6kAPqxsAH32Czdgt+RnldXAchBUw/saijp12AuByY4pPsdqUmKURl6hFr9+4WJcbU9i1OGlobzTrEXMCHt8TWH4Mi+6kzEqXbevetaI5MrYaSMjSs6W8lLLYV2akKkUANgRhtxzha1/MBQ76bWUdjJOZPfUhkWGdN3joFdeoPpDvioN4Z7LwA/v4XW/k+OLOXpByu6EMfvBaT7+dkNbaZ4nF4f/ZXr4ULIhQvJqPw==')])
def test_unit_1(PDF, signature):
    assert TestBasae(PDF, signature) == True

@pytest.mark.parametrize("PDF, signature", [("test.pdf",
                                            'T/aeHFZF3UXkBuEJ7LDfrnYyGRKquT3PffI86nrdJBpan1DNxCIPisBpuBk+Auy1nSzhyj0xlF84dlhN6TZe9ejftyqqZOx78snAb0eph8lSz/6kAPqxsAH32Czdgt+RnldXAchBUw/saijp12AuByY4pPsdqUmKURl6hFr9+4WJcbU9i1OGlobzTrEXMCHt8TWH4Mi+6kzEqXbevetaI5MrYaSMjSs6W8lLLYV2akKkUANgRhtxzha1/MBQ76bWUdjJOZPfUhkWGdN3joFdeoPpDvioN4Z7LwA/v4XW/k+OLOXpByu6EMfvBaT7+dkNbaZ4nF4f/ZXr4ULIhQvJqPw==')])
def test_unit_2(PDF, signature):
    assert TestBasae(PDF, signature) == False

