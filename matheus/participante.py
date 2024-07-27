
from matheus.evento import Evento



class Participante(Evento):
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        self.ingressosComprados = []


    def comprarIngresso(self):
        x=0
        for evento in Evento.eventos:
            print(f"{x} -> {evento}")
            x+=1
        num=int(input("Qual evento vc deseja comprar um ingresso: "))
        if num > len(Evento.eventos):
            print("Valor invalido")
        else:
            self.ingressosComprados.append(Evento.eventos[num])
        
        Ingresso.dicionario[self.nome] = Evento.eventos[num]


    def listarIngressosComprados(self):
        return self.ingressosComprados
    
    def getDicionario(cls):
        return Ingresso.dicionario
    

class Ingresso(Evento):
    dicionario={}
    def __init__(self,data,status):
        self.data = data
        self.status = status


    
  



        

        
        


        



