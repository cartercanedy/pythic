from typing import (
    Callable,
    Sequence,
    List
)

from typing import TypeVar
_TIn = TypeVar( "_TIn" )
_TOut = TypeVar( "_TOut" )

def select( frm : Sequence[ _TIn ] , how : Callable[ [ _TIn ] , _TOut ] ) -> List[ _TOut ]: ...
