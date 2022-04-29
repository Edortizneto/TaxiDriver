
from SearchAlgorithms import AEstrela
from TaxiDriver import TaxiDriver
import numpy as np

class MeuTaxi():
    def __init__(self,map,positions):  # positions = (taxi row, taxi column, passenger index, destination index)
        streets = { 0:'1', 
                    1:'3',
                    2:'5',
                    3:'7',
                    4:'9'}
        positions = list(positions)
        M = np.zeros((map.shape[0],map.shape[1]))
        M = M.astype(str)
        points = ["R", "G", "Y", "B"]
        waypoints = []
        for i in range(map.shape[0]):
            for j in range(map.shape[1]):
                M[i,j] = map[i,j].decode('UTF-8')
                if M[i,j] in points:
                    waypoints.append([i,j])
        start = [positions[0]+1,int(streets[positions[1]])]
        M[start[0],start[1]] = '0'
        self.state = TaxiDriver(start,waypoints[positions[2]],map,False,'',waypoints[positions[3]])
        self.algorithm = AEstrela()
        self.result = self.algorithm.search(self.state)
            
    def path(self):
        operations = []
        if self.result != None:
            operations = (self.result.show_path()+";5").replace(" ","").replace(";"," ").split() # 5 = drop off
            operations = list(map(int,operations))
            return operations
        else:
            return 'Nao achou solucao'