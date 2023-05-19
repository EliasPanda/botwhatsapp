import pyautogui as bot

bot.press('win') # press() ele pressiona a tecla, nesse caso mandei pressionar a tecla do windows 
bot.sleep(2)
bot.write('opera')# write() é uma função para escrever algo, nesse caso ele escreve na pesquisa do menu inicar
bot.sleep(2)
bot.press('enter')# aqui ele preciona o ENTER
bot.sleep(2) #aqui você da um tempo de pesquisa, nesse caso eu dei 1s
bot.write('https://web.whatsapp.com') #aqui você passará o endereço desejado, no nosso caso é do whats.
bot.sleep(2)
bot.press('enter')
bot.sleep(8)
bot.click(x=205, y=186)
bot.write('Desenvolvimento de garotos de programas')
bot.press('enter')
bot.sleep(2)
bot.write('Henrrique e jon estão com a doença do Passaro, hahaha risada do bot')
bot.sleep(2)
bot.press('enter')
