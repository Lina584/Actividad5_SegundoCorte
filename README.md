# Brazo Robótico Controlado con ESP32 y PyBullet

##  Descripción

Este proyecto consiste en el desarrollo de un sistema de control para un brazo robótico utilizando un **ESP32**, seis botones físicos y una simulación realizada en **PyBullet**.

El sistema permite controlar diferentes movimientos del brazo robótico mediante botones conectados físicamente al ESP32. Las señales generadas por los botones son enviadas desde el ESP32 al computador mediante comunicación serial.

En el computador, un programa desarrollado en **Python** recibe estas señales, las interpreta y controla las articulaciones correspondientes del brazo robótico dentro de la simulación de PyBullet.

El proyecto integra conceptos de **microcontroladores, comunicación serial, programación en Python, simulación robótica y modelado de robots mediante URDF**.

---

# Objetivos

## Objetivo general

Desarrollar un sistema de control para un brazo robótico simulado en PyBullet mediante seis botones físicos conectados a un ESP32.

## Objetivos específicos

- Configurar un ESP32 para detectar seis botones físicos.
- Utilizar entradas digitales del ESP32 para recibir las señales de los botones.
- Implementar `INPUT_PULLUP` para simplificar la conexión de los botones.
- Establecer comunicación serial entre el ESP32 y el computador.
- Desarrollar un programa en Python para recibir las instrucciones del ESP32.
- Cargar el modelo del brazo robótico mediante un archivo URDF.
- Controlar las articulaciones del robot utilizando PyBullet.
- Controlar el movimiento de la base y del brazo.
- Controlar la apertura y cierre de la pinza.
- Integrar el sistema físico con la simulación robótica.

---

#  Tecnologías utilizadas

- **ESP32**
- **Arduino IDE**
- **Python 3.12**
- **PyBullet**
- **PySerial**
- **URDF**
- **Visual Studio Code**
- **Git**
- **GitHub**

---

#  Componentes utilizados

- 1 × ESP32
- 6 × botones pulsadores de 4 patas
- 1 × protoboard
- Cables Dupont
- 1 × cable USB
- 1 × computador

---

#  Conexiones del ESP32

Se utilizaron seis botones físicos para controlar las diferentes funciones del brazo robótico.

| Botón | GPIO | Función |
|---|---:|---|
| 🔘 Botón 1 | GPIO18 | Girar base a la izquierda |
| 🔘 Botón 2 | GPIO19 | Girar base a la derecha |
| 🔘 Botón 3 | GPIO21 | Subir brazo |
| 🔘 Botón 4 | GPIO22 | Bajar brazo |
| 🔘 Botón 5 | GPIO23 | Abrir pinza |
| 🔘 Botón 6 | GPIO25 | Cerrar pinza |

Cada botón se conecta entre un GPIO del ESP32 y GND.

La conexión general de cada botón es:

```text
GPIO ESP32 ─────── BOTÓN ─────── GND
```
El modelo utilizado contiene las siguientes articulaciones principales:
| Indice | Articulación | Función |
|---|---:|---|
| 0 | joint_1 | Giro de la base|
| 1 | joint_2 | Movimiento del brazo|
| 2 | joint_gripper | Movimiento vertical de la pinza|
| 3 | joint_dedo_izq| Movimiento del dedo izquierdo |
| 4 | joint_dedo_der| Movimiento del dedo derecho |

Durante las pruebas se comprobó que ```joint_gripper``` genera un movimiento vertical de la pinza

Por esta razón, para conseguir la apertura y cierre de la pinza se utilizan directamente: 

```joint_dedo_izq```
```joint_dedo_der``` 

Los dos dedos se controlan simultáneamente para conseguir el movimiento de apertura y cierre.

# Programa de Python
El archivo ```control_brazo.py``` es el programa principal encargado de conectar el ESP32 con PyBullet.

Sus funciones principales son:

- Abrir la comunicación serial con el ESP32.
- Conectarse a PyBullet.
- Cargar el modelo del brazo robótico.
- Leer los comandos enviados por el ESP32.
- Identificar qué botón fue presionado.
- Controlar la articulación correspondiente.
- Actualizar continuamente la simulación.

La comunicación serial se realiza mediante la biblioteca ```PySerial```

# Video de la demostración
En el siguiente video se puede observar el funcionamiento del brazo robótico controlado mediante los seis botones conectados al ESP32:

[![Video de demostración](https://img.youtube.com/vi/7I3oRRVXjyA/0.jpg)](https://youtu.be/7I3oRRVXjyA)

# Conclusión 

El desarrollo de este proyecto permitió integrar un sistema físico basado en un ESP32 con una simulación de un brazo robótico desarrollada en PyBullet.

El ESP32 se encargó de detectar las acciones realizadas mediante seis botones físicos y transmitirlas mediante comunicación serial al computador.

Posteriormente, Python recibió e interpretó estos comandos para controlar las diferentes articulaciones del brazo robótico.

Uno de los principales aspectos del desarrollo fue la identificación de las articulaciones correspondientes a cada movimiento. 

Durante las pruebas se comprobó que la articulación joint_gripper producía un movimiento vertical, por lo que se utilizaron las articulaciones joint_dedo_izq y joint_dedo_der para obtener correctamente la apertura y cierre de la pinza.

Finalmente, se obtuvo un sistema funcional que permite controlar la base, el brazo y la pinza del robot mediante botones físicos, representando los movimientos en tiempo real dentro de PyBullet.

# Autora 

Lina María Moreno Ospina 

7004589

Ingeniería Mecatrónica

Universidad Militar Nueva Granada 
