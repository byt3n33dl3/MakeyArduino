import tkinter as tk
import keyboard

def perform_action(key):
    actions = {
        "up": lambda: label.config(text="Moving Up!", fg="green"),
        "down": lambda: label.config(text="Moving Down!", fg="red"),
        "left": lambda: label.config(text="Moving Left!", fg="blue"),
        "right": lambda: label.config(text="Moving Right!", fg="orange"),
    }
    
    action = actions.get(key)
    if action:
        action()

def on_key_event(event):
    if event.event_type == 'down':
        perform_action(event.name)

root = tk.Tk()
root.title("Makey Makey Controller")

label = tk.Label(root, text="Press a key...", font=('Arial', 24))
label.pack(pady=20)

keyboard.on_press(on_key_event)

root.mainloop()

def main():
    """
    Main function to set up keyboard hooks and listen for events.
    """
    print("Listening for Makey Makey events. Press ESC to stop.")
    
    keyboard.hook(on_key_event)
    
    keyboard.wait('esc')
    
    print("Stopped listening for Makey Makey events.")

if __name__ == "__main__":
    try:
        main()
    except PermissionError:
        print("Permission denied. You might need to run this program as an administrator or root.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")