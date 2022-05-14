# Appoo (una app sobre la caca)



## Integrantes

- Francisco Astete

- Ricardo Castillo

- Javier Espinoza

- Patricio Garrido

- María-Fernanda Villalobos


## Grupos de Permisos Creados


- editor: _todo, excepto admin y auth_.

- content_creator: _permisos para escribir contenido en las páginas_.

- visit: _solo permisos para ver_.

## Instrucciones para levantar el proyecto

- En el archivo **requirements.txt** estan las librerias necesarias para levantar el proyecto

- El entorno virtual usado es **Pipenv**

- Las contraseñas de prueba para cada usuario estan **README-keys.txt**.


---
# MÓDULO 7

## ABPro1

- Generación de nuevo modelos en Django para registrarse.

- Migración de los modelos a tablas

- Incorpore una plantilla en la cual se muestran todos los usuarios registrados en una tabla.

- Implemente de datos con MaterilizeCSS e integración de elementos estéticos utilizando CSS

## ABPro2

- Se conectó el modelo a MySql. (Se adjunta un archivo llamado `appoo-main-mysql.zip` en directorio `extras`)

- Incorporación de sistema de comentarios


## ABPro3
- El proyecto ya se encuentra vinculado a diferentes tablas de información

- Funfact, Scale, Tip, Post, Link, Photo, Suscriptor.

- Los modelos Tip y Link poseen un siste ma de sub categorias para elegien en el admin 


## ABPro5

- Comprobar que las modificaciones se reflejan en nuestro servidor respectivo. En visual studio code `en carpeta migrations`:

<img src="./extras/img/abpro5-01a.png" alt="" style="width:300px" /><br/>

- Comprobar en consola: `python manage.py showmigrations`

<img src="./extras/img/abpro5-01b.png" alt="" style="width:300px" /><br/>


- Revertir a migración anterior `python manage.py migrate NOMBRE_DE_APP ID_MIGRACION`
    
<img src="./extras/img/abpro5-02.png" alt="" style="width:300px" /><br/>

- Avanzar hasta restaurar la migración actual `python manage.py migrate NOMBRE_DE_APP ID_MIGRACION`

<img src="./extras/img/abpro5-03.png" alt="" style="width:300px" /><br/>


- Información sobre formas de volver directamente a la primera migración.



---

## Mapa del Proyecto

<kbd> 
<img src="./extras/img/Frame-1.png" alt="" style="width:80%;" />
</kbd>

<kbd>
<img src="./extras/img/Frame-2.png" alt="" style="width:80%;" />
</kbd>


<kbd>
<img src="./extras/img/Frame-3.png" alt="" style="width:80%;" />
</kbd>


<kbd>
<img src="./extras/img/Frame-4.png" alt="" style="width:80%;" />
</kbd>


<kbd>
<img src="./extras/img/Frame-5.png" alt="" style="width:80%;" />
</kbd>


<kbd>
<img src="./extras/img/Frame-6.png" alt="" style="width:80%;" />
</kbd>


<kbd>
<img src="./extras/img/Frame-7.png" alt="" style="width:80%;" />
</kbd>

