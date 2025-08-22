import subprocess
import os

# === Configuration ===
model_name = "trustsoft8"
start_model = "vie"
ground_truth_dir = f"data/{model_name}-ground-truth"
tessdata_path = "../tessdata"
max_iterations = "50000"
epochs= '2' 
learning_rate = "0.0001"
ratio_train = "0.80"
target_error_rate = "0.001"

# === Training Commands ===
commands = [
    f"make training MODEL_NAME={model_name} START_MODEL={start_model} " +
    f"TESSDATA={tessdata_path} " +
    f"GROUND_TRUTH_DIR={ground_truth_dir} " +
    f"MAX_ITERATIONS={max_iterations} " +
    # f"EPOCHS={epochs} " +
    f"LEARNING_RATE={learning_rate} " +
    f"RATIO_TRAIN={ratio_train} TARGET_ERROR_RATE={target_error_rate} " 
]


# === Run Commands ===
for cmd in commands:
    print(f"🔧 Running: {cmd}")
    process = subprocess.run(cmd, shell=True)
    if process.returncode != 0:
        print(f"❌ Command failed: {cmd}")
        break
