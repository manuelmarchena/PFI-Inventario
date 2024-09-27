# Proyecto Final Integrador (PFI)

El Proyecto Final Integrador (PFI) consiste en el desarrollo de una aplicación en Python que, utilizando la terminal o consola, permita al usuario gestionar el inventario de una pequeña tienda o comercio.

La aplicación debe ser capaz de registrar, actualizar, eliminar y mostrar productos en el inventario. Además, debe incluir funcionalidades para realizar búsquedas y generar reportes de productos con bajo stock.

## Funcionalidades

Debe contar con un CRUD:

- **CREATE:** Debería poder crear productos de forma que persistan.
- **READ:** Debería poder leer los productos de forma que persistan.
- **UPDATE:** Debería poder actualizar los productos de forma que persistan.
- **DELETE:** Debería poder eliminar los productos de forma que persistan.

## Persistencia de datos

Si voy a trabajar sin base de datos, debería poder guardar los datos en un archivo de texto (`.txt`). Algunas opciones son:

- Un diccionario para las consultas.
- Un archivo .CSV con las columnas correspondientes.

## Estructura del proyecto

Podría manejar los datos en diferentes funciones, evitando el uso de clases para dividir el proyecto.

Si voy a guardar en un archivo de texto, se actualizará según sea necesario.

Adicionalmente tambien crear los elementos necesarios para capturar el input del usuario 

inventario_comercio/
│
├── app/
│   ├── README.md
│   ├── models/
│   │   └── inventory_manager.py  # Lógica de negocio
│   ├── views/
│   │   └── display.py  # Funciones para mostrar al usuario
│   ├── controllers/
│   │   ├── create_product.py
│   │   ├── read_inventory.py
│   │   ├── update_stock.py
│   │   ├── delete_product.py
│   │   └── app.py  # Punto de entrada de la aplicación
│   └── data/
│       ├── file_manager.py  # Funciones para leer y escribir en archivo
│       └── inventario.csv  # Archivo de datos persistente
│
├── validation/
│   ├── input_validation.py  # Validación de entradas del usuario
│   └── validation_manager.py  # Lógica central de validación
└── tests/
    └── test_inventory.py  # Pruebas del inventario
