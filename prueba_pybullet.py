import pybullet as p
import pybullet_data
import time

# Abrir ventana gráfica
p.connect(p.GUI)

# Cargar recursos de PyBullet
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Cargar un plano
p.loadURDF("plane.urdf")

# Gravedad
p.setGravity(0, 0, -9.81)

while True:
    p.stepSimulation()
    time.sleep(1/240)
  
