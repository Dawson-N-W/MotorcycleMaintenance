import tkinter as tk
import tkinter.ttk as ttk
from src.Controllers.maintenance_page_controller import *



class Maintenance_Page(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Motorcycle Maintenance', font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

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
        #retrieve specs
        specbox = tk.Text(self, width=40, height=5, font=('Helvetica', 17), wrap=tk.WORD)
        specbox.insert(tk.END, f'Engine Type: NA\n')
        specbox.insert(tk.END, f'Engine Size: NA\n')
        specbox.insert(tk.END, f'Horsepower: NA\n')
        specbox.insert(tk.END, f'Torque: NA\n')
        specbox.insert(tk.END, f'Mileage: NA\n')
        specbox.pack()
        specbox.config(state=tk.DISABLED)

        def specs():
         specbox.config(state=tk.NORMAL)
         #remove previous specs
         specbox.delete(1.0, tk.END)
         #get selected motorcycle
         selected = listbox.get(listbox.curselection())
         #get bike number from selected motorcycle
         bike_num = bikenums[selected]
         #get specs of bike
         bike = find_bike(bike_num)
         
         if bike != -1 and bike != None and bike != []:
            specbox.insert(tk.END, f'Engine Type: {bike["EngineType"]}\n')
            specbox.insert(tk.END, f'Engine Size: {str(bike["CC"])}cc\n')
            specbox.insert(tk.END, f'Horsepower: {str(bike["Horsepower"])}hp\n')
            specbox.insert(tk.END, f'Torque: {str(bike["Torque"])}ft-lbs\n')
            specbox.insert(tk.END, f'Mileage: {str(bike["Mileage"])}\n')
            
            specbox.config(state=tk.DISABLED)
         else:
            error_label = tk.Label(self, text='Error finding motorcycle.', fg='red')
            error_label.pack()
            error_label.after(2000, lambda: error_label.destroy())
            return
        spec_button = tk.Button(self, text='Retrieve Specs', command=specs)
        spec_button.pack()
         #entry fields for new motorcycle
        check_1 = tk.IntVar()
        check_2 = tk.IntVar()
        check_3 = tk.IntVar()
        check_4 = tk.IntVar()
        check_5 = tk.IntVar()
        check_6 = tk.IntVar()
        check_7 = tk.IntVar()
        check_8 = tk.IntVar()
        check_9 = tk.IntVar() 

        #check box for maintenance
        maintenance_label = tk.Label(self, text='Maintenance List:', font = ('Helvetica', 17))
        maintenance_label.pack()
        c1 = tk.Checkbutton(self, text='Oil Change', variable=check_1)
        c1.pack(anchor='w')
        c2 = tk.Checkbutton(self, text='Oil Filter', variable=check_2)
        c2.pack(anchor='w')
        c3 = tk.Checkbutton(self, text='Transmission Oil', variable=check_3)
        c3.pack(anchor='w')
        c4 = tk.Checkbutton(self, text='Air Filter', variable=check_4)
        c4.pack(anchor='w')
        c5 = tk.Checkbutton(self, text='Spark Plugs', variable=check_5)
        c5.pack(anchor='w')
        c6 = tk.Checkbutton(self, text='Chain', variable=check_6)
        c6.pack(anchor='w')
        c7 = tk.Checkbutton(self, text='Tires', variable=check_7)
        c7.pack(anchor='w')
        c8 = tk.Checkbutton(self, text='Brakes', variable=check_8)
        c8.pack(anchor='w')
        c9 = tk.Checkbutton(self, text='Brake Fluid', variable=check_9)
        c9.pack(anchor='w')
      
        #select motorcycle from list box
        def select_motorcycle():
            deselect()
            #get selected motorcycle
            selected = listbox.get(listbox.curselection())
            #get bike number from selected motorcycle
            bike_num = bikenums[selected]
            #pass bike number to find_all_maintenance
            maintenance = find_all_maintenance(bike_num)
            #display maintenance in listbox
            if maintenance != -1 and maintenance != None and maintenance != []:
               for item in maintenance:
                  if item["Oil"] == 1:
                     c1.select()
                  if item["OilFilter"] == 1:
                     c2.select()
                  if item["TranOil"] == 1:
                     c3.select()
                  if item["AirFilter"] == 1:
                     c4.select()
                  if item["SparkPlug"] == 1:
                     c5.select()
                  if item["Chain"] == 1:
                     c6.select()
                  if item["Tires"] == 1:
                     c7.select()
                  if item["Brakes"] == 1:
                     c8.select()
                  if item["BrakeFluid"] == 1:
                     c9.select()
                  success_label = tk.Label(self, text='Maintenance populated successfully!', fg='green')
                  success_label.pack()
                  success_label.after(2000, lambda: success_label.destroy())
                  return
            else:
               error_label = tk.Label(self, text='Error finding maintenance record.', fg='red')
               error_label.pack()
               error_label.after(2000, lambda: error_label.destroy())
               return
         
            #button to select motorcycle
        select_button = tk.Button(self, text='Retrieve Existing Maintenance Record', command=select_motorcycle)
        select_button.pack()

        #create new maintenance record
        def submit_data():
            #get selected motorcycle
            selected = listbox.get(listbox.curselection())
            #get bike number from selected motorcycle
            bike_num = bikenums[selected]
            #get maintenance data
            oil = check_1.get()
            oil_filter = check_2.get()
            tran_oil = check_3.get()
            air_filter = check_4.get()
            spark_plug = check_5.get()
            chain = check_6.get()
            tires = check_7.get()
            brakes = check_8.get()
            brake_fluid = check_9.get()
            
            #pass bike number and maintenance object to add_maintenance
            if add_maintenance(bike_num, oil, oil_filter, tran_oil, air_filter, spark_plug, chain, tires, brakes, brake_fluid ) == -1:
               error_label = tk.Label(self, text='Error adding maintenance record.', fg='red')
               error_label.pack()
               error_label.after(2000, lambda: error_label.destroy())
               return
            #display success message
            success_label = tk.Label(self, text='Maintenance added successfully!', fg='green')
            success_label.pack()
            success_label.after(2000, lambda: success_label.destroy())
            #clear check boxes
            deselect()
            
        def deselect():
         c1.deselect()
         c2.deselect()
         c3.deselect()
         c4.deselect()
         c5.deselect()
         c6.deselect()
         c7.deselect()
         c8.deselect()
         c9.deselect()
            
        submit = tk.Button(self, text='Create New Maintenance Record', command=submit_data)
        submit.pack()

        #button to return to start page
        button = tk.Button(self, text="Return to Start Page", command=lambda: controller.show_frame("StartPage"))
        button.pack()

        
        
      
               

      

