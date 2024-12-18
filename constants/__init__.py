import os

CHECKBOXES =  ["Lowercase", "Uppercase", "Numbers", "Symbols"]

PATH_TO_SOUNDS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sounds")
PATH_TO_ALERT_SOUND = os.path.join(PATH_TO_SOUNDS, "alert.wav")
