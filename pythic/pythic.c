#include <stdio.h>
#include "pythicConfig.h" 

static PyObject *
pythic_select( PyObject *self , PyObject *args , PyObject *kwargs )
{
  PyObject *frm = NULL, *how = NULL;
  static char *arg_names[] = {
    "frm",
    "how",
    NULL
  };

  RAISE_MSG_IF(!PyArg_ParseTupleAndKeywords( args , kwargs, "OO" , arg_names , &frm , &how) , "Unable to parse arguments" );

  PyObject *lItems = PySequence_Fast( frm , "Argument \"frm\" didn't support iteration");
  RAISE_MSG_IF(!lItems , "Wasn't able to convert arg \"frm\" to a list" );

  Py_ssize_t lItemsLen = PyList_GET_SIZE(lItems);
  PyObject *lOutList = PyList_New(lItemsLen);
  RAISE_IF(!lOutList);

  int i = 0;
  PyObject *lArg = NULL; 
  for (; i < lItemsLen; i++)
  {
    lArg = PyList_GET_ITEM( lItems , i );
    PyObject *lTransformed = PyObject_CallOneArg( how , lArg );

    RAISE_MSG_IF(!lTransformed , "Error in producing the requested transformation" );

    PyList_SET_ITEM( lOutList , i , lTransformed );
  }

  return lOutList;
}

static PyMethodDef pythicMethods[] = {
  {
    "select" ,
    (PyCFunction)pythic_select,
	  METH_VARARGS | METH_KEYWORDS,
	  "Return a sequence that contains the operation specified applied to all constituents of the input sequence"
  },
  { NULL , NULL , 0 , NULL }
};

static struct PyModuleDef pythicmodule = {
  PyModuleDef_HEAD_INIT,
  "pythic",
  "A lightweight data querying library...",
  -1,
  pythicMethods
};

PyMODINIT_FUNC
PyInit_pythic( void )
{
  return PyModule_Create( &pythicmodule );
}
