import time
import sys


def loading_process(total_iterations=20, ellipsis_reset_threshold=4, sleep_time=0.5):
    print("\n\nWelcome to InfoTech Center V1.0\n")
    time.sleep(2)

    ellipsis = 0
    for iteration in range(1, total_iterations + 1):
        progress = iteration / total_iterations * 100
        message = f"InfoTech Center Operation System Loading... [{progress:.0f}%]"
        sys.stdout.write("\r" + message)
        sys.stdout.flush()
        time.sleep(sleep_time)

        ellipsis = (ellipsis + 1) % (ellipsis_reset_threshold + 1)

    print("\n\nOperating System Booted up - Retina Scanned - Access Granted!")


if __name__ == "__main__":
    loading_process()
