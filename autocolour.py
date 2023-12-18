import pyautogui

def get_color_at_position(x, y):
    try:
        # Get the RGB values of the color at the specified position
        color = pyautogui.pixel(x, y)
        print(f"Color at position ({x}, {y}): RGB({color[0]}, {color[1]}, {color[2]})")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace these coordinates with the position you're interested in
    target_position = (1180, 670)

    get_color_at_position(*target_position)
