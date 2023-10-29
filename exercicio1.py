# 1) Crie uma classe Produto, que receba como argumentos no instanciamento o nome e o preço do produto. 
# A classe deve ter um método "desconto" que retornará o preço do produto com um percentual de desconto 
# que é passado como argumento para esse método.

class Produto:
    
    def __init__(self, nome, nomeProduto, preco):
        self.nome = nome
        self.nomeProduto = nomeProduto
        self.preco = preco
        
    def desconto(self, percentual):
        valorDesconto = self.preco * (percentual / 100)
        valorFinal = self.preco - valorDesconto
        print(f"Olá {self.nome}, o produto: {self.nomeProduto} custa R$ {self.preco}. Você recebeu um desconto de {percentual}% sendo o valor final com desconto de R$ {valorFinal:.2f}")

produto = Produto('Grazielle', 'Notebook', 5000)  
produto.desconto(50)
   