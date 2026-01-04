import bcrypt

def encrypt(senha_digitada):

    senha_bytes = senha_digitada.encode('utf-8')
    salt = bcrypt.gensalt() 
    hash_senha = bcrypt.hashpw(senha_bytes, salt)

    return hash_senha


