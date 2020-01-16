from board import Board
from timon import *
from pumba import *
from simba import *
from trap import *
from pictures import *


class GameController:

    def __init__(self, lock_object=None, key = None):
        self.board = Board()
        self.timon = Timon(1, 1, TIMON_YELLOW, self.board, lock_object)
        self.pumba = Pumba(18, 14, PUMBA_YELLOW, self.board, lock_object)
        self.simba = Simba(1, 2, SIMBA_YELLOW, self.board, lock_object)
        self.trap = Trap(4, 2, TRAP_PASSIVE, self.board, 1, 1)
        self.board.set_field(1, 1, TIMON_YELLOW)
        self.board.set_field(18, 14, PUMBA_YELLOW)
        self.board.set_field(1, 2, SIMBA_YELLOW)

    def simba_movement(self):
        self.simba.changePosition()

    def timon_movement(self):
        self.timon.changePosition()

    def pumba_movement(self):
        self.pumba.changePosition()

    def trap_active(self):
        self.trap.active()