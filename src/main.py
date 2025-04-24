from modules.menu import show_menu
from modules.Tree import Node, Tree

def is_number():
    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("Por favor, digite um número válido")


def format_order(path_name:str, order:list):
    print(path_name, ", ".join(str(x) for x in order))


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

                num_exists = tree.search(root, num)

                if not num_exists:
                    root = tree.insert(root, num)
                    print(f'O número {num} foi inserido!')
                else:
                    print("Número já adicionado, não é aceito duplicados")

            case 2:
                print("Qual número você deseja buscar: ")
                num_search = is_number()

                num_exists = tree.search(root, num_search)
                if num_exists:
                    level = tree.get_height(root) + 1 - num_exists.height
                    print(f'O número {num_search} está no nível {level} da árvore!',)
                else:
                    print(f'O número {num_search} ainda não foi inserido na árvore')

            case 3:
                print("Qual número você deseja excluir: ")
                num_delete = is_number()

                num_exists = tree.search(root, num_delete)
                if num_exists:
                    root = tree.delete(root, num_delete)
                    print(f'O número {num_delete} foi removido!')
                else:
                    print(f'O número {num_delete} não se encontra na árvore')
                
            case 4:
                pre_order = tree.print_pre_order(root)
                format_order("Caminho Pré-Ordem:", pre_order)
                
            case 5:
                in_order = tree.print_in_order(root)
                format_order("Caminho Em Ordem:", in_order)
                
            case 6:
                post_order = tree.print_post_order(root)
                format_order("Caminho Pós-Ordem:", post_order)
                
            case 7:
                tree_height = tree.get_height(root)
                print(f'A árvore tem {tree_height} de altura')
                
            case 8:
                tree_balance = tree.get_balance(root)
                print(f'O balanceamento atual da árvore é de {tree_balance}')
                
            case 9:
                tree.print_tree(root)
                
if __name__ == "__main__":
    main()