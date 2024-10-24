from contacorrente import ContaCorrente, CartaoCredito

# PROGRAMA 

conta_lira = ContaCorrente("Lira","111.222.333-45","1234","34062")
cartao_lira = CartaoCredito("Lira", conta_lira)

print(cartao_lira.__dict__)

cartao_lira.numero = 123
conta_lira.consultar__saldo()
#numero da conta associado ao cartao_lira
print(cartao_lira.conta_corrente._num_conta)
#retorna a lista de cartoes associados a conta corrente conta_lira
print(conta_lira._cartoes)

#acessando o primeiro item da lista 
print(conta_lira._cartoes[0].numero)



conta_maeLira = ContaCorrente("Beth","222.333.444-55","5555","656565")

conta_lira.depositar_dinheiro(11000)
conta_lira.consultar__saldo()

conta_lira.sacar_dinheiro(1000)
conta_lira.consultar__saldo

conta_lira.consultar_historico_transacoes()
conta_lira.transferir(1000, conta_maeLira)

# _saldo via metodos 
print(conta_lira._saldo)
#tentando mudar o valor do _saldo  por fora  do programa 
conta_lira._saldo = 8000
# novo valor apos  tentativa de "burlar" o sistema
print(conta_lira._saldo)

print('_Saldo da conta é',conta_lira._saldo)
print(conta_lira.cpf)



#help(ContaCorrente)