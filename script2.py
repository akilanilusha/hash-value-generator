import hashlib

text = input() #get input plain text

# Encode the text to bytes, then create hash object
hash_object_sha256 = hashlib.sha256(text.encode())
hash_object_md5 = hashlib.md5(text.encode())
hash_object_sha1 = hashlib.sha1(text.encode())
hash_object_sha224 = hashlib.sha224(text.encode())
hash_object_sha384 = hashlib.sha384(text.encode())
hash_object_sha512 = hashlib.sha512(text.encode())

# Get the hexadecimal representation of the hash
hash_hex = hash_object_md5.hexdigest()

print("Original text:", text)
print("SHA-256 hash:", hash_hex)
