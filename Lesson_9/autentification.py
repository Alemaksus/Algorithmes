import hashlib

print(hashlib.sha1(b'Hello World!').hexdigest()) # sha1 - это встроенная функция хеширования. hexdigest - это рез-т в
# виде шестнадцатеричного числа

print(hashlib.sha1(b'Hello World.').hexdigest())

# 1-й способ аутентификации:
print(hashlib.sha1(b'qwgrhejkyjj' + b'Hello World!').hexdigest()) # 'qwgrhejkyjj' - это секретное слово, которого
# не должно было быть в теле письма.

# 2-й способ аутентификации:

s = hashlib.sha1(b'Hello World.').hexdigest()
print(s.encode('utf-8'))
print(hashlib.sha1(b'drfgsgs' + bytes(s.encode('utf-8'))).hexdigest())

