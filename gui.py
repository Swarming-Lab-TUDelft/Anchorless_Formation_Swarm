import tkinter as tk
from tkinter import ttk

import time
import leader_follower
from visualisation import visualiseFormation

window_width = 950
window_height = 580


dark1 = "#17181a"
dark2 = "#202123"
dark3 = "#202123"

text_white = "#f7f7f7"
text_green = "#379c7c"
text_red = "#c05646"
text_grey = "#494a4c"
text_light_grey = "#d0d0d0"

grey_line = "#333436"
bar_grey = "#494a4c"
bar_green = "#02b075"
bar_red = "#e61102"
card_hover = "#333436"

button_colors = {
    "green": ("#02B075", "#029665", "#02E398", "#016343"),
    "red": ("#E61102", "#CC1002", "#EA5348", "#990C02"),
    "grey": ("#494A4C", "#3D3E40", "#5A5A63", "#313233"),
    "purple": ("#702A8C", "#5E2679", "#8A51B1", "#4B1A64"),
    "blue": ("#0B85FF", "#0A71D8", "#3E9CEB", "#0963AB"),
    "yellow": ("#FFC107", "#D4A006", "#FFD453", "#B78B05"),
    "orange": ("#FF6D00", "#DD5F00", "#FF8A3B", "#AC4E00"),
    "green2": ("#4CAF50", "#43A047", "#66BB6A", "#388E3C")
}


x_entries = 470
y_entries = 20






