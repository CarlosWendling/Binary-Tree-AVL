from modules.menu import show_menu

def is_number():
    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("Por favor, digite um número válido")


def main():
    valid_values = [0,1,2,3,4,5,6,7,8,9]

    while True:
        show_menu()

        while True:
            print("O que você deseja fazer: ")
            choice = is_number()
            if choice in valid_values:
                break
            else:
                print("Número inválido. Tente novamente")


        match choice:
            case 0:
                print("Saindo...")
                break
                
            case 1:
                input("Qual número você deseja inserir: ")
                
            case 2:
                input("Qual número você deseja buscar: ")
                
            case 3:
                input("Qual número você deseja excluir: ")
                
            case 4:
                print("Caminho Pré-Ordem: ")
                
            case 5:
                print("Caminho Em Ordem: ")
                
            case 6:
                print("Caminho Pós-Ordem: ")
                
            case 7:
                print("Altura: ")
                
            case 8:
                print("Balanceamento da árvore: ")
                
            case 9:
                print("Árvore: ")
                
if __name__ == "__main__":
    main()