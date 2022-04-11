
from SearchAlgorithms import AEstrela
from Graph import State
import numpy as np
import time
import gym



class TaxiDriver(State):

    def __init__(self, taxi, pax, barriers, onBoard, op, goal):
        self.taxi = TaxiDriver\
            .checkPos(taxi)                 # tupla com a posição do taxi
        self.pax = TaxiDriver\
            .checkPos(pax)                  # tupla com a posição do passageiro
        self.barriers = TaxiDriver\
            .detectBarriers(barriers)       # lista com as posições dos pipes
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
            sucessors.append(TaxiDriver([taxi[0]-1,taxi[1]], pax, barriers, onBoard, "north", goal))
        #move south
        if taxi and [taxi[0]+1,taxi[1]] not in barriers:
            sucessors.append(TaxiDriver([taxi[0]+1,taxi[1]], pax, barriers, onBoard, "south", goal))
        #move west
        if taxi and [taxi[0],taxi[1]-1] not in barriers:
            sucessors.append(TaxiDriver([taxi[0],taxi[1]-1], pax, barriers, onBoard, "west", goal))
        #move east
        if taxi and [taxi[0],taxi[1]+1] not in barriers:
            sucessors.append(TaxiDriver([taxi[0],taxi[1]+1], pax, barriers, onBoard, "east", goal))
        #pick up passanger
        if not onBoard and taxi == pax:
            sucessors.append(TaxiDriver(taxi, pax, barriers, True, "pick up", goal))
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

    def checkPos(tupla):
        for e in tupla:
            if e <= 0:
                raise ValueError("Posição inválida")
        return tupla
        

    def print(self):
        pass #return str(self.operator)


def main():
    print('Busca A*')
    env = gym.make("Taxi-v3").env
    M = np.zeros((env.desc.shape[0],env.desc.shape[1]))
    M = M.astype(str)
    points = ["R", "G", "B", "Y"]
    letters = []
    for i in range(env.desc.shape[0]):
        for j in range(env.desc.shape[1]):
            M[i,j] = env.desc[i,j].decode('UTF-8')
            if M[i,j] in points:
                letters.append([i,j])
    start = [1,6]
    M[start[0],start[1]] = '0'
    print(M)
    map = env.desc#TaxiDriver.detectBarriers(env.desc)
    state = TaxiDriver(start,letters[0],map,False,'',letters[2])
    algorithm = AEstrela()
    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print('Achou!')
        print(result.show_path()+" ; drop off")
        print(f"Em {tf-ts}")
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()