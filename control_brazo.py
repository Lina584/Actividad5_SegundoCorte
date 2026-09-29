import pybullet as p
import pybullet_data
import serial
import time

# ESP32
arduino = serial.Serial("COM4", 115200, timeout=0.05)
time.sleep(2)

# PyBullet
p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.loadURDF("plane.urdf")

robot_id = p.loadURDF(
    "brazo.urdf",
    [0, 0, 0.15],
    useFixedBase=True
)

# Posiciones iniciales
base = 0.0
brazo = 0.0
pinza = 0.0
dedo_izq = 0.0
dedo_der = 0.0

# Pasos de movimiento
PASO_ANGULO = 0.1
PASO_PINZA = 0.01

print("================================")
print(" CONTROL DEL BRAZO ACTIVADO")
print("================================")
print("Boton 1: Base izquierda")
print("Boton 2: Base derecha")
print("Boton 3: Brazo arriba")
print("Boton 4: Brazo abajo")
print("Boton 5: Pinza abrir")
print("Boton 6: Pinza cerrar")
print("================================")

while p.isConnected():

    dato = arduino.readline().decode(errors="ignore").strip()

    # BOTON 1 - BASE IZQUIERDA
    if dato == "BOTON1":
        base = max(-2.5, base - PASO_ANGULO)

        p.setJointMotorControl2(
            robot_id,
            0,
            p.POSITION_CONTROL,
            targetPosition=base
        )

        print("Base izquierda:", round(base, 2))

    # BOTON 2 - BASE DERECHA
    elif dato == "BOTON2":
        base = min(2.5, base + PASO_ANGULO)

        p.setJointMotorControl2(
            robot_id,
            0,
            p.POSITION_CONTROL,
            targetPosition=base
        )

        print("Base derecha:", round(base, 2))

    # BOTON 3 - BRAZO ARRIBA
    elif dato == "BOTON3":
        brazo = min(2.0, brazo + PASO_ANGULO)

        p.setJointMotorControl2(
            robot_id,
            1,
            p.POSITION_CONTROL,
            targetPosition=brazo
        )

        print("Brazo arriba:", round(brazo, 2))

    # BOTON 4 - BRAZO ABAJO
    elif dato == "BOTON4":
        brazo = max(-2.0, brazo - PASO_ANGULO)

        p.setJointMotorControl2(
            robot_id,
            1,
            p.POSITION_CONTROL,
            targetPosition=brazo
        )

        print("Brazo abajo:", round(brazo, 2))

        # BOTON 5 - ABRIR PINZA
    elif dato == "BOTON5":

        dedo_izq = min(0.05, dedo_izq + PASO_PINZA)
        dedo_der = min(0.05, dedo_der + PASO_PINZA)

        p.setJointMotorControl2(
            robot_id,
            3,
            p.POSITION_CONTROL,
            targetPosition=dedo_izq
        )

        p.setJointMotorControl2(
            robot_id,
            4,
            p.POSITION_CONTROL,
            targetPosition=dedo_der
        )

        print("Pinza abrir")

    # BOTON 6 - CERRAR PINZA
    elif dato == "BOTON6":

        dedo_izq = max(0.0, dedo_izq - PASO_PINZA)
        dedo_der = max(0.0, dedo_der - PASO_PINZA)

        p.setJointMotorControl2(
            robot_id,
            3,
            p.POSITION_CONTROL,
            targetPosition=dedo_izq
        )

        p.setJointMotorControl2(
            robot_id,
            4,
            p.POSITION_CONTROL,
            targetPosition=dedo_der
        )

        print("Pinza cerrar")

    p.stepSimulation()
    time.sleep(1 / 240)
