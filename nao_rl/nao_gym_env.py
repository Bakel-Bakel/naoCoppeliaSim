import numpy as np
import gymnasium as gym
from gymnasium import spaces
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

class NaoCoppeliaEnv(gym.Env):
    def __init__(self):
        super(NaoCoppeliaEnv, self).__init__()

        # Connect to CoppeliaSim
        self.client = RemoteAPIClient()
        self.sim = self.client.getObject('sim')

        # Get joint handles
        self.LHipPitch = self.sim.getObject('/NAO/LHipPitch')
        self.RHipPitch = self.sim.getObject('/NAO/RHipPitch')
        self.LKneePitch = self.sim.getObject('/NAO/LKneePitch')
        self.RKneePitch = self.sim.getObject('/NAO/RKneePitch')
        self.LAnklePitch = self.sim.getObject('/NAO/LAnklePitch')
        self.RAnklePitch = self.sim.getObject('/NAO/RAnklePitch')

        # Define action space (continuous values for leg joints)
        self.action_space = spaces.Box(low=-0.5, high=0.5, shape=(6,), dtype=np.float32)

        # Define observation space (joint angles)
        self.observation_space = spaces.Box(low=-1.0, high=1.0, shape=(6,), dtype=np.float32)

        # Start the simulation
        self.sim.startSimulation()
        time.sleep(1)

    def safe_get_joint_position(self, joint_handle):
        """ Get joint position with timeout to prevent blocking. """
        start_time = time.time()
        while time.time() - start_time < 2:  # 2-second timeout
            try:
                pos = self.sim.getJointPosition(joint_handle)
                if pos is not None:
                    return float(pos)  # Convert safely
            except:
                time.sleep(0.1)  # Retry after short delay
        print(f"Warning: Timeout while getting joint position for {joint_handle}")
        return 0.0  # Default safe value

    def step(self, action):
        action = [float(a) for a in action]  # Convert NumPy floats to Python floats

        print("Applying Actions:", action)  # Debugging Log

        # Apply joint actions
        self.sim.setJointTargetPosition(self.LHipPitch, action[0])
        self.sim.setJointTargetPosition(self.RHipPitch, action[1])
        self.sim.setJointTargetPosition(self.LKneePitch, action[2])
        self.sim.setJointTargetPosition(self.RKneePitch, action[3])
        self.sim.setJointTargetPosition(self.LAnklePitch, action[4])
        self.sim.setJointTargetPosition(self.RAnklePitch, action[5])

        time.sleep(0.1)  # Simulate step

        print("Fetching Joint Positions...")  # Debugging Log

        # Get new joint states with timeout
        obs = [
            self.safe_get_joint_position(self.LHipPitch),
            self.safe_get_joint_position(self.RHipPitch),
            self.safe_get_joint_position(self.LKneePitch),
            self.safe_get_joint_position(self.RKneePitch),
            self.safe_get_joint_position(self.LAnklePitch),
            self.safe_get_joint_position(self.RAnklePitch),
        ]

        print("Observation:", obs)  # Debugging Log

        # Ensure no NaN values
        if any(np.isnan(obs)) or any(np.isinf(obs)):
            print("Warning: NaN detected in observation space!")
            obs = [0.0] * 6  # Reset observation to safe values

        reward = obs[2] - 0.5 * abs(obs[0])  # Reward function
        done = obs[2] < -0.5  # Done condition if NAO falls

        print("Reward:", reward, "Done:", done)  # Debugging Log

        return np.array(obs, dtype=np.float32), reward, done, False, {}


    def reset(self, seed=None, options=None):
        self.sim.stopSimulation()
        time.sleep(1)
        self.sim.startSimulation()
        time.sleep(1)

        # Reset NAO to default position
        obs = np.zeros(6, dtype=np.float32)
        return obs, {}

    def close(self):
        self.sim.stopSimulation()
