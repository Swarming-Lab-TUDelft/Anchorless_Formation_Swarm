import tkinter as tk
from tkinter import ttk

import leader_follower

window_width = 1000
window_height = 600

class SimpleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI")
        self.root.geometry(f"{window_width}x{window_height}")

        # Create a label
        self.label = ttk.Label(self.root, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        self.entry_dx = ttk.Entry(self.root, textvariable=tk.DoubleVar(value=0))
        self.entry_dx.pack(padx = 100, pady= 10)

        self.entry_dy = ttk.Entry(self.root, textvariable=tk.DoubleVar(value=0))
        self.entry_dy.pack(padx = 100, pady= 20)

        self.entry_dz = ttk.Entry(self.root, textvariable=tk.DoubleVar(value=0))
        self.entry_dz.pack(padx = 100, pady= 20)


        # Set formation button
        self.button_setFormation = ttk.Button(self.root, text="Set Formation", command=self.setFormation)
        self.button_setFormation.pack(pady=10)

    def setFormation(self):
        dx = float(self.entry_dx.get());
        dy = float(self.entry_dy.get());
        dz = float(self.entry_dz.get());

        print(f'Setting formation to {dx}, {dy}, {dz}');
        leader_follower.streamFormation(dx, dy, dz);

def main():
    # Define parameters
    
  

    # Initialize Tkinter
    root = tk.Tk()

    # Create the application
    app = SimpleGUI(root)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
