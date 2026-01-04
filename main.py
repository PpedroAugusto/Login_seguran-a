import mysql.connector
from encrypt import encrypt
from check import check

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='122715',
    database='sistema_auth',
)

cursor = conexao.cursor()

def register():
    nome = input("Digite seu nome: ")
    try:
        cursor.execute("SELECT email FROM usuarios")
        resultados = cursor.fetchall()
        email = input("Digite seu email: ")
        if email in resultados:
            print("Email já cadastrado!!")
    
    except:
        ...
    senha_digitada = input("Digite uma senha: ")
    hash_senha = encrypt(senha_digitada)
    hash_banco = hash_senha.decode('utf-8')

    cursor.execute('INSERT INTO usuarios (nome, email, senha_hash) VALUES(%s,%s,%s)', (nome, email,hash_banco))
    conexao.commit()
    
    
def log_in():
    cursor.execute('SELECT * FROM usuarios')
    resultados = cursor.fetchall()

    while True: 
        email_digitado = input("Email: ")
        for usuario in resultados:
            id, nome, email, hash_do_banco = usuario
            if email == email_digitado:
                senha_digitada = input("Senha: ")
                check(senha_digitada, hash_do_banco)
                break
        else:
            print("Email não encontrado")
                
            

while True:
    print("""1 - Registrar-se
2 - Log in""")
    opcao = int(input(":"))

    match opcao:
        
        case 1:
            register()
            
        case 2:
            log_in()
            break


cursor.close()
conexao.close()