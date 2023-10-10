import tkinter as tk
from src.Controllers.delete_motorcycle_page_controller import *

class Delete_Motorcycle_Page(tk.Frame):
   def __init__(self, parent, controller):
      tk.Frame.__init__(self, parent)
      self.controller = controller
      label = tk.Label(self, text='Delete Motorcycle', font=controller.title_font)
      label.pack(side="top", fill="x", pady=50, padx=50)

        #list view showing all motorcycles
      listbox = tk.Listbox(self, width=40, height=10, font=('Helvetica', 17))
      
        #shift down
      bikenums = {}
      def populate_bikes():
            #clear listbox
            listbox.delete(0, tk.END)
            bikes = find_all_bikes()
            if bikes != -1 and bikes != None and bikes != []:
                for item in bikes:
                        listbox.insert(tk.END, f'{item["Year"]} {item["Make"]} {item["Model"]}')
                        bikenums[f'{item["Year"]} {item["Make"]} {item["Model"]}'] = item["BikeNum"]
            listbox.pack()
        #refresh button
      refresh_button = tk.Button(self, text='Refresh', command=populate_bikes)
        #place towards the right hand side of the list below
      refresh_button.pack()
      populate_bikes()
      #select and delete a bike
      def delete_a_bike():
         #get selected motorcycle
         selected = listbox.get(listbox.curselection())
         #get bike number from selected motorcycle
         bike_num = bikenums[selected]
         #delete bike
         delete_bike(bike_num)
         #refresh list
         populate_bikes()
      delete_button = tk.Button(self, text='Delete', command=delete_a_bike)
      delete_button.pack()
        #back button
      button = tk.Button(self, text="Back", command=lambda: controller.show_frame("StartPage"))
      button.pack()