#Quero um progama que retorne uma mensagem de boas vinda, e resolva conta matematica!
print('Olá, seja bem vindo, ao progama que ajuda suas duvida na matematica!')
msg = str (input('Como você gosta de ser chamado[a] '))
print('E um prazer ter você aqui conosco {}!'.format(msg))
print('Iremos começar sua jornada, o que nos podemso te ajudar? insira o valor da conta que está com dvuida!')
msg2 = int (input('insira os primeiro numeros'))
msg3 = int (input('insira outros numeros'))
soma = msg2 + msg3
nm1 = msg2 / msg3
nm2 = msg2 // msg3
nm3 = msg2 % msg3
nm4 = msg2 ** msg3
print('{}, Seu primeiro resultado [Adição] {} \n  Segundo resultando [Divisão] {} \n Terceiro resultado [Divisão inteira] {} \n Quarto Resultado [resto da divisão] {} \n Quinto Resultado [potencia] {}!'.format(msg ,soma,nm1,nm2,nm3,nm4 ))
print('Obrigado por confia na gente, Até uma proxima!!!')