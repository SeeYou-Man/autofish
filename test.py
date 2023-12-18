import pyautogui
import time

def get_color_at_position(x, y):
    try:
        # Get the RGB values of the color at the specified position
        color = pyautogui.pixel(x, y)
        return color

    except Exception as e:
        print(f"Error: {e}")
        return None

def right_click_if_color_changes(target_position, base_color):
    try:
        while True:
            # Get the current color at the specified position
            current_color = get_color_at_position(*target_position)

            # Check if the color has changed
            if current_color and current_color != base_color:
                # Right-click action
                pyautogui.rightClick()
                print(f"Color change detected at {target_position}. Right-click performed.")

            # Wait for 1 second before the next iteration
            time.sleep(1)

    except KeyboardInterrupt:
        print("Color change detection stopped.")

if __name__ == "__main__":
    # Replace these coordinates with the position you're interested in
    target_position = (1240, 670)

    # Replace this color with the base color you want to ignore
    base_color = (39, 130, 171)

    if base_color:
        print("Base color:", base_color)
        right_click_if_color_changes(target_position, base_color)
    else:
        print("Unable to get base color.")
