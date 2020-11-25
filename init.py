import tkinter as tk
import os
import json


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Bot Startup")
        self.label = tk.Label(text="Bot Token:")
        self.entry = tk.Entry()
        self.button = tk.Button(self, text="Start", command=lambda: self.runCommand(self.onButton()))
        self.label.pack(padx=20, pady=20)
        self.button.pack()
        self.entry.pack(padx=20, pady=20)

    def runCommand(self, input):
        a_file = open("Source\scoreboard.json", "r")
        json_object = json.load(a_file)
        a_file.close()

        a_file = open("Source\scoreboard.json", "w")
        json_object["token"] = str(input)
        json.dump(json_object, a_file)
        a_file.close()
        self.destroy()
        try:
            os.system('python3 Source\DiscordDieRoller.py')
        except:
            error = tk.Tk()
            error.label = tk.Label(text="The runtime environment gave an error!")
            error.label.pack(padx=20, pady=20)
            error.mainloop()
        finally:
            return
            self.mainloop()


    def onButton(self):
        val = self.entry.get()
        return val


app = SampleApp()
app.mainloop()
