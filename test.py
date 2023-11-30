import timeit
import pythic as pth

def select( frm , how ):
    return [ how( frm[ i ] ) for i in range( len( frm ) ) ]

class Foo:
    def __init__( self ): self.bar = "Baz"

inp = [ Foo() for i in range( 1000 ) ]
how = lambda x: x.bar

print( f"Pure python implementation: { timeit.timeit( 'select( inp , how )' , number = 10000 , globals = globals() ) }" )
print( f"C implentation: { timeit.timeit( 'pth.select( inp , how )' , number = 10000 , globals = globals() ) }" )
