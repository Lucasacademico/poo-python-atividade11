# Desafio: Classe Abstrata Pagamento em Python

## Descrição do Desafio

1. **Defina uma classe abstrata `Pagamento`**:
    - Inclui um método abstrato `processar_pagamento()` que deve ser implementado por todas as subclasses.
    - Inclui um método concreto `detalhes_pagamento()` que imprime "Processando pagamento via [Método]".

2. **Crie subclasses `PagamentoCartao` e `PagamentoBoleto`** que herdam de `Pagamento`:
    - Cada subclasse deve implementar o método `processar_pagamento()`.
        - Para `PagamentoCartao`, `processar_pagamento()` deve imprimir "Pagamento processado com cartão."
        - Para `PagamentoBoleto`, `processar_pagamento()` deve imprimir "Pagamento processado com boleto."

3. **Crie uma função `testar_pagamentos()`** que:
    - Cria instâncias de `PagamentoCartao` e `PagamentoBoleto`.
    - Chama os métodos `processar_pagamento()` e `detalhes_pagamento()` para cada instância.
