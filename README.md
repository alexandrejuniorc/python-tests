# Python Tests

Este é um projeto de estudos sobre **testes em Python**, demonstrando diferentes técnicas de teste incluindo unit tests, doctests, mocking e assertions.

## 📁 Estrutura do Projeto

```
python-tests/
├── src/                        # Código fonte
│   ├── calculadora.py          # Funções matemáticas com doctests
│   ├── pessoa.py               # Classe com integração HTTP
│   └── baconcomovos.py         # Lógica de múltiplos (FizzBuzz-like)
├── tests/                      # Testes unitários
│   ├── test_calculadora.py     # Testes para calculadora
│   ├── test_pessoa.py          # Testes para pessoa (com mocking)
│   ├── test_baconcomovos.py    # Testes para bacon com ovos
│   └── __init__.py
├── main.py                     # Exemplo de uso
└── README.md
```

## 🚀 Funcionalidades

### 📊 Calculadora (`src/calculadora.py`)
- **Soma**: Adiciona dois números
- **Subtração**: Subtrai dois números
- Validação de tipos com `assert`
- **Doctests** integrados para documentação e teste

### 👤 Pessoa (`src/pessoa.py`)
- Classe para representar uma pessoa
- Integração com API externa (JSONPlaceholder)
- Método para obter dados via HTTP requests

### 🥓 Bacon com Ovos (`src/baconcomovos.py`)
Implementação do problema clássico FizzBuzz:
- **Múltiplo de 3 e 5**: "Bacon com ovos"
- **Múltiplo de 3**: "Bacon" 
- **Múltiplo de 5**: "Ovos"
- **Outros**: "Passar fome"

## 🧪 Tipos de Teste Demonstrados

### 1. **Unit Tests** (pytest/unittest)
```python
def test_soma_5_e_5_deve_retornar_10(self):
    self.assertEqual(soma(5, 5), 10)
```

### 2. **Doctests**
```python
def soma(x, y):
    """ Soma x e y
    >>> soma(10, 20)
    30
    >>> soma(-10, 20)
    10
    """
```

### 3. **Mocking** (para APIs externas)
```python
with patch("requests.get") as fake_request:
    fake_request.return_value.ok = True
```

### 4. **Subtestes** (múltiplos casos)
```python
def test_soma_varias_entradas(self):
    x_y_saidas = ((10, 10, 20), (5, 5, 10))
    for x_y_saida in x_y_saidas:
        with self.subTest(x_y_saida):
            # teste aqui
```

## 🛠️ Pré-requisitos

- Python 3.7+
- `requests` library

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/alexandrejuniorc/python-tests.git
cd python-tests
```
2. Crie o ambiente virtual:
```bash
python3 -m venv .venv
```

3. Instale as dependências:
```bash
pip install requests
```

## ▶️ Como Executar

### Executar todos os testes
```bash
# Usando unittest
python3 -m unittest -v

# Ou executar arquivo específico
python -m unittest tests/test_calculadora.py -v
```

### Executar doctests
```bash
# Executar doctests da calculadora
python src/calculadora.py
```

### Executar o exemplo principal
```bash
python main.py
```

## 📋 Exemplos de Uso

### Calculadora
```python
from src.calculadora import soma, subtrai

# Uso normal
print(soma(10, 5))      # 15
print(subtrai(10, 5))   # 5

# Tratamento de erro
try:
    soma('10', 5)
except AssertionError as e:
    print(f"Erro: {e}")  # Erro: x precisa ser int ou float
```

### Pessoa
```python
from src.pessoa import Pessoa

pessoa = Pessoa("João", "Silva")
resultado = pessoa.obter_todos_os_dados()
print(resultado)  # "CONECTADO" se API responder OK
```

### Bacon com Ovos
```python
from src.baconcomovos import bacon_com_ovos

print(bacon_com_ovos(15))  # "Bacon com ovos" (múltiplo de 3 e 5)
print(bacon_com_ovos(9))   # "Bacon" (múltiplo de 3)
print(bacon_com_ovos(10))  # "Ovos" (múltiplo de 5)
print(bacon_com_ovos(7))   # "Passar fome"
```

## 📚 Conceitos Aprendidos

- **Assertions**: Validação de condições com mensagens de erro claras
- **Unit Testing**: Testes isolados de unidades de código
- **Doctests**: Documentação executável dentro do código
- **Mocking**: Simulação de dependências externas (APIs, banco de dados)
- **Subtestes**: Execução de múltiplos casos em um mesmo teste
- **Test Discovery**: Descoberta automática de testes
- **Tratamento de Exceções**: Como capturar e tratar erros em testes

## 🤝 Contribuição

Este é um projeto de estudos. Sinta-se livre para:
- Adicionar novos tipos de teste
- Melhorar a cobertura de testes
- Implementar novas funcionalidades
- Corrigir bugs

## 📄 Licença

Este projeto é livre para uso educacional e de estudos.

---

**Autor**: Alexandre Junior  
**Objetivo**: Aprender e demonstrar diferentes técnicas de teste em Python
