import Tkinter as tk
import base64
import time

import pyautogui


def screen_capture():
    import keyboard
    import pyautogui as pag
    from PIL import ImageGrab
    if keyboard.wait(hotkey='ctrl+alt') is None:
        x1, y1 = pag.position()
        if keyboard.wait(hotkey='ctrl+alt') is None:
            x2, y2 = pag.position()
            image_pos = (x1, y1, x2, y2)
            print image_pos
            image = ImageGrab.grab(image_pos)
            filename = "C:\\Users\\watson.zeng\\Pictures\\screenshot\\screen.png"
            image.save(filename)
            return filename
    return None


def get_format_datetime(date_format='%Y%m%d_%H%M%S'):
    return time.strftime(date_format, time.localtime(time.time()))


def write_to_clipboard(a_str):
    r = tk.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(a_str)
    r.destroy()


def convert_to_base64(filepath):
    with open(filepath, "rb") as f:
        base64_data = base64.b64encode(f.read())
    pic_name = "pic_%s" % get_format_datetime()
    html_data = '[%s]:data:image/png;base64,%s' % (pic_name, base64_data)
    write_to_clipboard(html_data)


def take_screen_shot():
    screen_shot = pyautogui.screenshot()
    # image_data = screen_shot.tobytes()
    filepath = "test.png"
    screen_shot.save(filepath)
    # "C:\\Users\\user\\Desktop\\20170508134213.png"
    with open(filepath, "rb") as f:
        base64_data = base64.b64encode(f.read())
    pic_name = "pic_%s" % get_format_datetime()
    html_data = '[%s]:data:image/png;base64,%s' % (pic_name, base64_data)
    write_to_clipboard(html_data)
    # with open("test.html", "w") as f:
    #     f.write(html_data)


def main():
    root = tk.Tk()

    canvas1 = tk.Canvas(root, width=300, height=300)
    canvas1.pack()

    my_button = tk.Button(text='Take Screenshot', command=take_screen_shot, bg='green', fg='white', font=10)
    canvas1.create_window(150, 150, window=my_button)

    root.mainloop()


if __name__ == '__main__':
    screen_capture()
