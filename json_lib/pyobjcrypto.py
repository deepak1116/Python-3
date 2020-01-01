import base64
import hashlib
import json
from Crypto import Random
from Crypto.Cipher import AES

class Crypter:
    def __init__(self,key):
        self.key = hashlib.sha256(key.encode()).digest()
    @staticmethod
    def object_encrypt(key,raw):
        raw = Crypter._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key,AES.MODE_CBC,iv)
        return base64.b64encode(iv + cipher.encrypt(raw)).decode()

    @staticmethod
    def object_decrypt(key,raw):
        raw = base64.b64decode(raw)
        iv = raw[:AES.block_size]
        cipher = AES.new(key,AES.MODE_CBC,iv)
        return Crypter._unpad(cipher.decrypt(raw[AES.block_size:])).decode()

    def dictionary_convert(self,dictionary,option=True):
        for obj_key, value in dictionary.items():
            if not isinstance(value, (dict, list)):
                if option:
                    value = Crypter.object_encrypt(self.key,value)
                elif not option:
                    value = Crypter.object_decrypt(self.key,value)
                dictionary.update({obj_key: value})
            else:
                Crypter.inner_check(self,value,option=option)
        return dictionary

    def list_convert(self,list_obj,option=True):
        for value in list_obj:
            if not isinstance(value, (dict, list)):
                index = list_obj.index(value)
                if option:
                    list_obj[index] = Crypter.object_encrypt(self.key, value)
                elif not option:
                    list_obj[index] = Crypter.object_decrypt(self.key, value)
            else:
                Crypter.inner_check(self,value,option=option)
        return list_obj

    def inner_check(self,object,option=True):
        if isinstance(object, dict):
            object = Crypter.dictionary_convert(self,object,option=option)
        elif isinstance(object, list):
            object = Crypter.list_convert(self,object,option=option)
        return object
    def encrypt_json(self,json_obj):
        python_obj = json.loads(json_obj)
        new_object = Crypter.inner_check(self,python_obj,option=True)
        return new_object

    def decrypt_json(self,enc_json_obj):
        enc_python_obj = json.loads(enc_json_obj)
        dec_obj = Crypter.inner_check(self,enc_python_obj,option=False)
        return dec_obj

    @staticmethod
    def _pad(s, bs=AES.block_size):
        return (s + (bs - len(s) % bs) * chr(bs - len(s) % bs)).encode()

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s) - 1:])]