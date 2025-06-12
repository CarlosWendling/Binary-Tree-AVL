import pandas as pd
from Pessoa import Pessoa

# retorna um dataframe se o csv for lido corretamente
def lerCsv(filePath: str) -> pd.DataFrame | str:
  # trata os erros caso não ache o csv ou o conteúdo esteja incorreto
  try:
    dados = pd.read_csv(filePath, sep=";", header=None)
  except pd.errors.EmptyDataError:
    return "Arquivo vazio"
  except FileNotFoundError:
    return f"Não foi achado o arquivo {filePath}"
  return dados


# recebe cada linha do csv
def criaPessoas(data: list[list]) -> list[Pessoa]:
  pessoas = []
  for dado in data:
    pessoa = Pessoa(
      cpf=str(dado[0]),
      rg=str(dado[1]),
      nome=dado[2],
      data=dado[3],
      cidade=dado[4],
    )

    # adiciona a pessoa na lista caso não tenha sido cadastrada
    if checaPessoa(pessoa, pessoas):
        pessoas.append(pessoa)

  return pessoas


# verifica se tem uma pessoa identica na lista
def checaPessoa(pessoa: Pessoa, pessoasList: list[Pessoa]) -> bool:
  for pes in pessoasList:
    if (
      pes.getNome == pessoa.getNome
      and pessoa.getCidade == pes.getCidade
      and pessoa.getCPF == pes.getCPF
      and pessoa.getData == pes.getData
      and pessoa.getRG == pes.getRG
    ):
      return False
  return True


if __name__ == "__main__":
  pessoas = lerCsv("grauB/exemplo.csv")
  if isinstance(pessoas, pd.DataFrame):
    pessoasList = criaPessoas(pessoas.values)
    for pessoa in pessoasList:
      print(str(pessoa))
  else:
    print(pessoas)
