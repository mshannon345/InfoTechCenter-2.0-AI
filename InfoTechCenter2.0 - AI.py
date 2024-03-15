import time
import sys


def loading_process(total_iterations=20, ellipsis_reset_threshold=4, sleep_time=0.5):
    # Print welcome message
    print("\n\nWelcome to InfoTech Center V1.0\n")
    # Wait for 2 seconds
    time.sleep(2)

    ellipsis = 0
    # Loop to simulate loading process
    for iteration in range(1, total_iterations + 1):
        # Calculate progress percentage
        progress = iteration / total_iterations * 100
        # Construct progress message
        message = f"InfoTech Center Operation System Loading... [{progress:.0f}%]"
        # Write progress message to console
        sys.stdout.write("\r" + message)
        sys.stdout.flush()  # Flush buffer to ensure immediate display
        # Pause execution for a specified time
        time.sleep(sleep_time)

        # Reset ellipsis counter if it reaches the threshold
        ellipsis = (ellipsis + 1) % (ellipsis_reset_threshold + 1)

    # Print completion message
    print("\n\nOperating System Booted up - Retina Scanned - Access Granted!")


if __name__ == "__main__":
    loading_process()

