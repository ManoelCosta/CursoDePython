salarioFuncionario = float(input('Informe o salario do funcionario: '))
novoSalarioFuncionario = salarioFuncionario + (salarioFuncionario * (15/100))
print('O salario do funcionarios era de: R${:.2f}'.format(salarioFuncionario))
print('Com aumento de 15%, o novo salario do funcionario será de: {:.2f}'.format(novoSalarioFuncionario))
