import time
from coppeliaSimZMQRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Get NAO's main joints
LHipPitch = sim.getObject('/NAO/LHipPitch')
RHipPitch = sim.getObject('/NAO/RHipPitch')
LKneePitch = sim.getObject('/NAO/LKneePitch')
RKneePitch = sim.getObject('/NAO/RKneePitch')
LAnklePitch = sim.getObject('/NAO/LAnklePitch')
RAnklePitch = sim.getObject('/NAO/RAnklePitch')

sim.startSimulation()
time.sleep(2)

# Make NAO sit down
sim.setJointTargetPosition(LHipPitch, -1.0)
sim.setJointTargetPosition(RHipPitch, -1.0)
sim.setJointTargetPosition(LKneePitch, 2.0)
sim.setJointTargetPosition(RKneePitch, 2.0)
sim.setJointTargetPosition(LAnklePitch, -1.0)
sim.setJointTargetPosition(RAnklePitch, -1.0)
time.sleep(2)

# Make NAO stand up
sim.setJointTargetPosition(LHipPitch, 0.0)
sim.setJointTargetPosition(RHipPitch, 0.0)
sim.setJointTargetPosition(LKneePitch, 0.0)
sim.setJointTargetPosition(RKneePitch, 0.0)
sim.setJointTargetPosition(LAnklePitch, 0.0)
sim.setJointTargetPosition(RAnklePitch, 0.0)
time.sleep(2)

sim.stopSimulation()

