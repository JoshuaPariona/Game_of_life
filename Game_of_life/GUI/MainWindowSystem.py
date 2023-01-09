import tkinter as tk
from Entities.Cell import Cell

class CellCeld(tk.Button):
    def __init__(self, master, cell: Cell):
        tk.Button.__init__(self, master)
        self.master = master
        self["command"] = self.switch_status
        self.is_on = True
        self.cell = cell
        self.id_after : str
        self.switch_status()

    def switch_status(self):
        if self.is_on:
            self["bg"] = "#FFFFFF"
            self.cell.kill()
            self.is_on = False
        else:
            self["bg"] = "#000000"
            self.cell.to_revive()
            self.is_on = True
    
    def update_CellCeld(self):
        if self.cell.get_status() == "alive":
            self["bg"] = "#000000"
        elif self.cell.get_status() == "dead":
            self["bg"] = "#FFFFFF"

    def reset(self):
        self.is_on=True
        self.switch_status()

    def get_cell(self):
        return self.cell

    
    
class MainWindowSystem(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Game of life")
        self.geometry("1000x600")
        self.resizable(0,0)
        self.table : list[list[CellCeld]]
        self.table = []
        self.first = True
        self.disable = False
        self.colocar_botones()
        self.colocar_celulas()
    
    def colocar_botones(self):
        Button_inicio= tk.Button(self)
        Button_inicio["justify"] = "center"
        Button_inicio["text"] = "Iniciar"
        Button_inicio.place(x=50,y=580, width=50,height=20)
        Button_inicio["command"] = self.iniciar

        Button_pausa= tk.Button(self)
        Button_pausa["justify"] = "center"
        Button_pausa["text"] = "Pausa"
        Button_pausa.place(x=500,y=580, width=50,height=20)
        Button_pausa["command"] = self.pausa

        Button_reset= tk.Button(self)
        Button_reset["justify"] = "center"
        Button_reset["text"] = "Limpiar"
        Button_reset.place(x=900,y=580, width=50,height=20)
        Button_reset["command"] = self.reset
    
    def run(self):
        if self.first:
            print("In run")
            self.first = False
        for list_cell in self.table:
            for cell_celd in list_cell:
                cell = cell_celd.get_cell()
                status = cell.get_status()
                row,columm = cell.get_position()
                new_status = self.check_around(status,row,columm)
                if new_status == "alive":
                    cell.to_next("alive")
                elif new_status == "dead":
                    cell.to_next("dead")
        for list_cell in self.table:
            for cell_celd in list_cell:
                cell = cell_celd.get_cell()
                cell.commit_status()
                cell_celd.update_CellCeld()
        self.id_after = self.after(1000,self.run)

    def iniciar(self):
        if not self.disable:
            self.disable = True
            self.run()
            
    def check_around(self, cell_status, cell_row, cell_columm):
        if cell_status == "alive":
            count =self.count_around(cell_row, cell_columm)
            if count == 2 or count == 3:
                return "alive"
            else:
                return "dead"
        elif cell_status == "dead":
            count =self.count_around(cell_row, cell_columm)
            if count == 3:
                return "alive"
            else:
                return "dead"

    def count_around(self,cell_row,cell_columm):
        #alive cells
        count = 0
        if self.is_neighbor(cell_row-1,cell_columm-1):
            count += 1
        if self.is_neighbor(cell_row,cell_columm-1): 
            count += 1
        if self.is_neighbor(cell_row+1,cell_columm-1):
            count += 1

        if self.is_neighbor(cell_row-1,cell_columm):
            count += 1
        if self.is_neighbor(cell_row+1,cell_columm):
            count += 1
        
        if self.is_neighbor(cell_row-1,cell_columm+1):
            count += 1
        if self.is_neighbor(cell_row,cell_columm+1):
            count += 1
        if self.is_neighbor(cell_row+1,cell_columm+1):
            count += 1
        return count

    def is_neighbor(self,cell_row,cell_columm):
        try:
            cell:Cell
            cell_celd = self.table[cell_row][cell_columm] 
            cell = cell_celd.get_cell()
            if (cell.get_status()=="alive"):
                return True 
            else:
                return False
        except:
            return False
    
    def pausa(self):
        self.after_cancel(self.id_after)
        self.disable = False
        self.first=True
        print("In pause")
    
    def reset(self):
        self.pausa()
        for i in range(22):
            for j in range(58):
                self.table[i][j].reset()
        print("Reset table")

    def colocar_celulas(self):
        for i in range(22):
            row=[]
            for j in range(58):
                cell = Cell(i,j,"dead")
                cell_celd = CellCeld(self,cell)
                cell_celd.config(width=1,height=1)
                cell_celd.grid(row=i,column=j)
                row.append(cell_celd)
            self.table.append(row)