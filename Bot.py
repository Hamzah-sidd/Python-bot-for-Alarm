import pyautogui
import time
from playsound import playsound

# Path to the alarm sound file (replace with the actual path)
alarm_sound_path = "C:\\Users\\HamzahFurqan\\Desktop\\ChromeDriver\\alarm.wav"

# Region of the screen to monitor (update these coordinates)
# Use `pyautogui.displayMousePosition()` to find the region where messages appear
monitor_region = (500, 200, 600, 300)  # Example coordinates (left, top, width, height)

def monitor_group():
    """
    Monitor a WhatsApp group chat for new messages and play an alarm when a new message arrives.
    """
    print("Monitoring the group chat for new messages...")
    try:
        # Take an initial screenshot of the region
        last_screenshot = pyautogui.screenshot(region=monitor_region)
        
        while True:
            # Take a new screenshot of the same region
            current_screenshot = pyautogui.screenshot(region=monitor_region)
            
            # Compare the screenshots
            if current_screenshot != last_screenshot:
                print("New message detected! Playing alarm...")
                
                # Play the alarm sound
                playsound(alarm_sound_path)
                
                # Update the last screenshot
                last_screenshot = current_screenshot
            
            # Wait for a short interval before checking again
            time.sleep(2)
    
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main execution
if __name__ == "__main__":
    print("Please ensure the WhatsApp window is open and the group chat is visible.")
    time.sleep(5)  # Wait for the user to prepare
    monitor_group()
