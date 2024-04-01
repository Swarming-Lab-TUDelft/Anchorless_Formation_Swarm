import tkinter as tk
from tkinter import ttk

import leader_follower
from visualisation import visualise

window_width = 1000
window_height = 600


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


x_entries = 300
y_entries = 20






class Window(tk.Tk):
    def __init__(self, name):
        super().__init__()
        self.title(name)
        self.geometry(f"{window_width}x{window_height}")

        self.configure(cursor="left_ptr", bg=dark2)

        dx1 = tk.StringVar()
        dy1 = tk.StringVar()
        dz1 = tk.StringVar()

        dx2 = tk.StringVar()
        dy2 = tk.StringVar()
        dz2 = tk.StringVar()

        dx3 = tk.StringVar()
        dy3 = tk.StringVar()
        dz3 = tk.StringVar()

        dx4 = tk.StringVar()
        dy4 = tk.StringVar()
        dz4 = tk.StringVar()

        dx5 = tk.StringVar()
        dy5 = tk.StringVar()
        dz5 = tk.StringVar()


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





        ##################################   DRONE 1  ###################################################



        self.label_offset1 = ttk.Label(self, text="Offset Drone 1:", background=dark2, foreground='white')
        self.label_offset1.place(x = x_entries, y = y_entries+2)

        # dx1
        self.label_dx1 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
        self.label_dx1.place(x = x_entries + 150, y = y_entries+2)

        self.entry_dx1 = ttk.Entry(self, textvariable=dx1, background=dark2, foreground=dark1, width=20)
        self.entry_dx1.place(x = x_entries + 180, y = y_entries, width=30)

        self.label_mx1 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mx1.place(x = x_entries + 215, y = y_entries+2)

        #dy1
        self.label_dy1 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
        self.label_dy1.place(x = x_entries + 260, y = y_entries+2)

        self.entry_dy1 = ttk.Entry(self, textvariable=dy1, background=dark2, foreground=dark1, width=20)
        self.entry_dy1.place(x = x_entries + 290, y = y_entries, width=30)

        self.label_my1 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_my1.place(x = x_entries + 325, y = y_entries+2)

        #dz1
        self.label_dz1 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
        self.label_dz1.place(x = x_entries + 370, y = y_entries+2)

        self.entry_dz1 = ttk.Entry(self, textvariable=dz1, background=dark2, foreground=dark1, width=20)
        self.entry_dz1.place(x = x_entries + 400, y = y_entries, width=30)

        self.label_mz1 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mz1.place(x = x_entries + 435, y = y_entries+2)




        ##################################   DRONE 2  ###################################################

        self.label_offset2 = ttk.Label(self, text="Offset Drone 2:", background=dark2, foreground='white')
        self.label_offset2.place(x = x_entries, y = y_entries+2 + 50)

        # dx2
        self.label_dx2 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
        self.label_dx2.place(x = x_entries + 150, y = y_entries+2 + 50)

        self.entry_dx2 = ttk.Entry(self, textvariable=dx2, background=dark2, foreground=dark1, width=20)
        self.entry_dx2.place(x = x_entries + 180, y = y_entries + 50, width=30)

        self.label_mx2 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mx2.place(x = x_entries + 215, y = y_entries+2 + 50)

        #dy2
        self.label_dy2 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
        self.label_dy2.place(x = x_entries + 260, y = y_entries+2 + 50)

        self.entry_dy2 = ttk.Entry(self, textvariable=dy2, background=dark2, foreground=dark1, width=20)
        self.entry_dy2.place(x = x_entries + 290, y = y_entries + 50, width=30)

        self.label_my2 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_my2.place(x = x_entries + 325, y = y_entries+2 + 50)

        #dz2
        self.label_dz2 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
        self.label_dz2.place(x = x_entries + 370, y = y_entries+2 + 50)

        self.entry_dz2 = ttk.Entry(self, textvariable=dz2, background=dark2, foreground=dark1, width=20)
        self.entry_dz2.place(x = x_entries + 400, y = y_entries + 50, width=30)

        self.label_mz2 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mz2.place(x = x_entries + 435, y = y_entries+2 + 50)





        ##################################   DRONE 3  ###################################################

        self.label_offset3 = ttk.Label(self, text="Offset Drone 3:", background=dark2, foreground='white')
        self.label_offset3.place(x = x_entries, y = y_entries+2 + 100)

        # dx2
        self.label_dx3 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
        self.label_dx3.place(x = x_entries + 150, y = y_entries+2 + 100)

        self.entry_dx3 = ttk.Entry(self, textvariable=dx3, background=dark2, foreground=dark1, width=20)
        self.entry_dx3.place(x = x_entries + 180, y = y_entries + 100, width=30)

        self.label_mx3 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mx3.place(x = x_entries + 215, y = y_entries+2 + 100)

        #dy2
        self.label_dy3 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
        self.label_dy3.place(x = x_entries + 260, y = y_entries+2 + 100)

        self.entry_dy3 = ttk.Entry(self, textvariable=dy3, background=dark2, foreground=dark1, width=20)
        self.entry_dy3.place(x = x_entries + 290, y = y_entries + 100, width=30)

        self.label_my3 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_my3.place(x = x_entries + 325, y = y_entries+2 + 100)

        #dz2
        self.label_dz3 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
        self.label_dz3.place(x = x_entries + 370, y = y_entries+2 + 100)

        self.entry_dz3 = ttk.Entry(self, textvariable=dz3, background=dark2, foreground=dark1, width=20)
        self.entry_dz3.place(x = x_entries + 400, y = y_entries + 100, width=30)

        self.label_mz3 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mz3.place(x = x_entries + 435, y = y_entries+2 + 100)




