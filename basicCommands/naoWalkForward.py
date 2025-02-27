import time
from coppeliaSimZMQRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Get joint handles for NAO's legs
LHipPitch = sim.getObject('/NAO/LHipPitch')
RHipPitch = sim.getObject('/NAO/RHipPitch')
LKneePitch = sim.getObject('/NAO/LKneePitch')
RKneePitch = sim.getObject('/NAO/RKneePitch')
LAnklePitch = sim.getObject('/NAO/LAnklePitch')
RAnklePitch = sim.getObject('/NAO/RAnklePitch')

sim.startSimulation()
time.sleep(2)

# Walking motion loop
for _ in range(5):
    # Move left leg forward
    sim.setJointTargetPosition(LHipPitch, -0.3)
    sim.setJointTargetPosition(LKneePitch, 0.6)
    sim.setJointTargetPosition(LAnklePitch, -0.3)
    time.sleep(0.5)

    # Move right leg forward
    sim.setJointTargetPosition(RHipPitch, -0.3)
    sim.setJointTargetPosition(RKneePitch, 0.6)
    sim.setJointTargetPosition(RAnklePitch, -0.3)
    time.sleep(0.5)

# Stop simulation
sim.stopSimulation()

