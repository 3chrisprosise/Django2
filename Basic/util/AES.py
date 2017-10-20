import string
import base64
import random

from Crypto.Cipher import AES


class AESecrypt():  
    def __init__(self, key, padding='\0'):
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度
        self.key = key
        self.iv = key[:AES.block_size]
        self.mode = AES.MODE_CBC
        self.padding = padding
        # self.is_unicode = False
    # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数

    def encrypt(self, text):
        # if isinstance(text, unicode):
        #     text = text.encode('utf-8')
            # self.is_unicode = True
        cryptor = AES.new(self.key, self.mode, IV=self.iv)
        length = AES.block_size
        count = len(text)
        add = count % length
        if add:
            text = text + (self.padding * (length - add))
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串用base64转化
        return base64.b64encode(self.ciphertext)
    # 解密后，去掉补足的'\0'用strip() 去掉

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, IV=self.iv)
        plain_text = cryptor.decrypt(base64.b64decode(text)).rstrip(self.padding)
        # return plain_text.decode('utf-8') if self.is_unicode else plain_text
        return plain_text

if __name__ == '__main__':  


    # e_text_en = tool.encrypt('my_text')
    # print(u'encrypt_text_en:{text}'.format(text=e_text_en))
    # d_text_en = tool.decrypt(e_text_en)
    # print('de_text_en:{text}'.format(text=d_text_en))



    # e_text_cn = tool.encrypt('中文文本'.encode(encoding="utf-8"))
    # print('encrypt_text_cn:{text}'.format(text=e_text_cn))
    # d_text_cn = tool.decrypt(e_text_cn)

    # key = ''.join(random.sample(string.ascii_letters + string.digits, 32))
    # print('key:{key}, length:{length}'.format(key=key, length=len(key)))
    # tool = AESecrypt(key)

    inputstr = str.encode('中文文本')

    print('encrypt_text_cn:{text}'.format(text=inputstr))

    d_text_cn = inputstr.decode()

    print(u'de_text_en:{text}'.format(text=d_text_cn))