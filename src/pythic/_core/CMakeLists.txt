add_library(_pythic SHARED 
            pythic.c)

set_target_properties(_pythic PROPERTIES PREFIX "")
target_include_directories(_pythic PUBLIC .)
target_include_directories(_pythic PUBLIC ${PY_INCLUDE_DIR})
set_property(TARGET _pythic APPEND PROPERTY ARCHIVE_OUTPUT_DIRECTORY ../core)
set_property(TARGET _pythic APPEND PROPERTY LIBRARY_OUTPUT_DIRECTORY ../core)
set_property(TARGET _pythic APPEND PROPERTY RUNTIME_OUTPUT_DIRECTORY ../core)

configure_file(pythicConfig.h.in pythicConfig.h)