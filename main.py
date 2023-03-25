import customtkinter as ctk

from components.Clusters import KubeClusters
from components.StatusBar import StatusBar
from kubectl.config_read import getKubeConfigDetails
from menus.MenuMain import MainMenu

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")
appWidth, appHeight = 900, 800

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Kubectl Config Manager")
        self.geometry(f"{appWidth}x{appHeight}")

        MainMenu(self)

        self.clusterFrame = ctk.CTkFrame(self)
        self.KubeClusters = KubeClusters(self.clusterFrame, self)
        self.clusterFrame.pack(side='top', fill='both', expand=True)

        self.statusFrame  = ctk.CTkFrame(self)
        self.StatusBar    = StatusBar(self.statusFrame)
        self.statusFrame.pack(side='bottom', fill='both', expand=True)

    def generateResults(self, event=None):
        self.StatusBar.setAction(f'generateResults - event:{event}')
        print(f'generateResults - event:{event}')

    def set_kube_details(self, kube_config_details):
        self.KubeClusters.setValues(kube_config_details)

    def reset_app(self):
        print('Reloading all settings')
        #app.quit()

    def shutdown_app(self):
        print('Shutting down 1')
        app.quit()

# ----------------------------------------------------
if __name__ == "__main__":
    kube_config = getKubeConfigDetails()

    app = App()
    app.set_kube_details(kube_config)

    # trap the close event to kill the matplotlib agent
    app.protocol('WM_DELETE_WINDOW', app.shutdown_app)

    app.mainloop()
