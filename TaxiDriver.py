from Graph import State
import numpy as np

class TaxiDriver(State):

    def __init__(self, taxi, pax, barriers, onBoard, op, goal):

        self.barriers = TaxiDriver\
            .detectBarriers(barriers)       # lista com as posições dos pipes
        self.taxi = TaxiDriver\
            .checkPos(self,taxi)            # tupla com a posição do taxi
        self.pax = TaxiDriver\
            .checkPos(self,pax)             # tupla com a posição do passageiro
        self.onBoard = onBoard              # booleana se passageiro está no taxi
        self.operator = op                  # string da operação (e.g. "north", "south")
        self.goal = goal                    # tupla com o destino do passageiro
        
    def env(self):
        return str(self.operator)+str(self.taxi)+str(self.onBoard)

    def sucessors(self):
        sucessors = []
        taxi = self.taxi
        pax = self.pax
        barriers = self.barriers
        onBoard = self.onBoard
        goal = self.goal
        #move north
        if taxi and [taxi[0]-1,taxi[1]] not in barriers:
            sucessors.append(TaxiDriver([taxi[0]-1,taxi[1]], pax, barriers, onBoard, "1", goal))
        #move south
        if taxi and [taxi[0]+1,taxi[1]] not in barriers:
            sucessors.append(TaxiDriver([taxi[0]+1,taxi[1]], pax, barriers, onBoard, "0", goal))
        #move west
        if taxi and [taxi[0],taxi[1]-1] not in barriers:
            sucessors.append(TaxiDriver([taxi[0],taxi[1]-2], pax, barriers, onBoard, "3", goal))
        #move east
        if taxi and [taxi[0],taxi[1]+1] not in barriers:
            sucessors.append(TaxiDriver([taxi[0],taxi[1]+2], pax, barriers, onBoard, "2", goal))
        #pick up passanger
        if not onBoard and taxi == pax:
            sucessors.append(TaxiDriver(taxi, pax, barriers, True, "4", goal))
        return sucessors
    
    def is_goal(self):
        return self.onBoard and self.taxi == self.goal

    def description(self):
        return "Taxi pick up passanger and drop off at destination (goal) "
    
    def cost(self):
        return 1 

    def h(self):
        erros = self.distanciaManhattan()
        return erros

    def distanciaManhattan(self):
        if not self.onBoard:
            distX = abs(self.pax[1] - self.taxi[1])
            distY = abs(self.pax[0] - self.taxi[0])
        else:
            distX = abs(self.goal[1] - self.taxi[1])
            distY = abs(self.goal[0] - self.taxi[0])
        return distX + distY

    def detectBarriers(map):
        if type(map) != list:
            barriers = ["|","-","+"]
            coords = []
            M = np.zeros((map.shape[0],map.shape[1]))
            M = M.astype(str)
            for i in range(map.shape[0]):
                for j in range(map.shape[1]):
                    M[i,j] = map[i,j].decode('UTF-8')
                    if M[i,j] in barriers:
                        coords.append([i,j])
            return coords
        return map

    def checkPos(self,tupla):
        bounds = max(self.barriers)
        if tupla[0] > 0 and tupla[0] < bounds[0]:
            if tupla[1] > 0 and tupla[1] < bounds[1]:
                return tupla
        else:
            raise ValueError("Posição inválida")

    def print(self):
        pass #return str(self.operator)