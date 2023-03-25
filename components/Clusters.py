from typing import List
import customtkinter as ctk

widget_font = ("Verdana", 15)
class KubeClusters(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent, border_color="green", border_width=3,bg_color='pink')
        self.clustersLabel = ctk.CTkLabel(parent, text="Select a cluster", font=widget_font)
        self.clustersLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
        self.clustersOptionMenu = ctk.CTkOptionMenu(parent, values=['option 1', 'option 2'], command=controller.generateResults)
        self.clustersOptionMenu.grid(row=0, column=1, padx=20, pady=20, sticky="ew")

        self.contextsLabel = ctk.CTkLabel(parent, text="Select a context", font=widget_font)
        self.contextsLabel.grid(row=0, column=2, padx=20, pady=20, sticky="ew")
        self.contextsOptionMenu = ctk.CTkOptionMenu(parent, values=['context 1', 'context 2'], command=controller.generateResults)
        self.contextsOptionMenu.grid(row=0, column=3, padx=20, pady=20, sticky="ew")

    def setValues(self, values_list):
        self.clustersOptionMenu.configure(values=values_list)
        self.clustersOptionMenu.set(values_list[0])
