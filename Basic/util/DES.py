from binascii import b2a_hex, a2b_hex
from Crypto.Cipher import DES
key = '12345678' #长度必须是8位的
text = 'simonzhang.net ' #长度必须是8的倍数,我用空格补的
# 实例化
obj = DES.new(key)
# 加密
cryp = obj.encrypt(text)
pass_hex = b2a_hex(cryp)
print(pass_hex)
print('=' * 20)
# 解密
get_cryp = a2b_hex(pass_hex)
after_text = obj.decrypt(get_cryp)
print(after_text)