class Window(tk.Tk):
    def __init__(self, name):
        super().__init__()
        self.title(name)
        self.geometry(f"{window_width}x{window_height}")

        self.configure(cursor="left_ptr", bg=dark2)

        style = ttk.Style()
        style.configure('Custom.TButton', background=button_colors['green'][0], foreground='white', font=("Arial", 14, 'bold'))

        self.n_drones = 2
        self.flashing = False


        self.dx = [0.0, 0.0, 1.0, -1.0, 0.0]; self.dy = [0.0, 0.0, 0.0, 0.0, 1.0]; self.dz = [1.0, -1.0, 0.0, 0.0, 0.0]

        self.dx1_var = tk.StringVar();          self.dx1_var.set(self.dx[0]);
        self.dy1_var = tk.StringVar();          self.dy1_var.set(self.dy[0]);          
        self.dz1_var = tk.StringVar();          self.dz1_var.set(self.dz[0]);

        self.dx2_var = tk.StringVar();          self.dx2_var.set(self.dx[1]);   
        self.dy2_var = tk.StringVar();          self.dy2_var.set(self.dy[1]);        
        self.dz2_var = tk.StringVar();          self.dz2_var.set(self.dz[1]);        

        self.dx3_var = tk.StringVar();          self.dx3_var.set(self.dx[2]);        
        self.dy3_var = tk.StringVar();          self.dy3_var.set(self.dy[2]);         
        self.dz3_var = tk.StringVar();          self.dz3_var.set(self.dz[2]);          

        self.dx4_var = tk.StringVar();          self.dx4_var.set(self.dx[3]);   
        self.dy4_var = tk.StringVar();          self.dy4_var.set(self.dy[3]);   
        self.dz4_var = tk.StringVar();          self.dz4_var.set(self.dz[3]);   

        self.dx5_var = tk.StringVar();          self.dx5_var.set(self.dx[4]);   
        self.dy5_var = tk.StringVar();          self.dy5_var.set(self.dy[4]);  
        self.dz5_var = tk.StringVar();          self.dz5_var.set(self.dz[4]);

        self.bind('<Escape>', self.on_escape)
        self.bind('<Return>', self.changeFormation)

        self.drawWindow()


        # style = ttk.Style()
        # style.configure('Front.TFrame', background=dark2)
        # style.configure('Back.TFrame', background=dark1)
        # style.configure('Card.TFrame', background=dark3)
        # style.configure('TLabel', font=('Roboto', 11), foreground=text_white, background=dark2)
        # style.configure('grey.TLabel', font=('Roboto', 11), foreground=text_grey, background=dark2)
        # style.configure('Header.TLabel', font=('Roboto', 11, 'bold'), foreground=text_white, background=dark1)
        # style.configure('TButton', font=('Roboto', 10), foreground=text_white, background=dark2)
        # style.configure('green.TButton', font=('Roboto', 10), foreground=text_white, background=bar_green)
        # style.configure('red.TButton', font=('Roboto', 10), foreground=text_white, background="#ff463a")
        # style.configure('separator.TFrame', background=grey_line)
        # style.configure('bar_grey.TFrame', background=bar_grey)
        # style.configure('bar_green.TFrame', background=bar_green)





        

    def drawWindow(self):
        

        for widget in self.winfo_children():
            widget.destroy()

        ##################################   DRONE 1  ###################################################



        self.label_offset1 = ttk.Label(self, text="Offset Drone 2:", background=dark2, foreground='white')
        self.label_offset1.place(x = x_entries, y = y_entries+2)

        # dx1
        self.label_dx1 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
        self.label_dx1.place(x = x_entries + 150, y = y_entries+2)

        self.entry_dx1 = ttk.Entry(self, textvariable=self.dx1_var, background=dark2, foreground=dark1, width=20)
        self.entry_dx1.place(x = x_entries + 180, y = y_entries, width=30)
        self.entry_dx1.bind('<FocusOut>', self.changeFormation)

        self.label_mx1 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mx1.place(x = x_entries + 215, y = y_entries+2)

        #dy1
        self.label_dy1 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
        self.label_dy1.place(x = x_entries + 260, y = y_entries+2)

        self.entry_dy1 = ttk.Entry(self, textvariable=self.dy1_var, background=dark2, foreground=dark1, width=20)
        self.entry_dy1.place(x = x_entries + 290, y = y_entries, width=30)
        self.entry_dy1.bind('<FocusOut>', self.changeFormation)

        self.label_my1 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_my1.place(x = x_entries + 325, y = y_entries+2)

        #dz1
        self.label_dz1 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
        self.label_dz1.place(x = x_entries + 370, y = y_entries+2)

        self.entry_dz1 = ttk.Entry(self, textvariable=self.dz1_var, background=dark2, foreground=dark1, width=20)
        self.entry_dz1.place(x = x_entries + 400, y = y_entries, width=30)
        self.entry_dz1.bind('<FocusOut>', self.changeFormation)


        self.label_mz1 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mz1.place(x = x_entries + 435, y = y_entries+2)




        ##################################   DRONE 2  ###################################################
        if self.n_drones >= 3:

            self.label_offset2 = ttk.Label(self, text="Offset Drone 3:", background=dark2, foreground='white')
            self.label_offset2.place(x = x_entries, y = y_entries+2 + 50)

            # dx2
            self.label_dx2 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
            self.label_dx2.place(x = x_entries + 150, y = y_entries+2 + 50)

            self.entry_dx2 = ttk.Entry(self, textvariable=self.dx2_var, background=dark2, foreground=dark1, width=20)
            self.entry_dx2.place(x = x_entries + 180, y = y_entries + 50, width=30)
            self.entry_dx2.bind('<FocusOut>', self.changeFormation)

            self.label_mx2 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mx2.place(x = x_entries + 215, y = y_entries+2 + 50)

            #dy2
            self.label_dy2 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
            self.label_dy2.place(x = x_entries + 260, y = y_entries+2 + 50)

            self.entry_dy2 = ttk.Entry(self, textvariable=self.dy2_var, background=dark2, foreground=dark1, width=20)
            self.entry_dy2.place(x = x_entries + 290, y = y_entries + 50, width=30)
            self.entry_dy2.bind('<FocusOut>', self.changeFormation)

            self.label_my2 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_my2.place(x = x_entries + 325, y = y_entries+2 + 50)

            #dz2
            self.label_dz2 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
            self.label_dz2.place(x = x_entries + 370, y = y_entries+2 + 50)

            self.entry_dz2 = ttk.Entry(self, textvariable=self.dz2_var, background=dark2, foreground=dark1, width=20)
            self.entry_dz2.place(x = x_entries + 400, y = y_entries + 50, width=30)
            self.entry_dz2.bind('<FocusOut>', self.changeFormation)


            self.label_mz2 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mz2.place(x = x_entries + 435, y = y_entries+2 + 50)





        ##################################   DRONE 3  ###################################################
        if self.n_drones >= 4:

            self.label_offset3 = ttk.Label(self, text="Offset Drone 4:", background=dark2, foreground='white')
            self.label_offset3.place(x = x_entries, y = y_entries+2 + 100)

            # dx2
            self.label_dx3 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
            self.label_dx3.place(x = x_entries + 150, y = y_entries+2 + 100)

            self.entry_dx3 = ttk.Entry(self, textvariable=self.dx3_var, background=dark2, foreground=dark1, width=20)
            self.entry_dx3.place(x = x_entries + 180, y = y_entries + 100, width=30)
            self.entry_dx3.bind('<FocusOut>', self.changeFormation)

            self.label_mx3 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mx3.place(x = x_entries + 215, y = y_entries+2 + 100)

            #dy2
            self.label_dy3 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
            self.label_dy3.place(x = x_entries + 260, y = y_entries+2 + 100)

            self.entry_dy3 = ttk.Entry(self, textvariable=self.dy3_var, background=dark2, foreground=dark1, width=20)
            self.entry_dy3.place(x = x_entries + 290, y = y_entries + 100, width=30)
            self.entry_dy3.bind('<FocusOut>', self.changeFormation)

            self.label_my3 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_my3.place(x = x_entries + 325, y = y_entries+2 + 100)

            #dz2
            self.label_dz3 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
            self.label_dz3.place(x = x_entries + 370, y = y_entries+2 + 100)

            self.entry_dz3 = ttk.Entry(self, textvariable=self.dz3_var, background=dark2, foreground=dark1, width=20)
            self.entry_dz3.place(x = x_entries + 400, y = y_entries + 100, width=30)
            self.entry_dz3.bind('<FocusOut>', self.changeFormation)


            self.label_mz3 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mz3.place(x = x_entries + 435, y = y_entries+2 + 100)




