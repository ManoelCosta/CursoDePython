precoProduto = float(input('Informe o valor do produto: '))
novoPreco = precoProduto - ((5/100) * precoProduto)
print('Preço do Produto: {:.2f}'.format(precoProduto))
print('Preço com desconto de 5%: {:.2f}'.format(novoPreco))
