import tensorflow as tf
import numpy as np

# ✅ Load training data (Assuming you logged rewards in a .npy file)
rewards = np.load("training_rewards.npy")

# ✅ Define a simple TensorFlow model for analyzing NAO’s learning process
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation="relu"),
    tf.keras.layers.Dense(32, activation="relu"),
    tf.keras.layers.Dense(1, activation="linear")
])

# ✅ Compile the model
model.compile(optimizer="adam", loss="mse")

# ✅ Train the model on NAO’s reward data
model.fit(rewards[:-1], rewards[1:], epochs=50)

print("✅ TensorFlow Model Trained to Predict Future Rewards")

