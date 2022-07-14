from requests import get
endpoint = "https://frases.atico.ga/"



def frase():
  return get(f"{endpoint}.json").json()


def all():
  frases = get(f"{endpoint}all.json").json()
  return frases["lista"]


def autor(autor):
  frases = get(f"{endpoint}all.json").json()["lista"]
  lista = []
  for x in frases:
    if autor == x["autor"]:
      lista.append(x)
  return lista


def buscar(consulta: str):
  frases = get(f"{endpoint}all.json").json()["lista"]
  lista = []
  for x in frases:
    consulta = consulta.split(" ")
    consulta = "".join(consulta)
    consulta = consulta.lower()
    frase = x["frase"].split(" ")
    frase = "".join(frase)
    frase = frase.lower()
    if consulta in frase:
      print(consulta)
      print(frase)
      lista.append(x)
  return lista