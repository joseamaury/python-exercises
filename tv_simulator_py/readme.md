# Exercício: Classe TV

Este exercício é uma prática de **Programação Orientada a Objetos (OOP)** em Python.  
O objetivo é criar uma classe que simula o funcionamento de uma televisão, permitindo:

- Ligar e desligar a TV
- Mudar de canal para cima ou para baixo
- Acompanhar o canal atual

---

## Código

O código está no arquivo `tv.py`.

### Exemplo de uso:

```python
from tv import TV

# Cria uma TV
television = TV()

# Verifica se a TV está ligada
print(television.on)  # False

# Liga a TV
television.power()
print(television.on)  # True

# Muda de canal
television.change_channel_up()
print(television.channel)  # 6
```
___

## Detalhes da implementação

A TV começa desligada (on = False) e no canal 5.

### Métodos disponíveis:

```
power(): liga ou desliga a TV.

change_channel_up(): aumenta o canal (somente se a TV estiver ligada).

change_channel_down(): diminui o canal (somente se a TV estiver ligada).
```

A implementação garante que os canais só mudam quando a TV está ligada.

___

## Autor

**José Amaury**

[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/joseamaury)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/joseamaury)
[![Gmail](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:amaury345.ja@gmail.com)
