import gymnasium as gym
import tensorflow as tf
import numpy as np
from stable_baselines.common.policies import MlpPolicy
from stable_baselines import PPO2  # TensorFlow-based PPO
from nao_gym_env import NaoCoppeliaEnv

# ✅ Initialize NAO environment
env = NaoCoppeliaEnv()

# ✅ Train PPO with TensorFlow-based policy
model = PPO2(MlpPolicy, env, verbose=1)

# ✅ Initialize reward tracking
reward_log = []

try:
    print("🚀 Training Started (TensorFlow). Press Ctrl+C to stop safely...")

    # ✅ Training loop
    for _ in range(100000):  # Number of training steps
        obs = env.reset()
        total_reward = 0
        done = False

        while not done:
            action, _ = model.predict(obs)
            obs, reward, done, _, _ = env.step(action)
            total_reward += reward

        reward_log.append(total_reward)  # ✅ Log episode reward

except KeyboardInterrupt:
    print("\n🛑 Training interrupted. Saving model and rewards...")
    model.save("nao_ppo_tf_model")
    env.close()

    # ✅ Save rewards to file
    np.save("training_rewards.npy", np.array(reward_log))
    print("✅ Model and reward log saved.")

# ✅ Save trained model and rewards
model.save("nao_ppo_tf_model")
np.save("training_rewards.npy", np.array(reward_log))
env.close()

