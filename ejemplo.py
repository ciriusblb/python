try:
  import Tkinter              # Python 2
  import ttk
except ImportError:
  import tkinter as Tkinter   # Python 3
  import tkinter.ttk as ttk

maxValue=100

# def progress(currentValue):
#     progressbar["value"]=currentValue


def main():
    root = Tkinter.Tk()
    root.title("Termometro")
    root.geometry("500x400")

    progressbar=ttk.Progressbar(root,orient="vertical",length=300,mode="determinate")
    progressbar.pack()
    def progress(currentValue):
        progressbar["value"]=currentValue

    currentValue=0
    progressbar["value"]=currentValue
    progressbar["maximum"]=maxValue

    divisions=10
    for i in range(divisions):
        currentValue=currentValue+10
        progressbar.after(500, progress(currentValue))
        progressbar.update() # Force an update of the GUI

    root.mainloop()


if __name__ == '__main__':
  main()