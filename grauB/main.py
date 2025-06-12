import sys
import os
import pandas as pd
from menu import showMenuMain
from importaCsv import lerCsv, criaPessoas
from Pessoa import Pessoa
from datetime import datetime, date

sys.path.append(os.getcwd().replace("grauB", ""))

from grauA.modules.Tree import Tree, Node

# leitura do csv com os dados da árvore
choice = 99
while choice != 0:
  filePath = str(input("Digite o caminho do arquivo csv a ser lido:"))
  dadosPessoas = lerCsv(filePath)

  # se voltar um dataframe indica que o caminho do csv está certo
  if isinstance(dadosPessoas, pd.DataFrame):
      pessoasList = criaPessoas(dadosPessoas.values)
      choice = 0
  else:
      print(dadosPessoas)


# cria uma árvore AVL com base no campo
def criarArvore(pessoasList: list[Pessoa], campo: str) -> tuple[Tree, Node]:
  avl = Tree()
  root = None
  for pessoa in pessoasList:
      if campo == "CPF":
          root = avl.insert(root, pessoa.getCPF)
      elif campo == "Data":
          root = avl.insert(root, pessoa.getData)
      elif campo == "Nome":
          root = avl.insert(root, pessoa.getNome)

  return avl, root

# cria as 3 instâncias de árvore avl
avlCPF, rootCPF = criarArvore(pessoasList, "CPF")
avlData, rootData = criarArvore(pessoasList, "Data")
avlNome, rootNome = criarArvore(pessoasList, "Nome")

root = None
while choice != 99:
  # buscas por cpf, data e nome -> utilizam os métodos da classe tree e pessoa
  showMenuMain()
  choice = input("Digite o número da escolha o que você deseja fazer: ")
  if not choice.isnumeric():
      print("Digite um número")
      continue

  choice = int(choice)
  match choice:
      case 1:
          cpf = input("Digite o CPF que desejas buscar: ")
          if not cpf.isnumeric():
              print("CPF deve ser escrito apenas com números")
              continue
          cpf = int(cpf)

          if avlCPF.search(rootCPF, cpf):
            for pessoa in pessoasList:
              if pessoa.getCPF == cpf:
                print("")
                print(pessoa)
                print("")
                continue
          else:
            print("")
            print("Não há a pessoa com este CPF na árvore")
            print("")

      case 2:
        data_inicial_str = input("Data inicial (DD/MM/YYYY): ")
        data_final_str = input("Data final (DD/MM/YYYY): ")

        try:
            # chama o método da árvore para buscar datas dentro do intervalo
            data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y").date()
            data_final = datetime.strptime(data_final_str, "%d/%m/%Y").date()
            datas_encontradas = avlData.search_range(rootData, data_inicial, data_final)
            if not datas_encontradas:
                print("")
                print("Nenhuma pessoa encontrada no intervalo informado.")
                print("")
                continue

            for data in datas_encontradas:
                for pessoa in pessoasList:
                    if pessoa.getData == data:
                        print("\n" + str(pessoa))

        except ValueError:
            print("")
            print("Formato inválido de data. Use o formato DD/MM/YYYY.")
            print("")

      case 3:
        prefixo = input("Digite o início do nome a ser buscado: ").strip().lower()
        nomesEncontrados = avlNome.search_prefix(rootNome, prefixo)

        if nomesEncontrados:
          for nome in nomesEncontrados:
            for pessoa in pessoasList:
              if pessoa.getNome.lower() == nome.lower():
                print("")
                print(pessoa)
                print("")
        else:
          print("")
          print("Nenhuma pessoa encontrada com esse nome")
          print("")

      case 99:
        print("Até uma próxima!")
        choice = 99

      case others:
        print("Número inválido")
