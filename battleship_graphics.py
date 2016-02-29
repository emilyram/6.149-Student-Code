# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 01:33:14 2016

@author: sylvant
"""
from graphics import *

# constants uesd in drawing the game board
SIZE = 50
UNATTACKED_COLOR = "#FFFFFF"
ATTACKED_COLOR = "#DDDDDD"
HIT_COLOR = "#FF0000"  
MINED_COLOR = "#000000"  

class GraphicsBoard(object):                
    def __init__(self, board):
        """
        Initializes the graphics used to draw the board
        
        Inputs: board (Board), the Board we are depicting
        
        Attributes: self.board (Board), the Board we are depicting
                    self.num_cols (int), the number of columns we will draw,
                                         which is the same as what self.board 
                                         has
                    self.num_rows (int), the number of rows we will draw, which
                                         is the same as what self.board has
                    self.graphics (dict), maps tuple of ints (col, row) to the
                                          corresponding Rectangle graphics
                                          object we are drawing
        
        Returns: nothing
        """
        
        # save board and pull number of cols/rows from it
        self.board = board
        self.num_cols = board.get_num_cols()
        self.num_rows = board.get_num_rows()
        
        # initialize our graphics window
        self.win = GraphWin(width=self.num_cols*SIZE, height=self.num_rows*SIZE)
        
        # initialize our graphics dictionary
        # each square at (col, row) will be drawn with a Rectangle
        self.graphics = {}              
        for x in range(self.num_cols):
            for y in range(self.num_rows):
                r = Rectangle(Point(x*SIZE, y*SIZE),
                              Point((x+1)*SIZE, (y+1)*SIZE))
                self.graphics[(x, y)] = r
                
                # draws a white square, representing an unattacked position
                r.setFill(UNATTACKED_COLOR)
                r.draw(self.win)
    
    def redraw(self):
        """
        Updates our visual representation of the board when a Square is attacked
        
        Inputs: none
        
        Returns: nothing
        """
        board_squares = self.board.get_squares()
        for (col, row) in board_squares:
            if board_squares[(col, row)].get_is_attacked():
                if board_squares[(col, row)].contains_ship():
                    self.graphics[(col, row)].setFill(HIT_COLOR)
                elif board_squares[(col, row)].get_is_mined():
                    self.graphics[(col, row)].setFill(MINED_COLOR)
                else:
                    self.graphics[(col, row)].setFill(ATTACKED_COLOR)
    
    def play(self):
        """
        Controls the game play.
        When the user attacks a square by clicking on it, we use the
        coordinates of their mouse to compute the corresponding column/row
        of the Square and update the Board accordingly. Then, we update
        the visual representation of the Board. This continues until we
        have sunk all of the ships on the Board.
        
        Inputs: none
        
        Returns: nothing
        """
        
        while not self.board.all_ships_sunk():
            # get where user clicked and compute col/row
            m = self.win.getMouse()
            col = m.getX() // SIZE
            row = m.getY() // SIZE
            
            # if it was a valid Square to attack, update both the Board and
            # our graphical representation of the board
            if self.board.is_valid_square(col, row):
                if not self.board.get_squares()[(col, row)].get_is_attacked():
                    self.board.update(col, row)
                self.redraw()
        
        # user has sunk all the ships
        print "You win!"
        
        # pause 3 seconds before closing graphics window
        time.sleep(3)
        self.win.close()