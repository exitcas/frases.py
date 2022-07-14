# Frases.py
Librería de Python para la API de [Las Frases](https://frases.atico.ga)

## Instalar
### PyPI
- `pip install frases`

### Git
- `git clone https://github.com/Luqaska/frases.py.git`
- `cd frases`
- `pip install .`

## Ejemplo
```python
import frases
print(frases.frase()["frase"])
```

## Funciones
- `frase()`: Frase al azar
- `all()`: Lista de todas las frases disponibles
- `autor(autor)`: Filtrar por autor (Anónimo => False)
- `buscar(consulta: str)`: Buscar frase por su contenido

(C) 2022 [Luqaska](https://atico.ga)