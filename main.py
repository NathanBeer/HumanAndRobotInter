import threading
import os
import time
import RobotSeeing
import RobotHearing
import RobotMovement
import RobotNavigator

def speak_async(text):
    """Speaks text using gTTS and plays via mpg123 in a background thread."""
    def run_speak():
        # gtts-cli generates the audio, mpg123 plays it instantly
        # -q flag is for 'quiet' mode to avoid console clutter
        cmd = f"gtts-cli '{text}' | mpg123 -q -"
        os.system(cmd)
    
    # Daemon thread ensures the audio thread closes when the main program exits
    threading.Thread(target=run_speak, daemon=True).start()

def run_robot():
    # 1. Initialization
    RobotMovement.robot_init()
    print("[System] Adjusting camera arm...")
    RobotMovement.move_arm(1, 90)
    RobotMovement.move_arm(2, 90)
    
    speak_async("Hello. Vision Dog is ready. What would you like me to find?")
    
    # 2. Main Interaction Loop
    while True:
        command = RobotHearing.listen_for_command().lower()
        if not command:
            continue
            
        # Check if the requested object is in our known model classes
        available_objects = [str(obj).lower() for obj in RobotSeeing.get_model_classes()]
        target = next((obj for obj in available_objects if obj in command), None)
        
        if target:
            speak_async(f"Searching for {target}")
            
            # 3. Perform Search via Navigator
            if RobotNavigator.perform_search_pattern(target):
                speak_async(f"I found the {target}. Moving towards it.")
                RobotMovement.move_forward(speed=50)
                # Keep moving briefly then stop
                time.sleep(1.5)
                RobotMovement.safe_stop()
                speak_async("I have arrived.")
            else:
                speak_async(f"I could not find the {target}.")
        else:
            speak_async("I didn't recognize that object. Please try again.")
            continue

        # 4. Check for further instructions
        speak_async("Is there anything else you would like me to find?")
        next_command = RobotHearing.listen_for_command().lower()
        
        stop_words = ["no", "nothing", "that's it", "that's all", "stop", "goodbye"]
        if any(word in next_command for word in stop_words):
            speak_async("Shutting down. Goodbye.")
            RobotMovement.move_arm(1, 0)
            break
        else:
            speak_async("Understood, let's keep going.")
            continue 

    RobotSeeing.release_camera()

if __name__ == "__main__":
    run_robot()