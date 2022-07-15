# Frases.py
Libreria de Python para la API de [Las Frases](https://frases.atico.ga)

## Instalar/Actualizar
### PyPI
`$ pip install frases`

### Git
```
$ git clone https://github.com/Luqaska/frases.py.git
$ cd frases
$ pip install .
```

## Ejemplo
```python
import frases
print(frases.frase()["frase"])
```

## Funciones
En todos los casos, una frase se vendria a ver algo asi: `{'autor': <autor>, 'frase': <frase>}`. Esta puede venir en listas o no.

- `frase()`: Frase al azar
	- Respuesta: Frase
- `all()`: Lista de todas las frases disponibles
	- Respuesta: Lista de frases
- `autor(autor)`: Filtrar por autor (Anonimo => False)
	- Respuesta: Lista de frases
- `buscar(consulta: str)`: Buscar frase por su contenido
	- Respuesta: Lista de frases

~~(C)~~ 2022 [Luqaska](https://atico.ga)