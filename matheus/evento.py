class Evento:

    eventos=[]
    def __init__(self,nomeEvento,localEvento,datEvento,capacidadeEvento):
        self.nomeEvento=nomeEvento
        self.localEvento=localEvento
        self.datEvento=datEvento
        self.capacidadeEvento= capacidadeEvento
        self.inscritosEvento=[]
        
        Evento.eventos.append(self.nomeEvento)
        
        

    @classmethod
    def getEventos(cls):
        return cls.eventos
    
    def _mostraInfo(self):
        return f"O evento será um {self.nomeEvento} e o local sera {self.localEvento} a data sera {self.datEvento} e podera entra no max {self.capacidadeEvento} pessoas"
    
    def _cancelarEvento(self):
        Evento.eventos.remove(self.nomeEvento)
        return f"O evento {self.nomeEvento} foi cancelado"
    
    def incluirInscrito(self,*pessoas):
        
        if len(pessoas) > self.capacidadeEvento:
            print("Numero de inscritos maior doq a capacidade")
        
        else:
            for pessoa in pessoas:
                self.inscritosEvento.append(pessoa)
            return self.inscritosEvento
    
    def getInscritos(self):
        return self.inscritosEvento




if __name__=="__main__":
    festa=Evento("niver","rua","dia","15")
    festa1=Evento("pagode","lugar","mes","30")
    festa2=Evento("show","espaço","ano",3)
    festa1.cancelarEvento()
    print(festa2.incluirInscrito("Matheus","Joao","Pedro"))
    print(Evento.getEventos())





        