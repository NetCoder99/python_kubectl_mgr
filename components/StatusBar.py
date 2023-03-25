import customtkinter as ctk

widget_font = ("Verdana", 15)
class StatusBar(ctk.CTkFrame):
    def __init__(self, master):
        ctk.CTkFrame.__init__(self, master)
        self.statusLabel = ctk.CTkLabel(self, text="Status: Initialized")
        self.statusLabel.pack(side=ctk.LEFT, ipadx=10)
        #self.pack(side=ctk.BOTTOM, fill=ctk.X)

        self.actionLabel = ctk.CTkLabel(self, text="Current Action: None")
        self.actionLabel.pack(side=ctk.RIGHT, ipadx=10)
        self.pack(side=ctk.BOTTOM, fill=ctk.X)

    def setAction(self, inp_text):
        self.actionLabel.configure(text=inp_text)
