import timeit
import pythic as pth

def select( frm , how ):
    return [ how( frm[ i ] ) for i in range( len( frm ) ) ]

class CClass:
    def __init__( self ): self.hello = "world"

inp_list = [ CClass() for i in range( 1000 ) ]
how = lambda x: x.hello

glob = globals()

print( f"Pure python implementation: { timeit.timeit( 'select( inp_list , how )' , number = 10000 , globals = glob ) }" )
print( f"C implentation: { timeit.timeit( 'pth.select( inp_list , how )' , number = 10000 , globals = glob ) }" )
