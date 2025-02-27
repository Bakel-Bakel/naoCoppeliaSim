import time
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Connect to CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')

# Get NAO joint handles
joint_names = [
    "HeadYaw", "HeadPitch",
    "LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll",
    "RShoulderPitch", "RShoulderRoll", "RElbowYaw", "RElbowRoll",
    "LHipYawPitch", "LHipRoll", "LHipPitch", "LKneePitch", "LAnklePitch", "LAnkleRoll",
    "RHipYawPitch", "RHipRoll", "RHipPitch", "RKneePitch", "RAnklePitch", "RAnkleRoll"
]

# Retrieve joint handles
joints = {name: sim.getObject('/NAO/'+name) for name in joint_names}

# Function to make NAO walk forward
def nao_walk():
    steps = 10  # Number of steps
    step_size = 0.1  # Step length
    for i in range(steps):
        # Move left leg forward
        sim.setJointTargetPosition(joints["LHipPitch"], -0.3)  
        sim.setJointTargetPosition(joints["LKneePitch"], 0.6)  
        sim.setJointTargetPosition(joints["LAnklePitch"], -0.3) 
        time.sleep(0.5)

        # Move right leg forward
        sim.setJointTargetPosition(joints["RHipPitch"], -0.3)  
        sim.setJointTargetPosition(joints["RKneePitch"], 0.6)  
        sim.setJointTargetPosition(joints["RAnklePitch"], -0.3)  
        time.sleep(0.5)

        # Reset to standing position
        sim.setJointTargetPosition(joints["LHipPitch"], 0.0)  
        sim.setJointTargetPosition(joints["LKneePitch"], 0.0)  
        sim.setJointTargetPosition(joints["LAnklePitch"], 0.0)  
        sim.setJointTargetPosition(joints["RHipPitch"], 0.0)  
        sim.setJointTargetPosition(joints["RKneePitch"], 0.0)  
        sim.setJointTargetPosition(joints["RAnklePitch"], 0.0)  
        time.sleep(0.5)

# Start simulation
sim.startSimulation()
time.sleep(2)

# Execute walking motion
nao_walk()

# Stop simulation
time.sleep(2)
sim.stopSimulation()

