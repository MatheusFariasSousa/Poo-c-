
from matheus.evento import Evento
import matheus.participante as participante







if __name__=="__main__":
    festa0=Evento("niver","rua","dia",8)
    festa1=Evento("pagode","lugar","mes",15)
    festa2=Evento("show","espaço","ano",3)
    pessoa0 = participante.Participante("Matheus","matheuspelo123@gmail.com")
    pessoa1=participante.Participante("Joao","joao@1123.com")
    pessoa0.comprarIngresso()
    pessoa1.comprarIngresso()

    
    print(pessoa1.listarIngressosComprados())
    print(pessoa0.listarIngressosComprados())
    print(pessoa0.getDicionario())

