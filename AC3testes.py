import abc 
from unittest import TestCase, main  

class Operacao(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def executar(self, num1, num2):
        pass

class Divisao(Operacao):
    def executar(self, num1, num2):
        conta=num1/num2
        return conta

class Soma(Operacao):
    def executar(self, num1, num2):
        conta=num1+num2
        return conta

class Subtracao(Operacao):
    def executar(self, num1, num2):
        conta=num1-num2
        return conta

class Multiplicacao(Operacao):
    def executar(self, num1, num2):
        conta=num1*num2
        return conta

class OperacaoFabrica(object):
    def criar(self, operador):
        if(operador=='soma'):
            return Soma()
        elif(operador=='divisao'):
            return Divisao()
        elif(operador=='subtracao'):
            return Subtracao()
        elif(operador=='multiplicacao'):
            return Multiplicacao()

class Calculadora():
    def calcular(self, num1, num2, operador):
        operacaoFabrica=OperacaoFabrica()
        operacao = operacaoFabrica.criar(operador)
        if(operacao ==None):
            return 0
        else:
            resultado = operacao.executar(num1, num2)
            return resultado

class MeusTestes(TestCase):
    def teste_divisao(self):
        testarD = Calculadora()
        resultado = testarD.calcular(20,4, 'divisao')
        self.assertEqual(resultado, 5)

    def teste_soma(self):
        testarS = Calculadora()
        resultado = testarS.calcular(1,99,'soma')
        self.assertEqual(resultado, 100)

    def teste_subtracao(self):
        testarMenos = Calculadora()
        resultado = testarMenos.calcular(500,499,'subtracao')
        self.assertEqual(resultado, 1)
    
    def teste_multiplicacao(self):
        testarM = Calculadora()
        resultado = testarM.calcular(8,10,'multiplicacao')
        self.assertEqual(resultado, 80)
    
    def teste_divisao(self):
        testarD = Calculadora()
        resultado = testarD.calcular(20,4, 'truncada')
        self.assertEqual(resultado, 0)

calculador = Calculadora()
usar = calculador.calcular(8,10, 'multiplicacao')
print (usar)

if __name__ == '__main__':
    main()