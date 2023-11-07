from typing import (
    Callable,
    Sequence,
    List
)
from sys import version_info

if version_info.major == 3 and version_info.minor >= 12:
    def select[ TIn , TOut ]( frm : Sequence[ TIn ] , how : Callable[ [ TIn ] , TOut ] ) -> List[ TOut ]: ...
else:
    from typing import TypeVar
    _TIn = TypeVar( "_TIn" )
    _TOut = TypeVar( "_TOut" )
    
    def select( frm : Sequence[ _TIn ] , how : Callable[ [ _TIn ] , _TOut ] ) -> List[ _TOut ]: ...