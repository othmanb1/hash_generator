import hashlib

def hash_string(input_string):
    sha256_hash = hashlib.sha256()
    
    sha256_hash.update(input_string.encode())
    
    return sha256_hash.hexdigest()

input_string = input("Entrez une chaîne de texte à hasher : ")
print(f"Le hash SHA-256 de la chaîne '{input_string}' est : {hash_string(input_string)}")
