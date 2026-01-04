from encrypt import encrypt
import bcrypt

def check(senha_digitada,hash_do_banco,nome):

    if bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_do_banco.encode('utf-8')):
        print(f"ACESSO PERMITIDO: Bem-vindo {nome}")
    else:
        print("ACESSO NEGADO!!!")


