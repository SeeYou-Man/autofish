import pyautogui
import threading
import time

class Scanner:
    def __init__(self, position, base_color):
        self.position = position
        self.base_color = base_color
        self.is_running = True

    def scan(self):
        while self.is_running:
            try:
                # Capture the pixel color at the given position
                color = pyautogui.pixel(*self.position)
                print(f"Color at position ({self.position[0]}, {self.position[1]}): RGB({color[0]}, {color[1]}, {color[2]})")
                # Check if the color matches the base color
                if color != self.base_color:
                    print("Test")
                    pyautogui.rightClick()
                    print("Test2")
                    #raise Exception(f"Color change detected at {self.position}!")

            except Exception as e:
                print(e)
    
            time.sleep(0.2)  # Adjust the sleep duration as needed

    def stop(self):
        self.is_running = False

def get_color_at_position(x, y):
    try:
        # Get the RGB values of the color at the specified position
        color = pyautogui.pixel(x, y)
        print(f"Color at position ({x}, {y}): RGB({color[0]}, {color[1]}, {color[2]})")
        return color

    except Exception as e:
        print(f"Error: {e}")

def main():
    fishing_rod_position = [(1081, 688)]
    time_to_click_color = get_color_at_position(fishing_rod_position[0][0],fishing_rod_position[0][1])
    scanner_color = (220, 234, 235)
    bar_colors = []
    # Define the positions and base colors for each scanner
    fishisng_positions = [(1180, 670), (1210, 670), (1240, 670), (1270, 670), (1300, 670), (1330, 670), (1360, 670)]
    base_color = (39, 130, 171)  # Replace with the base color you want to ignore

    scanners = []
    for position in fishisng_positions:
        bar_colors.append(get_color_at_position(*position))
    print(bar_colors,"\n")
    for color in bar_colors:
        if color == time_to_click_color:
            scanner = Scanner(fishisng_positions[bar_colors.index(color)],color)
            thread = threading.Thread(target=scanner.scan)
            thread.start()
            scanners.append((scanner, thread))
            try:
            # Keep the main thread alive
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
            # Stop all scanner threads on keyboard interrupt
                for scanner, thread in scanners:
                    scanner.stop()
                    thread.join()
    # Create and start scanner threads
    #for position in fishisng_positions:

    #    scanner = Scanner(position, base_color)
    #    
    #    
    #    

    #try:
    #    # Keep the main thread alive
    #    while True:
    #        time.sleep(1)

    #except KeyboardInterrupt:
    #    # Stop all scanner threads on keyboard interrupt
    #    for scanner, thread in scanners:
    #        scanner.stop()
    #        thread.join()

if __name__ == "__main__":
    main()
