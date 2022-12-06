# Práctica Modelado de Datos
Vamos a crear un gestor de empleados para llevar el control de:
* Datos de empleados
* Puestos de trabajo y salarios asociados
* Localizaciones de cada fábrica 

  COUNTRY <-|----||-> LOCATION <-|------||-> FACTORY <-||-----|-> EMPLOYEE <-||----|-> JOB <-|-----||-> SALARY
 

EMPLOYEE
id
dni: charfield
first_name: charfield
last_name: charfield
email: emailfield
address: charfield
job_id
factory_id


JOB
id
title: charfield
description: textfield
salary_id

SALARY
id
amount: integerfield
extra_dec: booleanfield
extra_jun: booleanfield

FACTORY
id
name: charfield
address: charfield
zip_code: charfield
location_id

LOCATION
id
name: charfield
country_id

COUNTRY
id
name: charfield
country_code: charfield

## Desarrollo
1. Creamos una aplicación "company"
2. La agregamos a las aplicaciones instaladas en settings.py. Comprobamos que se ha instalado correctamente
3. Conectamos con PostgreSQL
4. Migramos los datos
5. En la aplicación company, modelamos los datos
6. Establecemos las relaciones. Tendremos que reordenar las clases (en algunos casos) para que las clases con las que relacionemos la clase actual ya esté definida (esté más arriba).
7. Por último, migramos los cambios a PostgreSQL


           