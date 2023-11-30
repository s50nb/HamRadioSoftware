import tkinter as tk


class MyGUI:
    
    def __init__(self):
        
        self.root = tk.Tk()
        
        self.root.title("Coax stub filter cal.")
       
        self.L1 = tk.Label(self.root, text = "Coax stub filter calculator", font = ('Ariel', 15))
        self.L1.pack(pady=20,padx=50)
        
        self.L2 = tk.Label(self.root, text = "Frequency (Mhz): ", font = ('Ariel', 10))
        self.L2.pack(pady=10)
        
        self.E1 = tk.Entry(self.root)
        self.E1.pack(pady=5)
        
        self.L3 = tk.Label(self.root, text = "Coax velocity factor", font = ('Ariel', 10))
        self.L3.pack(pady=10)
        
        self.E2 = tk.Entry(self.root)
        self.E2.pack(pady=5)
        
        self.B1 = tk.Button(self.root, text = "Calculate", font = ('Ariel', 8), command = self.calculate)
        self.B1.pack(pady=10)
        
        self.L5 = tk.Label(self.root, text = "Coax stub lenght:", font = ('Ariel', 10))
        self.L5.pack(pady=5)
        
        self.L4 = tk.Label(self.root, text ="", font = ('Ariel', 10))
        self.L4.pack(pady= 5)
        
        self.root.mainloop()

    def calculate(self):
        Ve = float(299.792458)
        Lc = (float(Ve) / float(self.E1.get()) / 4 ) * float(self.E2.get())
        lim_Lc = round(Lc,4)
        self.L4.config(text = (round(lim_Lc * 1000,4),"mm"))
        
    
MyGUI()
