#!/bin/bash

# Script to set up Python environment and install dependencies
echo "🚀 Starting NAO RL Setup..."

# Step 1: Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python3 is not installed. Please install Python3 first!"
    exit 1
fi

# Step 2: Create Virtual Environment
if [ ! -d "nao_env" ]; then
    echo "📁 Creating Python virtual environment..."
    python3 -m venv nao_env
else
    echo "✅ Virtual environment already exists."
fi

# Step 3: Activate Virtual Environment
echo "🔁 Activating virtual environment..."
source nao_env/bin/activate

# Step 4: Upgrade pip
echo "⬆️ Upgrading pip..."
pip install --upgrade pip

# Step 5: Install Required Python Packages
echo "📦 Installing required dependencies..."

pip install \
    tensorflow \
    numpy \
    gymnasium \
    stable-baselines3 \
    stable-baselines \
    coppeliasim-zmqremoteapi-client \
    matplotlib \
    opencv-python \
    scipy \
    tqdm

# Step 6: Confirm Installation
echo "✅ All dependencies installed successfully!"

# Step 7: Important Instructions for CoppeliaSim
echo ""
echo "⚠️  IMPORTANT: You must also set up CoppeliaSim correctly!"
echo ""
echo "📥 Download CoppeliaSim from: https://www.coppeliarobotics.com/downloads"
echo ""
echo "🛠️ Ensure the 'ZMQ Remote API' is enabled in CoppeliaSim:"
echo "   - Open CoppeliaSim."
echo "   - Go to 'Tools' > 'ZMQ Remote API Server'."
echo "   - Click 'Start'."
echo ""
echo "✅ If the ZMQ API is enabled, you can now run the training script:"
echo ""
echo "   python naoWalk.py"
echo ""

# Step 8: Automatically Enter the Environment
exec bash --rcfile <(echo "source nao_env/bin/activate")

