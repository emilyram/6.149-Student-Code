# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 01:18:43 2016

@author: sylvant
"""
import random
from battleship_graphics import *

class Ship(object):
    """
    Representation of a 1x1 ship in battleship
    """
    def __init__(self, sunk):
        """
        Initializes the representation of a ship
        
        Inputs: is_sunk (bool), whether or not the ship has been sunk
        
        Attributes: self.is_sunk (bool), whether or not the ship has been sunk
        
        Returns: None
        """
        self.is_sunk = sunk
    
    def get_is_sunk(self):
        """
        Getter for self.is_sunk attribute
        
        Returns: (bool) whether or not the Ship has been sunk
        """
        return self.is_sunk
    
    def set_is_sunk(self, is_sunk):
        """
        Setter for self.is_sunk attribute
        Updates whether or not the Ship has been sunk
        
        Input: is_sunk (bool), whether or not the ship has been sunk
        
        Returns: None
        """
        self.is_sunk = is_sunk

class Square(object):
    """
    Representation of a square on a board/grid, which may or may not have a Ship
    """
    def __init__(self):
        """
        Initializes representation of a square on our grid.
        When first created, a Square should not have a Ship, should not
        be attacked.
        
        Inputs: none
        
        Attributes: self.ship (Ship or None), an instance of Ship that is
                                              on the Square, if one exists
                                              there. otherwise, None. starts
                                              out as None.
                    self.is_attacked (bool), whether or not the user has 
                                            attacked this Square. starts out as
                                            False
                    self.is_mined (bool)
        
        Returns: None                                      
        """
        self.ship = None
        self.is_attacked = False
        self.is_mined = False
    
    def contains_ship(self):
        """
        Determines whether or not the Square has a Ship on it
        
        Inputs: none   
        
        Returns: (bool) whether or not the Square has a Ship on it
        """
        if self.ship == None:
            return False
        else:
            return True
    
    def get_is_attacked(self):
        """
        Getter for self.is_attacked attribute
        
        Inputs: none
        
        Returns: (bool) whether or not the user has attacked this Square
        """
        return self.is_attacked
    
    def get_ship(self):
        """
        Getter for self.ship attribute
        
        Inputs: none
        
        Returns: (Ship or None) instance of Ship if one exists on this Square,
                otherwise, None.
        """
        return self.ship
    
    def get_is_mined(self):
        """
        Getter for self.is_mined
        
        Inputs: None
        
        Returns: (bool) whether or not it's mined
        """
        return self.is_mined
    
    def set_is_attacked(self, attacked):
        """
        Setter for self.is_attacked attribute
        
        Inputs: attacked (bool), what we want to set self.is_attacked to
        
        Returns: None
        """
        self.is_attacked = attacked
        
    def set_ship(self, ship):
        """
        Setter for self.ship attribute, simulates placing a Ship on the Square
        
        Inputs: ship (Ship), the Ship we are placing on the Square
        
        Returns: None
        """
        self.ship = ship

class MinedSquare(Square):
    def __init__(self):
        Square.__init__(self)        
        self.is_mined = True
        
    def set_ship(self, ship):
        raise TypeError

class Board(object):
    """
    Representation of our battleship board, which has Squares and Ships
    """
    def __init__(self, num_cols, num_rows, num_ships):
        """
        Initializes our representation of the board
        
        Inputs: num_cols (int), how many columns the Board has
                num_rows (int), how many rows the Board has
                num_ships (int), how many ships are on the Board
        
        Attributes: self.num_cols (int), how many columns the Board has
                    self.num_rows (int), how many rows the Board has
                    self.ships (list), list of all Ships on the Board
                    self.squares (dict), maps tuple of ints to a Square,
                                        where the tuple is the (column number,
                                        row number) of the Square's location.
        """
        self.num_cols = num_cols
        self.num_rows = num_rows
        self.ships = []               
        for i in range(num_ships):
            self.ships.append(Ship(False))
        self.squares = {}
        for i in range(num_cols):
            for j in range(num_rows):
                if random.random() < 0.10:
                    self.squares[(i, j)] = MinedSquare()
                else:
                    self.squares[(i, j)] = Square()    

   
    def get_num_cols(self):
        """
        Getter for self.num_cols attribute
        
        Returns: (int) number of columns that the Board has
        """
        return self.num_cols
    
    def get_num_rows(self):
        """
        Getter for self.num_rows attribute
        
        Returns: (int) number of rows that the Board has
        """
        return self.num_rows
    
    def get_squares(self):
        """
        Getter for self.squares attribute
        
        Returns: (dict) map of tuples representing positions on the Board
                 to Square instances
        """
        return self.squares
    
    def get_neighbors(self, col, row):
        """
        Given a column and row number, returns a list of the valid neighboring
        column, row pairs. For example: with a 9x9 board, if col is 0 and
        row is 1, this function should return [(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)]
        
        Inputs: col (int), column number
                row (int), row number
        
        Returns: (list), list of tuples (int, int), where the tuples are the
                         neighboring column, row pairs
        """
        neighbors = []
        for c in range(col-1, col+2):
            for r in range(row-1, row+2):
                if (c != col or r != row) and \
                   self.is_valid_square(c,r) and \
                   not self.squares[(c, r)].get_is_attacked():
                    neighbors.append((c, r))
        return neighbors
    
    def is_valid_square(self, col, row):
        """
        Determines whether or not the input column and row numbers represent
        a valid location on the Board.
        
        Inputs: col (int), the column number we're interested in
                row (int), the row number we're interested in
         
        Returns: (bool) whether or not (col, row) is a valid location on the Board
        """
        if (col, row) in self.squares:
            return True
        else:
            return False
    
    def place_ships(self):
        """
        Iterates through the Board's list of ships and places each on the Board
        by calling self.place_ship
        
        Inputs: none
        
        Returns: None
        """
        for ship in self.ships:
            self.place_ship(ship)
    
    def place_ship(self, ship):
        """
        Places the input ship on a random valid Square on the Board that
        does not already contain a ship.

        Inputs: ship (Ship), the Ship we want to place on the Board

        Returns: None
        """
        num1 = random.randrange(0, self.num_cols)
        num2 = random.randrange(0, self.num_rows)
        while self.squares[(num1, num2)].contains_ship() == True: 
            num1 = random.randrange(0, self.num_cols)
            num2 = random.randrange(0, self.num_rows)
        try:
            self.squares[(num1, num2)].set_ship(ship)
        except TypeError:
            self.place_ship(ship)

    def update(self, col, row):
        """
        After the user attacks a Square, updates the state of the Board:
            * marks the Square the user has attacked by updating the 
              is_attacked attribute
            * if the Square contained a Ship, sink the Ship
        
        Inputs: col (int), the column of the Square that the user attacked
                row (int), the row of the Square that the user attacked
        """
        square = (col, row)
        self.squares[square].set_is_attacked(True)
        contain_ship = self.squares[square].contains_ship()
        if contain_ship == True:
            self.squares[square].get_ship().set_is_sunk(True)
        elif self.squares[square].get_is_mined() == True:
            neighbors = self.get_neighbors(col, row)
            for neighbor in neighbors:
                self.squares[neighbor].set_is_attacked(True)
                contain_ship = self.squares[neighbor].contains_ship()
                if contain_ship == True:
                    self.squares[neighbor].get_ship().set_is_sunk(True)
            
    
    def all_ships_sunk(self):
        """
        Determines if all of the Board's ships have been sunk
        
        Inputs: none
        
        Returns: (bool), whether or not all of the Board's ships have been sunk
        """
        for ship in self.ships:
            if ship.get_is_sunk() == False:
                return False
        return True

if __name__ == "__main__":
    b = Board(9, 9, 15)
    b.place_ships()
    g = GraphicsBoard(b)
    g.play()
    

    