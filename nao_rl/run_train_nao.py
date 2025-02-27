import gymnasium as gym
from stable_baselines3 import PPO
from nao_gym_env import NaoCoppeliaEnv

# Load environment
env = NaoCoppeliaEnv()

# Load trained model
model = PPO.load("nao_ppo_model")

# Test model
obs, _ = env.reset()
for _ in range(100):
    action, _states = model.predict(obs)
    obs, reward, done, _, _ = env.step(action)
    if done:
        obs, _ = env.reset()

env.close()
