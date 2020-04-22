from tkinter import *

mWindow = Tk()


lisGrid = []

for i in range(1, 10):
    for j in range(1, 10):
#        Label(mWindow, text=" ", height = "3", width="6", borderwidth=1, font=("Courier", 16), relief='solid').grid(row=i, column=j)
#        num = StringVar()
        lisGrid.append(Entry(mWindow, textvariable=StringVar(), relief="solid", width='2', font=("Courier", 30)).grid(row=i, column=j))

"""
        grid[i-1][j-1] = StringVar()
        Entry(mWindow, textvariable=grid[i-1][j-1] ,relief="solid", width='2', font=("Courier", 30)).grid(row=i, column=j)
"""

def update():
    global lisGrid
    sGrid = [[[] for e in range(9)] for f in range(9)]
    for i in range(9):
        for j in range(9):
            try:
                if int(lisGrid[i*10+j].get()) < 1 or int(lisGrid[i+10+j].get()) > 9:
                    print("Error")
                    pass
                else:
                    sGrid[i][j] = [int(lisGrid[i*10+j].get())]
            except:
                sGrid[i][j] = [1,2,3,4,5,6,7,8,9]
    print(sGrid)
    return sGrid

# temp = [[None, None, None, None, 4, 9, 2, None, None], [None, None, None, None, 3, None, None, 8, None], [None, None, None, 8, 2, None, None, 1, 3], [None, 1, 5, None, None, 2, 3, None, None], [None, 6, None, 1, 8, None, None, None, 9], [None, None, None, None, 7, 4, None, 6, 1], [1, None, None, 4, None, 6, None, 3, None], [None, 9, None, 2, None, None, None, 4, None], [None, 8, None, None, None, 3, None, None, None]03


def solve(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] in [1,2,3,4,5,6,7,8,9]:
                pass
            else:
                pass



buttonUpdate = Button(mWindow, text="Update", command=update).grid(row=10, column=10)


mWindow.geometry("720x540")
mWindow.title("Sudoku Solver v1.0")

mWindow.mainloop()
