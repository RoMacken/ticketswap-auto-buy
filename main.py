import time
import pyautogui
import win32com.client as comctl
import keyboard


def ifavailable(coords) -> None:

    if pyautogui.locateOnScreen("home.png", confidence=0.9) is None:
        pyautogui.click(coords)
        time.sleep(0.5)

        while True:
            if pyautogui.locateOnScreen("buy.png", confidence=0.9) is not None:
                pyautogui.click(pyautogui.center(
                    pyautogui.locateOnScreen("buy.png", confidence=0.9)))
                exit(0)
            if keyboard.is_pressed("F10"):
                exit(1)


def main() -> None:

    wsh = comctl.Dispatch("WScript.Shell")
    wsh.AppActivate("Google Chrome")
    coords = pyautogui.center(
        pyautogui.locateOnScreen("home.png", confidence=0.9))
    coords = (coords[0], coords[1] + 10)

    while True:
        wsh.AppActivate("Google Chrome")
        time.sleep(0.5)
        ifavailable(coords)
        wsh.SendKeys("{F5}")

        if keyboard.is_pressed("F10"):
            break
        time.sleep(3)


if __name__ == "__main__":
    main()
