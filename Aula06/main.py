from Conta import Conta

# c = Conta()
# print( "Saldo: " , c.getSaldo() )
# c.setSaldo(100)
# print( "Saldo: " , c.getSaldo() )

c = Conta()
print( "Saldo: " , c.saldo )
c.saldo = 100
print( "Saldo: " , c.saldo )

c.sacar( 100 )
c.sacar( 98 )
c.depositar( 1.5 )
c.depositar( 2 )
print( f'Saldo:   {c.saldo:.2f}' )
