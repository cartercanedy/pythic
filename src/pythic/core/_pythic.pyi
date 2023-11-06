from typing import (
    Callable,
    Sequence,
    List
)

def select( frm : Sequence[ TIn ] , how : Callable[ [ TIn ] , [ TOut ] ] ) -> List[ TOut ]: ...
