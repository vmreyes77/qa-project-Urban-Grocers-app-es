# Proyecto Urban Grocers 

### Víctor Manuel Reyes Vargas, Cohort 9, Sprint 7

Es este proyecto hemos evaluado los límites y los parámetros aceptados en la creación de un nuevo kit.

Específicamente hemos probado el campo "name" y comprobado que todos los requisitos del mismo se cumplan correctamente.

Para realizar las pruebas primero hay que crear un nuevo usuario haciendo una solicitud POST ("api/v1/users/"), este nos arroja un token de
autorización, el cual es necesario para poder crear los kits nuevos.

Luego se procede a crear un nuevo kit asignado al usuario que acabamos de crear, para ello es necesario hacer otra solicitud POST
("api/v1/kits") asegurándonos de poner el parámetro "Authorization" conteniendo el authToken del usuario recién creado.

Ya en este entorno es posible realizar todas las pruebas de lugar.

La fuente utilizada para estas pruebas fue la siguiente:
"https://cnt-99d7a868-1d37-4db6-91f7-bae8c7bdead4.containerhub.tripleten-services.com/docs/#api-Main.Kits-CreateKit"

Las pruebas fueron realizadas utilizando PyCharm de manera local, una vez hecho el trabajo se cargó el código en GitHub
y el respositorio fue enviado a revisión.
