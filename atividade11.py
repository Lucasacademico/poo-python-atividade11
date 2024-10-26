from abc import ABC, abstractmethod


class Pagamento(ABC):
    @abstractmethod
    def processar_pagamento(self):
        pass 

    def detalhes_pagamento(self, metodo):
        print(f"Processando pagamento via {metodo}")

class PagamentoCartao(Pagamento):
    def processar_pagamento(self):
        print("- O pagamento com cartão foi processado com sucesso!")

class PagamentoBoleto(Pagamento):
    def processar_pagamento(self):
        print("- O pagamento com boleto foi processado com sucesso!") 


def testar_pagamentos():
    pagamento_cartao = PagamentoCartao()  
    pagamento_boleto = PagamentoBoleto()  
    
    pagamento_cartao.detalhes_pagamento("Cartão de crédito")
    pagamento_cartao.processar_pagamento()
    
    pagamento_boleto.detalhes_pagamento("Boleto bancário")
    pagamento_boleto.processar_pagamento()


testar_pagamentos()
