from Entities.Board import Board
from GUI.MainWindowSystem import MainWindowSystem



#Terminal program
"""b = Board(45,30)
b.new_table()

print("Ingrese su arreglo de puntos iniciales")

opt = "C"
while opt == "C":
    row = int(input("fila: "))
    columm = int(input("columna: "))
    b.put_cell((row-1),(columm-1))
    opt=input("F to finish, C to continue: ")

input("Ingrese cualquier tecla para empezar juego")

b.run()"""

#TK interface program

m = MainWindowSystem()
print("Plant a seed")
m.mainloop()