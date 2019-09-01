import serial
from tkinter import *
arduinoData = serial.Serial('COM3', 9600)
def led_on():
    arduinoData.write(b'1')
def led_off():
    arduinoData.write(b'0')

ventana = Tk()
ventana.title("interface Python Arduino")
# ventana.iconbitmap("Arduino.ico")
ventana.geometry("200x150")

miFrame = Frame(ventana, width = 650, height = 350)
miFrame.pack()

miFrame.config(bd = 5)
miFrame.config(relief = "groove")

botonEnvio = Button(miFrame, text = "ON", command = led_on)
botonEnvio.pack(anchor = "center", padx = 10, pady = 10)

botonEnvio1 = Button(miFrame, text = "OFF", command = led_off)
botonEnvio1.pack(anchor = "center", padx = 10, pady = 10)
ventana.mainloop()