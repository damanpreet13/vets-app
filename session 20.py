# Encrypting Data
import hashlib
password = input("Enter The Password:")
#encode password to UTF-8
password = password.encode('utf-8')
# generate the secure sha256 hash
password = hashlib.sha256(password).hexdigest()
print(password)