import pyautogui
import time

def print_mouse_position():
    try:
        while True:
            # Get the current mouse position
            x, y = pyautogui.position()
            print(f"Mouse Position: X={x}, Y={y}")

            # Wait for 3 seconds before the next iteration
            time.sleep(3)

    except KeyboardInterrupt:
        print("Mouse position printing stopped.")

if __name__ == "__main__":
    print("Press Ctrl+C to stop.")
    print_mouse_position()
