#!/usr/bin/python3 

import subprocess
import os

class screen(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
       
        # All workspaces and their data
        desk_output = subprocess.getoutput("wmctrl -d").split("\n")
        # All workspace numbers
        desk_list = [line.split()[0] for line in desk_output]

        # Data about current desktop. Not sure how it works with multiple.
        current = [line for line in desk_output if line.split()[1] == "*"][0].split()

        self.desktop = current[0]
        self.width, self.height = map(int, current[8].split('x'))
        self.orig_x, self.orig_y = current[7].split(',')

        row_division = self.height // self.rows
        col_division = self.width // self.cols


        self.grid = []
        for rownum in range(rows):
            row = []
            for colnum in range(cols):
                col = []
                col.append((col_division*colnum, col_division*(colnum+1))) 
                col.append((row_division*rownum, row_division*(rownum+1))) 
                row.append(col)
            self.grid.append(row)
       
        
        #Grid format is something like this:
        #[[(0, 640), (0, 522)],    [(640, 1280), (0, 522)],    [(1280, 1920), (0, 522)]],
        #[[(0, 640), (522, 1044)], [(640, 1280), (522, 1044)], [(1280, 1920), (522, 1044)]]

        for i in self.grid:
            print(i)

    def get_coords(self, cols, rows):
        """Precondition: two two-tuples of (start,end) for rows and columns."""
        row_start, row_end = rows
        col_start, col_end = cols

        x_start_coord = self.grid[0][col_start-1][0][0]
        x_end_coord =   self.grid[0][col_end - 1][0][1]
        x_coords = (x_start_coord, x_end_coord)
        
        y_start_coord = self.grid[row_start-1][0][1][0]
        y_end_coord =   self.grid[row_end - 1][0][1][1]
        y_coords = (y_start_coord, y_end_coord)


        x = x_coords[0]
        y = y_coords[0]
        w = y_coords[1] - y_coords[0]
        h = x_coords[1] - x_coords[0]


        return (x, y, w, h)

    def move_active(self,x,y,w,h):
        command = ','.join(map(str, [" wmctrl -r :ACTIVE: -e 0", x, y, w, h]))
        print(command)
        os.system(command)



if __name__ == "__main__":
    s = screen(2,2)
    c = s.get_coords((2,2), (2,2))
    print(c)
    s.move_active(c[0],c[1],c[3],c[2])
