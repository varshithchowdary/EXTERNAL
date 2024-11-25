import hashlib
def cal(text):
    encoded_text=text.encode('utf-8')
    md5_hash=hashlib.md5()
    md5_hash.update(encoded_text)
    return md5_hash.hexdigest()
print("enter text")
text=input()
print(cal(text))