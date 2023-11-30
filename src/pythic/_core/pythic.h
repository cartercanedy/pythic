#define PY_EXC PyExc_Exception
#define RAISE_MSG_IF( cond , msg ) if ( (cond) ) { if ( !PyErr_Occurred() ) PyErr_SetString( PY_EXC , (msg) ); return NULL; }
#define RAISE_IF( cond ) RAISE_MSG_IF( ( cond ) , "An internal error occurred" )
