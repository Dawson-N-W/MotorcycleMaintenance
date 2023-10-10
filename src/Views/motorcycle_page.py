import tkinter as tk
from src.Controllers.motorcycle_page_controller import *

class Motorcycle_Page(tk.Frame):
   def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      self.controller = controller
      label = tk.Label(self, text='Add Motorcycle', font=controller.title_font)
      label.pack(side="top", fill="x", pady=50, padx=50)

      make_label = tk.Label(self, text='Make:')
      make_label.pack()
      make_entry = tk.Entry(self)
      make_entry.pack()
        
      model_label = tk.Label(self, text='Model:')
      model_label.pack()
      model_entry = tk.Entry(self)
      model_entry.pack()
        
      year_label = tk.Label(self, text='Year:')
      year_label.pack()
      year_entry = tk.Entry(self)
      year_entry.pack()
        
      mileage_label = tk.Label(self, text='Mileage:')
      mileage_label.pack()
      mileage_entry = tk.Entry(self)
      mileage_entry.pack()

      error_label = tk.Label(self, text='Please check all fields.', fg='red')
      error_label.pack_forget()

      def on_error():
         error_label.pack()

      def remove_error():
         error_label.pack_forget()
      
      
        
      def submit_data():
         remove_error()
         make = make_entry.get()
         model = model_entry.get()
         year = year_entry.get()
         mileage = mileage_entry.get()
         if fetch_and_store_motorcycle(make, model, year, mileage) == -1:
            on_error()
            return
         #display success message
         success_label = tk.Label(self, text='Motorcycle added successfully!', fg='green')
         success_label.pack()
         success_label.after(2000, lambda: success_label.destroy())
         #clear entry fields
         make_entry.delete(0, 'end')
         model_entry.delete(0, 'end')
         year_entry.delete(0, 'end')
         mileage_entry.delete(0, 'end')

      submit = tk.Button(self, text='Submit', command=submit_data)
      submit.pack()

      button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("StartPage"))
      button.pack()
      
      
      
      


        
        
