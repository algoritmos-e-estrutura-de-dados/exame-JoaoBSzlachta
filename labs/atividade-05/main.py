def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_do_joao):
  cont = 0
  tem = False
  qtd = 0

  if (len(figurinhas_da_maria) >= len(figurinhas_do_joao)):
    qtdJoao = sorted(set(figurinhas_do_joao))

    while figurinhas_da_maria != figurinhas_do_joao:
      qtd = len(figurinhas_do_joao)
      break

    for i in range(len(qtdJoao)):
      for j in range(len(figurinhas_da_maria)):
        if (qtdJoao[i] == figurinhas_da_maria[j]):
          cont = cont + 1
          qtd = len(qtdJoao) - cont

  elif (len(figurinhas_da_maria) <= len(figurinhas_do_joao)):
    qtdMaria = sorted(set(figurinhas_da_maria))

    while figurinhas_da_maria != figurinhas_do_joao:
      qtd = len(figurinhas_da_maria)
      break

    for i in range(len(qtdMaria)):
      for j in range(len(figurinhas_do_joao)):
        if (qtdMaria[i] == figurinhas_do_joao[j]):
          cont = cont + 1
          qtd = len(qtdMaria) - cont

  else:
    for i in range(0, len(figurinhas_da_maria)):
      for j in range(0, len(figurinhas_do_joao) - 1):
        if (figurinhas_da_maria[i] == figurinhas_do_joao[j]):
          tem = True

    if (tem == False):
      cont = cont + 1

  return qtd


if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao)
