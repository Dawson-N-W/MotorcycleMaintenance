import tkinter as tk

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Motorcycle Maintenance Application', font=controller.title_font)
        label.pack(side="top", fill="x", pady=50, padx=50)

        button1 = tk.Button(self, text='Add Motorcycle', command=lambda: controller.show_frame("Motorcycle_Page"), pady=20, height=1, width=20).pack(pady=20)
        button2 = tk.Button(self, text='Delete Motorcycle', command=lambda: controller.show_frame("Delete_Motorcycle_Page"), pady=20, height=1, width=20).pack(pady=20)
        button3 = tk.Button(self, text='Update Mileage', command=lambda: controller.show_frame("Update_Motorcycle_Page"), pady=20, height=1, width=20).pack(pady=20)
        button4 = tk.Button(self, text='Maintenance', command=lambda: controller.show_frame("Maintenance_Page"), pady=20,height=1, width=20).pack(pady=20)