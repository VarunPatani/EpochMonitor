import time
from epochmonitor import EpochMonitor


# Test 1: Using the decorator
@EpochMonitor(log_file_prefix="decorator_test", file_format="json", gpu_index=1)
def decorated_training(epochs, monitor=None):
    for i in range(epochs):
        monitor.start_epoch()
        print(f"Decorated training, epoch {i + 1}...")
        time.sleep(1.5)
        monitor.end_epoch()


# Test 2: Using the context manager
def context_manager_training(epochs):
    with EpochMonitor(log_file_prefix="context_test", file_format="csv") as monitor:
        for i in range(epochs):
            monitor.start_epoch()
            print(f"Context manager training, epoch {i + 1}...")
            time.sleep(1)
            monitor.end_epoch()


if __name__ == "__main__":
    print("--- TESTING DECORATOR ---")
    decorated_training(epochs=2)

    print("\n\n--- TESTING CONTEXT MANAGER ---")
    context_manager_training(epochs=3)
