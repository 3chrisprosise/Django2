import hashlib

def md5(str):
    str = str.encode('utf-8')
    m = hashlib.md5()
    m.update(str)
    return m.hexdigest()


md5_code = md5("value")
print(md5_code)
print(hashlib.md5)

