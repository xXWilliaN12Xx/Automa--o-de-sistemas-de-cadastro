import pyautogui
from time import sleep

# cadastrar usuário
# 1 - clicar em cadastrar
pyautogui.click(950,593,duration=1)
# 2 - clicar e digitar novo usuario
pyautogui.click(979,543,duration=1)
pyautogui.write('willian')
# 3 - clicar e digitar nova senha
pyautogui.click(971,567,duration=1)
pyautogui.write('123')
# 4 - clicar em registrar novo usuário
pyautogui.click(888,600,duration=1)

# Passos manuais para realizar este processo:
# 1 - Clicar e digitar meu usuário
pyautogui.click(980,543, duration=1)
pyautogui.write('willian')
# 2 - Clicar e digitar minha senha
pyautogui.click(973,564, duration=1)
pyautogui.write('123')
# 3 - Clicar em 'Entrar'
pyautogui.click(871,599, duration=1)
# 4 - Extrair informações
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        linha.split(',')
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        # 	1 - Clicar e digitar produto
        pyautogui.click(707,525, duration=1)
        pyautogui.write(produto)
        # 	2 - Clicar e digitar Quantidade
        pyautogui.click(701,554, duration=1)
        pyautogui.write(quantidade)
        # 	3 - Clicar e digitar preço
        pyautogui.click(704,583, duration=1)
        pyautogui.write(preco)
        # 	4 - Clicar em 'Registrar'
        pyautogui.click(586,742, duration=1)
        sleep(1)
