# 🖱️ Automação de Cadastro com PyAutoGUI

Este projeto tem como objetivo automatizar o processo de cadastro de usuários e inserção de produtos em uma interface gráfica utilizando a biblioteca [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/).

## 🚀 Tecnologias Utilizadas

- Python 3.x
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/)
- Arquivo `.txt` para leitura de dados
- Interface gráfica externa (aplicativo de cadastro)

## 📋 Funcionalidades

- Cadastro automático de novo usuário
- Login automatizado
- Leitura de produtos de um arquivo `.txt`
- Preenchimento automático dos dados de produto na interface

## 📄 Formato do Arquivo `produtos.txt`

O arquivo `produtos.txt` deve conter as informações de produtos no seguinte formato, uma linha por produto:


## 🧠 Como Funciona

### 1. Cadastro de Novo Usuário

```python
pyautogui.click(950,593,duration=1)  # Botão 'Cadastrar'
pyautogui.click(979,543,duration=1)
pyautogui.write('willian')
pyautogui.click(971,567,duration=1)
pyautogui.write('123')
pyautogui.click(888,600,duration=1)  # Botão 'Registrar novo usuário'
pyautogui.click(980,543, duration=1)
pyautogui.write('willian')
pyautogui.click(973,564, duration=1)
pyautogui.write('123')
pyautogui.click(871,599, duration=1)  # Botão 'Entrar'
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(707,525, duration=1)
        pyautogui.write(produto)

        pyautogui.click(701,554, duration=1)
        pyautogui.write(quantidade)

        pyautogui.click(704,583, duration=1)
        pyautogui.write(preco)

        pyautogui.click(586,742, duration=1)  # Botão 'Registrar'
        sleep(1)
```
## 📥 Download do sistema

Você pode baixar o projeto pronto no formato `.zip` pelo link abaixo:

🔗 [Clique aqui para baixar](https://drive.google.com/file/d/1dOAp5PgN7rg_KzSXVJQFL85BW6ltPqKi/view)

### 🧾 Instruções para uso

1. Acesse o link acima e clique em **"Fazer download"**.
2. Extraia o conteúdo do arquivo `.zip` em uma pasta de sua preferência.
3. Abra a pasta extraída.
4. **Clique duas vezes no arquivo `app`** para iniciar o sistema de automação.

> **Observação:** Certifique-se de manter a janela do sistema de cadastro visível na tela, pois a automação depende das posições exatas dos cliques.

#

### Referências
🔗 [Clique aqui para entrar](https://www.youtube.com/watch?v=pNBjC32nisg)
