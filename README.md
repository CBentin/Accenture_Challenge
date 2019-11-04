# Easy Access
## Writeup - Christian, Lourdes, David y Carlos

 El objetivo de este proyecto es implementar un sistema de acceso a un estacionamiento por medio de detección de placas. El sistema está pensado para un estacionamiento privado de una torre de oficinas. Al hacer el reconocimiento de placas, se da el acceso a empleados o a visitantes previamente registrados en una base de datos temporal. De esta manera se elimina el uso de tarjetas físicas para el acceso de empleados y se agiliza el proceso de registro de visitantes.

![example]

---

## El Proyecto

Los objetivos de la aplicación son:

* Detectar cuando un automóvil se aproxima y obtener la matrícula de la placa.
* Buscar tanto en la base de datos de empleados como de visitantes el registro de la placa.
* Permitir el acceso si la placa está registrada.

Esto se hace de la siguiente manera:

![diagrama]


---

## Método de reconocimiento

La aplicación realiza el reconocimiento de placas por medio de AWS Rekognition. Esta aplicación recibe un input gráfico del cual extrae un string que contiene el número de placa detectada. 

---

## Back-end

El back-end se divide en dos partes: procesado y aplicación web. En la parte del procesado se tiene un script de python que toma un video y analiza el video frame por frame. Una vez que se analiza una imagen se manda a un servidor de AWS S3 donde se guarda la imagen con un string que contiene la lectura de la placa. Cambiando a la aplicación Web, el back-end es una API, escrita en Javascript que crea una CRUD con un solo metodo de "GET". Este metodo obtiene el string y la imagen y las manda al script que corre la aplicación web. Este script valida la placa si es de visitante o de un residente. En este caso la base de datos es local al script y no existen metodos CRUd para accesar a ella, esto se debe a la falta de tiempo.
---

## Front-end

Lenguajes y herramientas:

- HTML
- CSS
- Javascript
- Python
- Uso del tema [Journal] de bootswatch para el diseño de la interfaz
---

## Resultados

Se diseñó un demo de la aplicación que permite el acceso de placas reconocidas, desplegando un mensaje de bienvenida.

---

## Discusión

La aplicación tiene la capacidad de reducir costos para las empresas con control de acceso a los estacionamientos. Una de las principales ventajas de nuestra aplicación es su aplicación para visitantes, la cual con tan solo actualizar una base de datos se puede agilizar la forma de accesar las instalaciones.

El siguiente objetivo será construir una apliación con la cual se pueda dar de alta rápidamente a visitantes para que la persona anfitriona pueda permitir el acceso desde cualquier lado y en cualquier momento. 



[example]: fotos/numberplate.jpg
[diagrama]: fotos/flowchart.jpeg
[Journal]: https://bootswatch.com/journal/