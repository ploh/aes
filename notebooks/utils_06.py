import random
import time


# Simuliere Arbeit mit zufälliger Dauer
def random_sleep():
    time.sleep(random.uniform(0, 0.0001))

def worker(n, message):
    random_sleep()
    print(f"Worker {n}: {message}")
    return 100 * n, message
