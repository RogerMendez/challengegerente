# TuGerente Challenge

# Proyecto Backend
## Instalación de requerimientos
```
pip install -r requirements.txt
```

### Migraciones
```
python manage.py migrate
```
# Proyecto Frontend

## Instalación de requerimientos
#### Dentro de la carpeta frontend 
```
npm install
```

### Compilacion y minificación para producción 
```
npm run build
```

### Ejecutar Proyecto
```
    python manage.py runserver
```
### Ingreso con Frontend integrado
```
    http://127.0.0.1:8000/
```

# EndPoint Proyecto Backend
## Model Rooms

|  HTTP   |      CRUD       |            URL            |
|:-------:|:---------------:|:-------------------------:|
| POST |     Create      |      /api/v1.0/room/      |
| GET |      Read       |      /api/v1.0/room/      |
| GET |         Detail          |    /api/v1.0/room/:id     |
| GET | Read free rooms | /api/v1.0/room/freerooms/ |
| PUT |     Update      |    /api/v1.0/room/:id     |
| DELETE |     Delete      |    /api/v1.0/room/:id     |

## Model Reservation

|  HTTP   |    CRUD    |            URL            |
|:-------:|:----------:|:-------------------------:|
| POST |   Create   |  /api/v1.0/reservation/   |
| GET |    Read    |  /api/v1.0/reservation/   |
| GET |   Detail   | /api/v1.0/reservation/:id |
| PUT |   Update   | /api/v1.0/reservation/:id |
| DELETE |   Delete   | /api/v1.0/reservation/:id |

## Model DetailReservation

|  HTTP   |          CRUD           |                        URL                         |
|:-------:|:-----------------------:|:--------------------------------------------------:|
| POST |         Create          |           /api/v1.0/detail-reservation/            |
| GET |          Read           |           /api/v1.0/detail-reservation/            |
| GET |         Detail          |          /api/v1.0/detail-reservation/:id          |
| GET | Read Detail reservation | /api/v1.0/detail-reservation/rooms/:reservation_id |
| PUT |         Update          |          /api/v1.0/detail-reservation/:id          |
| DELETE |         Delete          |          /api/v1.0/detail-reservation/:id          |

## Model Invoice

|  HTTP   |           CRUD           |                      URL                      |
|:-------:|:------------------------:|:---------------------------------------------:|
| POST |          Create          |              /api/v1.0/invoice/               |
| GET |           Read           |              /api/v1.0/invoice/               |
| GET |         Detail           |             /api/v1.0/invoice/:id          |
| GET | Read invoice reservation | /api/v1.0/invoice/reservation/:reservation_id |
| PUT |          Update          |             /api/v1.0/invoice/:id             |
| DELETE |          Delete          |             /api/v1.0/invoice/:id             |



## Flujo de EndPoinds para reservación

|  HTTP   |          CRUD           |                        URL                         |                                                  Descripción                                                   |
|:-------:|:-----------------------:|:--------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| POST |         Create          |               /api/v1.0/reservation/               |                                              Crear la reservación                                              |
| GET | Read free rooms | /api/v1.0/room/freerooms/ |                                          Lista de habitaciones libres                                          |
| POST |         Create          |           /api/v1.0/detail-reservation/            | Registro de la habitacion con los datos de habitación<br/>Se repite la seleccion de habitacion si es necesaria |
| GET | Read Detail reservation | /api/v1.0/detail-reservation/rooms/:reservation_id |                               Listado de Habitaciones asignadas a la reservación                               |
| POST |          Create          |              /api/v1.0/invoice/               |                     Registro de los datos de la factura en base a los datos de la reserva                      |
| GET |   Detail   | /api/v1.0/reservation/:id |                                               Detalle de reserva                                               |
| GET | Read Detail reservation | /api/v1.0/detail-reservation/rooms/:reservation_id |                               Listado de Habitaciones asignadas a la reservación                               |
| GET | Read invoice reservation | /api/v1.0/invoice/reservation/:reservation_id |                                             Detalle de Facturación                                             |