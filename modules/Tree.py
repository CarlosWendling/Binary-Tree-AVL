class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class Tree:
    def search(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)

        return self.search(root.right, key)
    
    def get_height(self, node):
        if node:
            return node.height
        
        return 0
    

    def get_balance(self, node):
        if node:
            return self.get_height(node.left) - self.get_height(node.right)

        return 0
    

    def rotate_right(self, z):
        # z é o nodo desbalanceado
        y = z.left
        t2 = y.right # Filho a direita de y (vai virar filho a esquerda de z)

        # Rotação
        y.right = z
        z.left = t2

        # Atualizando alturas -> só precis atualizar dos nós que mudaram de nível
        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y


    def rotate_left(self, z):
        y = z.right
        t2 = y.left

        y.left = z
        z.right = t2

        z.height = max(self.get_height(z.left), self.get_height(z.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y
    

    # Função recursiva
    def insert(self, node, key):
        # Caso não encontrar um nó, irá inserir um novo
        if not node:
            return Node(key)
        
        if key > node.key:
            node.right = self.insert(node.right, key)
        elif key < node.key:
            node.left = self.insert(node.left, key)
        else:
            return node
        
        # Atualiza a altura de cada nodo recursivamente, junto da inserção dos seus descendentes
        node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1

        balance = self.get_balance(node)

        # Direita Simples
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Esquerda Simples
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Direita Dupla
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Esquerda Dupla
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node
    

    def print_pre_order(self, node):
        if not node:
            return []
        
        # Raiz->Sub.Arv da Esquerda->Sub.Arv da Direita
        return [node.key] + self.print_pre_order(node.left) + self.print_pre_order(node.right)
    

    def print_in_order(self, node):
        if not node:
            return []
        
        # Sub.Arv da Esquerda->Raiz->Sub.Arv da Direita
        return self.print_in_order(node.left) + [node.key] + self.print_in_order(node.right)


    def print_tree(self, node, prefix="", is_left=True, is_root=True):
        if node is not None:
            if is_root:
                print("   " + str(node.key))
            else:
                print(prefix + ("├── " if is_left else "└── ") + str(node.key))

            new_prefix = prefix + ("│   " if is_left and not is_root else "    ")

            if node.left:
                self.print_tree(node.left, new_prefix, True, False)
            else:
                print(new_prefix + "├── None")

            if node.right:
                self.print_tree(node.right, new_prefix, False, False)
            else:
                print(new_prefix + "└── None")
        else:
            print("Árvore vazia")