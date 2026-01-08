from database import conexao
import bcrypt

cursor = conexao.cursor()


def encrypt(senha_digitada):

    senha_bytes = senha_digitada.encode('utf-8')
    salt = bcrypt.gensalt() 
    hash_senha = bcrypt.hashpw(senha_bytes, salt)

    return hash_senha


def check(senha_digitada,hash_do_banco,nome):

    if bcrypt.checkpw(senha_digitada.encode('utf-8'), hash_do_banco.encode('utf-8')):
        print(f"ACESSO PERMITIDO: Bem-vindo {nome}")
    else:
        print("ACESSO NEGADO!!!")


def register():
    nome = input("Digite seu nome: ")
    while True:
        email = input("Digite seu email: ").strip()
        cursor.execute('SELECT email FROM usuarios WHERE email = %s', (email,))
        resultados = cursor.fetchall()
        if not resultados:
            break
        
        else:
            print("Email já cadastrado")
            continue

    senha_digitada = input("Digite uma senha: ").strip()
    hash_senha = encrypt(senha_digitada)
    hash_banco = hash_senha.decode('utf-8')

    cursor.execute('INSERT INTO usuarios (nome, email, senha_hash) VALUES(%s,%s,%s)', (nome, email, hash_banco))
    conexao.commit()
    
    
def log_in():
    while True: 
        email_digitado = input("Email: ")
        cursor.execute('SELECT nome, email, senha_hash FROM usuarios WHERE email = %s',(email_digitado,))
        resultados = cursor.fetchall()
        if resultados:
            senha_digitada = input("Senha: ")
            check(senha_digitada, resultados[0][2], resultados[0][0])
            break
        else:
            print("Email não encontrado")
                
