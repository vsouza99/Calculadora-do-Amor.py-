print("Bem vindo a Calculadora do amor!")
nome1 = input("Digite seu nome: ")
nome2 = input("Digite o nome do seu possivel companheiro: ")
combinacao_nomes = nome1 + nome2
combinacao = combinacao_nomes.lower()
 
t= (combinacao.count('t'))
r = (combinacao.count('r'))
u = (combinacao.count('u'))
e = (combinacao.count('e'))
l = (combinacao.count('l'))
o = (combinacao.count('o'))
v = (combinacao.count('v'))

true = str(t + r + u + e)
love = str(t + r + u + e)
true_love = int(true + love)

if (true_love < 10) or (true_love > 90):
  print(f"sua pontuação e ",true_love,"vocês foram feitos um para outro ")
elif true_love >= 40 or true_love <= 50:
  print(f"sua pontuação e ", true_love , "vocês estão bem juntos ")
else:
  print("sua pontuação e ", true_love)
  
  