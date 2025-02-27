import time
from coppeliaSimZMQRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Get joint handles for NAO's right arm
RShoulderPitch = sim.getObject('/NAO/RShoulderPitch')
RElbowRoll = sim.getObject('/NAO/RElbowRoll')

sim.startSimulation()
time.sleep(2)

# Wave motion loop
for _ in range(3):
    sim.setJointTargetPosition(RShoulderPitch, -0.5)  # Raise arm
    sim.setJointTargetPosition(RElbowRoll, -1.5)  # Bend elbow
    time.sleep(0.5)

    sim.setJointTargetPosition(RElbowRoll, 0.0)  # Straighten elbow
    time.sleep(0.5)

# Stop simulation
sim.stopSimulation()