##################################   DRONE 4  ###################################################

        if self.n_drones >= 5:

            self.label_offset4 = ttk.Label(self, text="Offset Drone 5:", background=dark2, foreground='white')
            self.label_offset4.place(x = x_entries, y = y_entries+2 + 150)

            # dx2
            self.label_dx4 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
            self.label_dx4.place(x = x_entries + 150, y = y_entries+2 + 150)

            self.entry_dx4 = ttk.Entry(self, textvariable=self.dx4_var, background=dark2, foreground=dark1, width=20)
            self.entry_dx4.place(x = x_entries + 180, y = y_entries + 150, width=30)
            self.entry_dx4.bind('<FocusOut>', self.changeFormation)


            self.label_mx4 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mx4.place(x = x_entries + 215, y = y_entries+2 + 150)

            #dy2
            self.label_dy4 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
            self.label_dy4.place(x = x_entries + 260, y = y_entries+2 + 150)

            self.entry_dy4 = ttk.Entry(self, textvariable=self.dy4_var, background=dark2, foreground=dark1, width=20)
            self.entry_dy4.place(x = x_entries + 290, y = y_entries + 150, width=30)
            self.entry_dy4.bind('<FocusOut>', self.changeFormation)

            self.label_my4 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_my4.place(x = x_entries + 325, y = y_entries+2 + 150)

            #dz2
            self.label_dz4 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
            self.label_dz4.place(x = x_entries + 370, y = y_entries+2 + 150)

            self.entry_dz4 = ttk.Entry(self, textvariable=self.dz4_var, background=dark2, foreground=dark1, width=20)
            self.entry_dz4.place(x = x_entries + 400, y = y_entries + 150, width=30)
            self.entry_dz4.bind('<FocusOut>', self.changeFormation)

            self.label_mz4 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mz4.place(x = x_entries + 435, y = y_entries+2 + 150)




