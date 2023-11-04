import timeit
from pythic import pythic as pth

def select( frm , how ):
    return [ how( frm[ i ] ) for i in range( len( frm ) ) ]

class CClass:
    def __init__( self ): self.hello = "world"

inp_list = [ CClass() for i in range( 1000 ) ]
how = lambda x: x.hello

glob = globals()

print( timeit.timeit( "select( inp_list , how )" , number = 100000 , globals = glob ) )
print( timeit.timeit( "pth.select( inp_list , how )" , number = 100000 , globals = glob ) )
