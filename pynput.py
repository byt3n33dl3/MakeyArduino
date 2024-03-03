from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        print(f'Alphanumeric key {key.char} pressed')
    except AttributeError:
        print(f'Special key {key} pressed')

def on_release(key):
    print(f'{key} released')
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()