##################################   DRONE 5  ###################################################
        
        if self.n_drones >= 6:

            self.label_offset5 = ttk.Label(self, text="Offset Drone 6:", background=dark2, foreground='white')
            self.label_offset5.place(x = x_entries, y = y_entries+2 + 200)

            # dx2
            self.label_dx5 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
            self.label_dx5.place(x = x_entries + 150, y = y_entries+2 + 200)

            self.entry_dx5 = ttk.Entry(self, textvariable=self.dx5_var, background=dark2, foreground=dark1, width=20)
            self.entry_dx5.place(x = x_entries + 180, y = y_entries + 200, width=30)
            self.entry_dx5.bind('<FocusOut>', self.changeFormation)

            self.label_mx5 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mx5.place(x = x_entries + 215, y = y_entries+2 + 200)

            #dy2
            self.label_dy5 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
            self.label_dy5.place(x = x_entries + 260, y = y_entries+2 + 200)

            self.entry_dy5 = ttk.Entry(self, textvariable=self.dy5_var, background=dark2, foreground=dark1, width=20)
            self.entry_dy5.place(x = x_entries + 290, y = y_entries + 200, width=30)
            self.entry_dy5.bind('<FocusOut>', self.changeFormation)

            self.label_my5 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_my5.place(x = x_entries + 325, y = y_entries+2 + 200)

            #dz2
            self.label_dz5 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
            self.label_dz5.place(x = x_entries + 370, y = y_entries+2 + 200)

            self.entry_dz5 = ttk.Entry(self, textvariable=self.dz5_var, background=dark2, foreground=dark1, width=20)
            self.entry_dz5.place(x = x_entries + 400, y = y_entries + 200, width=30)
            self.entry_dz5.bind('<FocusOut>', self.changeFormation)

            self.label_mz5 = ttk.Label(self, text="m", background=dark2, foreground='white')
            self.label_mz5.place(x = x_entries + 435, y = y_entries+2 + 200)



        ############## REST  ##########

        self.label_ndrones = ttk.Label(self, text="Number of drones:", background=dark2, foreground='white', font=("Arial", 14))
        self.label_ndrones.place(x = 20, y = y_entries + 2)

        self.combobox_ndrones = ttk.Combobox(self, values=[*range(2, 7, 1)], state='readonly')
        self.combobox_ndrones.set(self.n_drones)
        self.combobox_ndrones.bind("<<ComboboxSelected>>", self.changeNumberDrones)
        self.combobox_ndrones.place(x = x_entries - 90, y = y_entries, width= 50)


        # Set formation button
        self.button_setFormation = ttk.Button(self, text="UPLOAD FORMATION", style='Custom.TButton', command=self.setFormation)
        self.button_setFormation.place(x = 20, y = y_entries + 470, width = x_entries - 60, height= 70)
        
        self.progressbar = ttk.Progressbar(self, orient="horizontal", length=300, mode="determinate")
        self.progressbar.place(x = x_entries, y = y_entries + 515, width= 450)
        self.progressbar['value'] = 0

        
        self.label_status = ttk.Label(self, text="Status: Specify Formation", background=dark2, foreground='white', font=("Arial", 24))
        self.label_status.place(x = x_entries, y = y_entries + 470)

        visualiseFormation(self, self.n_drones, self.dx, self.dy, self.dz)


   

    def changeNumberDrones(self, event):
        self.n_drones = int(self.combobox_ndrones.get())
        self.changeFormation()
        self.drawWindow()
        self.update()


    def changeFormation(self, event=None):
        self.dx[0] = float(self.dx1_var.get())
        self.dy[0]= float(self.dy1_var.get())
        self.dz[0] = float(self.dz1_var.get())
        self.dx[1] = float(self.dx2_var.get())
        self.dy[1] = float(self.dy2_var.get())
        self.dz[1] = float(self.dz2_var.get()) 
        self.dx[2] = float(self.dx3_var.get())
        self.dy[2] = float(self.dy3_var.get())
        self.dz[2] = float(self.dz3_var.get()) 
        self.dx[3] = float(self.dx4_var.get())
        self.dy[3] = float(self.dy4_var.get())
        self.dz[3] = float(self.dz4_var.get())
        self.dx[4] = float(self.dx5_var.get())
        self.dy[4] = float(self.dy5_var.get())
        self.dz[4] = float(self.dz5_var.get())
        visualiseFormation(self, self.n_drones, self.dx, self.dy, self.dz)


    def setFormation(self):
        self.changeFormation();
        self.label_status.configure(foreground ='yellow', text = "Status: Uploading...")
        self.update();
        success = True

        for i in range(self.n_drones-1):
                time.sleep(1.0)
                if leader_follower.streamFormation(i, self.dx[i], self.dy[i], self.dz[i]):
                    print(f"Drone {i+1}/{self.n_drones-1} updated.")
                else:
                    print(f'Update for Drone {i+2} failed.')
                    success = False
            
                self.progressbar.step(1 / (self.n_drones-1) * 99.9)
                self.update();
           
        self.progressbar['value'] = 0;
        if success:
            self.label_status.configure(foreground ="#02B075", text = "Status: Upload successful!")
        else:
            self.label_status.configure(foreground ="#E61102", text = "Status: Error during upload!")



    def on_escape(self, event):
        print('Window closed using Escape key.')
        self.quit();


#########################################################################
def main():
   app = Window("Anchorless Swarm Controller")
   app.protocol("WM_DELETE_WINDOW", app.quit)
   app.mainloop()


if __name__ == "__main__":
    main()
