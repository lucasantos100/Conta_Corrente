from datetime import datetime
import pytz
from random import randint

class ContaCorrente:

    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome (str) : Nome do cliente
        cpg (str) : CPF do cliente. deve ser inserido com pontos e traços (xxx.xxx.xxx-xx)
        agencia (str) : numero da agencia
        _num_conta (str) : numero da conta corrente do cliente
        saldo : saldo disponivel pelo cliente
        limite : limite de cheque especial daquele cliente
        transacoes : historico de transacoes do cliente
    """

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('America/Sao_Paulo')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('[%d/%m/%Y %H:%M:%S]')

    def __init__(self, nome, cpf, agencia, _num_conta):
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0
        self.limite = None
        self.agencia = agencia
        self._num_conta = _num_conta
        self.transacoes = []
        self._cartoes = []
 
    def consultar__saldo(self):
        print('Seu _saldo atual é de R${:,.2f}'.format(self._saldo))
        pass
    
    def depositar_dinheiro(self,valor):
        self._saldo += valor 
        self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def limite_conta(self):
            self.limite = -1000
            return self.limite

    def sacar_dinheiro(self,valor):
        if self._saldo -valor < self.limite_conta():
            print('Você nao tem _saldo suficiente para sacar esse valor')
            self.consultar__saldo()
        else:
            self._saldo -= valor
            self.transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))
        pass

    def consultar_historico_transacoes(self):
        print('Histórico de Transações:')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self.transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino.transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))

class CartaoCredito:
    
    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR

    def __init__(self, titular, conta_corrente):
        self.numero = randint (1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}'.format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 4)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 1000
        self.conta_corrente = conta_corrente
        conta_corrente._cartoes.append(self)