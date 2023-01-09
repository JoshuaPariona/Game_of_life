from .Cell import Cell
import time

class Board():
    def __init__(self,width:int,height:int) -> None:
        self.table = list[list[Cell]]
        self.table = []
        self.width = width
        self.height = height

    def new_table(self):
        for i in range(self.height):
            row = []
            for j in range(self.width):
                cell = Cell(i,j,"dead")
                row.append(cell)
            self.table.append(row)

    def show_table(self):
        for row in self.table:
            for cell in row:
                cell: Cell
                print(cell.show_cell(),end="  ")
            print()

    def put_cell(self,row:int,columm:int):
        cell = Cell(row,columm,"alive")
        self.table[row][columm] = cell

    def is_neighbor(self,cell_row,cell_columm):
        try:
            cell:Cell
            cell = self.table[cell_row][cell_columm] 
            if (cell.get_status()=="alive"):
                return True 
        except:
            return False

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

    def run(self):
        gen = 0
        print("Seed")
        self.show_table()
        while gen < 10:
            temp_table = []
            for list_cell in self.table:
                temp_row_cells = []
                for cell in list_cell:
                    cell:Cell
                    status = cell.get_status()
                    row,columm = cell.get_position()
                    new_status = self.check_around(status,row,columm)
                    if new_status == "alive":
                        temp_cell = Cell(row,columm,"alive")
                        temp_row_cells.append(temp_cell)
                    elif new_status == "dead":
                        temp_cell = Cell(row,columm,"dead")
                        temp_row_cells.append(temp_cell)
                temp_table.append(temp_row_cells)
            self.table = temp_table
            time.sleep(1)
            print()
            gen+=1
            print("Generation",gen)
            self.show_table()