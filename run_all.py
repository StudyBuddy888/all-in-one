import multiprocessing
import os
import signal
import time

def run_script(script_name):
    """Run a Python script in a separate process"""
    os.system(f"python {script_name}")

if __name__ == "__main__":
    scripts = ["voice_assistant.py", "distraction_detector.py", "face_recognition_module.py"]
    
    processes = []
    
    try:
        for script in scripts:
            process = multiprocessing.Process(target=run_script, args=(script,))
            process.start()
            processes.append(process)

        while True:
            time.sleep(1)  # Keep the main process alive
        
    except KeyboardInterrupt:
        print("\n🛑 Keyboard Interrupt detected! Stopping all processes...")
        for process in processes:
            os.kill(process.pid, signal.SIGTERM)  # ✅ Gracefully terminate each process

        print("✅ All processes stopped successfully.")
