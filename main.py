from auth import register, log_in
import os

def main()  :   
    while True:
        try:
            print("""1 - Registrar-se\n2 - Log in""")
            opcao = int(input(":"))

            match opcao:
                
                case 1:
                    register()
                    os.system("cls")

                case 2:
                    log_in()
                    break
        except ValueError:
            print("Digite apenas 1 ou 2: ")

if __name__ == "__main__":
    main()
