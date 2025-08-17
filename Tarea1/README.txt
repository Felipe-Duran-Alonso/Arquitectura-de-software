Felipe Duran Alonso 202160599-1
Instrucciones de ejecucion:
    Abrir la terminal en el directorio raiz del proyecto y ejecutar el comando (windows): docker-compose up --build -d
    Ejecutar, para ver cuantos contenedores se encuentran en ejecucion: docker ps 
    En caso de estar los 4 acceder a la siguiente ruta en el navegador de su preferencia (el * se mencionara a continuacion): localhost:8000/*
    Una vez realizadas las llamadas deseadas acceda a Grafana (usando las credenciales admin y admin para usuario y clave respectivamente) en localhost:8002
    Al agregar una fuente de datos, indicar para conectarse al servicio de Loki: http://contLOK:3100
    Una vez agregado, acceder a Drilldown->Logs para acceder a las consultas historicas. Seleccionar el periodo de tiempo que desea ver.

    (A modo de explicacion se agrego un diagrama que explica el flujo de lo planteado, indicando rutas y puertos con las siglas F y C para los valores del equipo Fisico y Contenedor respectivamente)

Acceso a las API(localhost:8000/*):
    SI * = random/{cantidad}/{inicio}/{tope}
        Retorna una {cantidad} de listas con cantidad de elementos entre 3 y 7. Con valores aleatorios entre {inicio} y {tope}.
        El retorno de cada lista se da en formato JSON, con clave de tipo ARR-n, siendo n el numero de lista.
    SI * = fibonacci/{cantidad}
        Retorna todos los valores de Fibonacci desde 1 hasta {cantidad}.
        Esa serie de valores las retorna en formato JSON. Siendo la clave de forma F_n, con n el numero evaluado en fibonacci.


    Casos ilustrados en el video:
        http://localhost:8000/random/7/-10/10
        http://localhost:8000/random/5/-1/5
        http://localhost:8000/fibonacci/5
        http://localhost:8000/fibonacci/-1
        http://localhost:8000/fibonacci/0
