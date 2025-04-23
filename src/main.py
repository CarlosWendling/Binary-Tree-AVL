from modules.menu import show_menu
from modules.Tree import Node, Tree

def is_number():
    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("Por favor, digite um número válido")


def main():
    valid_values = [0,1,2,3,4,5,6,7,8,9]

    # Inicializando a árvore vazia
    tree = Tree()
    root = None

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
                print("Qual número você deseja inserir: ")
                num = is_number()

                root = tree.insert(root, num)
                print(f'O número {num} foi inserido!')
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
                tree_height = tree.get_height(root)
                print(f'A árvore tem {tree_height} de altura')
                
            case 8:
                print("Balanceamento da árvore: ")
                
            case 9:
                tree.print_tree(root)
                
if __name__ == "__main__":
    main()