##################################   DRONE 4  ###################################################

        self.label_offset4 = ttk.Label(self, text="Offset Drone 4:", background=dark2, foreground='white')
        self.label_offset4.place(x = x_entries, y = y_entries+2 + 150)

        # dx2
        self.label_dx4 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
        self.label_dx4.place(x = x_entries + 150, y = y_entries+2 + 150)

        self.entry_dx4 = ttk.Entry(self, textvariable=dx4, background=dark2, foreground=dark1, width=20)
        self.entry_dx4.place(x = x_entries + 180, y = y_entries + 150, width=30)

        self.label_mx4 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mx4.place(x = x_entries + 215, y = y_entries+2 + 150)

        #dy2
        self.label_dy4 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
        self.label_dy4.place(x = x_entries + 260, y = y_entries+2 + 150)

        self.entry_dy4 = ttk.Entry(self, textvariable=dy4, background=dark2, foreground=dark1, width=20)
        self.entry_dy4.place(x = x_entries + 290, y = y_entries + 150, width=30)

        self.label_my4 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_my4.place(x = x_entries + 325, y = y_entries+2 + 150)

        #dz2
        self.label_dz4 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
        self.label_dz4.place(x = x_entries + 370, y = y_entries+2 + 150)

        self.entry_dz4 = ttk.Entry(self, textvariable=dz4, background=dark2, foreground=dark1, width=20)
        self.entry_dz4.place(x = x_entries + 400, y = y_entries + 150, width=30)

        self.label_mz4 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mz4.place(x = x_entries + 435, y = y_entries+2 + 150)




##################################   DRONE 5  ###################################################

        self.label_offset5 = ttk.Label(self, text="Offset Drone 5:", background=dark2, foreground='white')
        self.label_offset5.place(x = x_entries, y = y_entries+2 + 200)

        # dx2
        self.label_dx5 = ttk.Label(self, text="dx:", background=dark2, foreground='white')
        self.label_dx5.place(x = x_entries + 150, y = y_entries+2 + 200)

        self.entry_dx5 = ttk.Entry(self, textvariable=dx5, background=dark2, foreground=dark1, width=20)
        self.entry_dx5.place(x = x_entries + 180, y = y_entries + 200, width=30)

        self.label_mx5 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mx5.place(x = x_entries + 215, y = y_entries+2 + 200)

        #dy2
        self.label_dy5 = ttk.Label(self, text="dy:", background=dark2, foreground='white')
        self.label_dy5.place(x = x_entries + 260, y = y_entries+2 + 200)

        self.entry_dy5 = ttk.Entry(self, textvariable=dy5, background=dark2, foreground=dark1, width=20)
        self.entry_dy5.place(x = x_entries + 290, y = y_entries + 200, width=30)

        self.label_my5 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_my5.place(x = x_entries + 325, y = y_entries+2 + 200)

        #dz2
        self.label_dz5 = ttk.Label(self, text="dz:", background = dark2, foreground='white')
        self.label_dz5.place(x = x_entries + 370, y = y_entries+2 + 200)

        self.entry_dz5 = ttk.Entry(self, textvariable=dz5, background=dark2, foreground=dark1, width=20)
        self.entry_dz5.place(x = x_entries + 400, y = y_entries + 200, width=30)

        self.label_mz5 = ttk.Label(self, text="m", background=dark2, foreground='white')
        self.label_mz5.place(x = x_entries + 435, y = y_entries+2 + 200)





        # Set formation button
        # self.button_setFormation = ttk.Button(self, text="Set Formation", command=self.setFormation)
        # self.button_setFormation.pack(pady=10)




    def setFormation(self):
        # dx = float(self.entry_dx.get());
        # dy = float(self.entry_dy.get());
        # dz = float(self.entry_dz.get());

        # print(f'Setting formation to {dx}, {dy}, {dz}');
        # leader_follower.streamFormation(dx, dy, dz);
        visualise(self)
        print('Visualise function finished')





#########################################################################
def main():
   app = Window("Anchorless Swarm Controller")
   app.protocol("WM_DELETE_WINDOW", app.destroy)
   app.mainloop()


if __name__ == "__main__":
    main()
