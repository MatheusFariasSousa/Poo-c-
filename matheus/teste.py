def teste(*pessoas):
    lista=[]
    for pessoa in pessoas:
        lista.append(pessoa)
    return lista

print(teste("1","2","3"))