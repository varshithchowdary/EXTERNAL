import hashlib
def cal(text):
    encoded_text=text.encode('utf-8')
    sha1_hash=hashlib.sha1()
    sha1_hash.update(encoded_text)
    return sha1_hash.hexdigest()
print('text:')
text=input()
print(cal(text))