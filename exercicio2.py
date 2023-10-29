# 2) Crie uma classe que representa o caixa de uma empresa, onde os argumentos no instanciamento 
# serão o valor total inicial do caixa e deverão haver métodos de recebimento e pagamento, que 
# recebem argumentos do valor que deve ser recebido ou pago e alterar do valor total. Crie também 
# um método que printe o valor total atual do caixa. Simule após isso o fluxo para um caixa com 
# valor inicial de 5000, que faça 15 vendas de 500 e 4 pagamentos de 1000, após as transações 
# verifique o valor restante em caixa.

class CaixaEmpresa:
    
    def __init__(self, valor_inicial):
        self.valor_total = valor_inicial

    def receber(self, valor):
        self.valor_total += valor

    def pagar(self, valor):
        self.valor_total -= valor

    def verificar_valor_total(self):
        return self.valor_total

caixa = CaixaEmpresa(5000)

for _ in range(15):
    caixa.receber(500)

for _ in range(4):
    caixa.pagar(1000)

valor_restante = caixa.verificar_valor_total()
print(f"Valor restante em caixa: R$ {valor_restante:.2f}")

