import hashlib
import hmac

# print(hash('Hello world'))
# print(hash('Hello world'))
# print(hash('Hello world'))
# print(hash('Hello world'))
# 3421448585534729756
# -2856554776667203903

print(hashlib.sha1(b'Hello world'))
print(hashlib.sha1(b'Hello world').hexdigest())
# 7b502c3a1f48c8609ae212cdfb639dee39673f5e

print(hashlib.sha1('Hello worldё'.encode('utf-8')).hexdigest())
# ad8463b54bde29736b9e410e6b29abef659bd412
print(hashlib.sha256('Hello worldё'.encode('utf-8')).hexdigest())
print(hashlib.sha512('Hello worldё'.encode('utf-8')).hexdigest())
print(hashlib.md5('Hello worldё'.encode('utf-8')).hexdigest())
print('*' * 52)
print(hmac.new(key=b'salt',
               msg='here'.encode('utf-8'),
               digestmod=hashlib.md5
               ).hexdigest())
print(hashlib.md5('here'.encode('utf-8')).hexdigest())
