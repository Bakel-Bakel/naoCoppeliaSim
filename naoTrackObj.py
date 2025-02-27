import time
from coppeliaSimZMQRemoteApi import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Get NAO's head joint for tracking
HeadYaw = sim.getObject('/NAO/HeadYaw')

# Get object to track (e.g., a red ball)
target = sim.getObject('/RedBall')

sim.startSimulation()
time.sleep(2)

# Tracking loop
for _ in range(20):
    target_pos = sim.getObjectPosition(target, -1)
    nao_pos = sim.getObjectPosition(HeadYaw, -1)

    # Calculate direction to move head
    error = target_pos[0] - nao_pos[0]
    sim.setJointTargetPosition(HeadYaw, error)

    time.sleep(0.1)

# Stop simulation
sim.stopSimulation()

