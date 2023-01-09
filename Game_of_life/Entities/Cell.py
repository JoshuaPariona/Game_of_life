
class Cell():
    def __init__(self,row:int,columm:int,status:str) -> None:
        self.pos_row = row
        self.pos_columm = columm
        self.status = status
        self.next_status = None
    
    def to_revive(self):
        self.status = "alive"

    def kill(self):
        self.status = "dead"

    def to_next(self, next_status):
        self.next_status = next_status

    def commit_status(self):
        self.status = self.next_status

    def show_cell(self):
        if self.status == "alive":
            return "\u25A0"
        elif self.status == "dead":
            return "\u25A1"
        else:
            return "\u25A1"
    
    def get_status(self):
        return self.status
        
    def get_position(self):
        return (self.pos_row,self.pos_columm)