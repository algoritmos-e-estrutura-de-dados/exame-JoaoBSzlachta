def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  cont = 0
  tem = False
  if (len(figurinhas_da_maria) >= len(figurinhas_do_joao)):
    for i in range(len(figurinhas_do_joao)):
      for j in range(len(figurinhas_da_maria)):
        if (figurinhas_do_joao[i] == figurinhas_da_maria[j]):
          tem = True

      if (tem == False):
        cont = cont + 1

  elif (len(figurinhas_da_maria) <= len(figurinhas_do_joao)):
    for i in range(len(figurinhas_da_maria)):
      for j in range(len(figurinhas_do_joao)):
        if (figurinhas_da_maria[i] == figurinhas_do_joao[j]):
          tem = True

      if (tem == False):
        cont = cont + 1

  else:
    for i in range(0, len(figurinhas_da_maria)):
      for j in range(0, len(figurinhas_do_joao) - 1):
        if (figurinhas_da_maria[i] == figurinhas_do_joao[j]):
          tem = True

    if (tem == False):
      cont = cont + 1

  
  return cont



if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
