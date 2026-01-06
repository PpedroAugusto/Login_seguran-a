from auth import register, log_in

def main()  :   
    while True:
        print("""1 - Registrar-se\n2 - Log in""")
        opcao = int(input(":"))

        match opcao:
            
            case 1:
                register()
                
            case 2:
                log_in()
                break

if __name__ == "__main__":
    main()
