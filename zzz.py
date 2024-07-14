import multiprocessing
import time
import random
from datetime import datetime

def worker():
    # Wait for a random amount of time between 0 and 1 second
    time.sleep(random.uniform(0, 1))
    # Print the current time
    print(f"Process ID: {multiprocessing.current_process().pid}, Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")

if __name__ == "__main__":
    # Create a list to hold the process objects
    processes = []

    # Create and start three separate processes
    for _ in range(3):
        process = multiprocessing.Process(target=worker)
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()