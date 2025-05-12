Este es un sistema de gestión de inventario sencillo desarrollado en Python como parte de la prueba de desempeño del primer modulo "Fundamentos de programación con Python".

#DESCRIPCIÓN DEL PROYECTO:
	El sistema permite administrar los productos de una tienda en forma dinámica. Se puede agregar, consultar, actualizar precios, eliminar productos y  calcular el valor total del inventario.

#SUS FUNCIONALIDADES PRINCIPALES:
	1.) Añadir Productos Al Inventario:
		El usuario puede agregar productos indicando su nombre, precio y cantidad.
	2.) Consultar Productos:
		Permite buscar un producto por su nombre y muestra sus detalles como (nombre - precio - cantidad).
	3.) Actualizar Precios:
		Permite modificar el precio de un producto. El nuevo precio debe ser un numero positivo.
	4.) Eliminar Productos:
		Permite eliminar un producto del inventario si ya no esta disponible.
	5.) Calcular Valor Total Del Inventario:
		Multiplica el precio de cada producto que hay en inventario y muestra el total acumulado.
	6.) Mostrar Todos Los Productos:
		Muestra los productos que se encuentran en el inventario con su precio y cantidad.
	7.) Colores:
		El código cuenta con colores para resaltar mensajes del código y esos mensajes sean mas llamativos.
	8.) Tiempo:
		Se le agrego al código "import time" para que en el momento de que el programa muestre algo haya un tiempo corto de espera y no lance toda la información al usuario de una.

#REQUISITOS:
	- Se agregan al menos 5 productos iniciales automáticamente.
	- Si se consulta por un producto inexistente, se muestra un mensaje claro.
	- Al actualizar un precio, se valida que el usuario halla ingresado un numero positivo.
	- Al eliminar un producto de valida su existencia en inventario.
	- El calculo del valor total del inventario se muestra exactamente con dos decimales
	- La mayor parte del código esta estructurado en funciones y comentado en ingles.
	- El código unicamente esta copiado en español en las partes que el usuario ve o interactúa con ellas. 

#INSTRUCCIONES PARA EJECUTAR EL PROGRAMA:
	- Asegúrate de tener Python (Versión 3.6 o superior) instalado en tu pc, o un editor de código (VS Code)
	- Descarga el archivo "prueba de desempeño.py".
	- Abre una terminal o editor de código.
	- Ejecuta el programa.
	
EJEMPLOS:
Agregar un producto:
	----------Añadir Productos----------
	Ingresa el nombre del producto: silla
	Ingresa el precio del producto: 457.350
	Ingresa la cantidad: 22
	El producto se agrego correctamente.
	
Consultar productos existente:
	----------Consultar Productos----------
	Ingresa un producto para buscar: silla
	producto: silla
	Precio: $ 457.350
	Cantidad: 22

Consultar productos inexistentes:
	----------Consultar Productos----------
	Ingresa un producto para buscar: mesa
	Producto no encontrado en el inventario.

Actualizar precios:
	----------Actualizar Precios----------
	Ingrese nombre del producto: silla
	Ingresa el nuevo precio: 415.350
	El precio se ha cambiado exitosamente.
	
Eliminar productos:
	----------Eliminar Productos----------
	Ingrese el nombre del producto: silla
	Producto eliminado correctamente.
	
Calcular valor total del inventario:
	----------Calcular Valor Total----------
	El valor total del inventario es: 4405.00
	
Mostrar todos los productos:
	----------Inventario Completo----------
	- Laptop: $120.000 | Cantidad: 5
	- Mouse: $25.500 | Cantidad: 20
	- keyboard: $45.000 | Cantidad: 10
	- Monitor: $300.000 | Cantidad: 8
	- Cable USB: $8.900 | Cantidad: 50
	
Salir del programa:
	Saliendo del programa
  	   ¡Hasta Pronto!

