
from SearchAlgorithms import AEstrela
from TaxiDriver import TaxiDriver
from datetime import datetime
import numpy as np
import gym

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
map = env.desc
          

def test_1():
    state = TaxiDriver(start,letters[0],map,False,'',letters[1])
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result != None

def test_2():
    state = TaxiDriver(start,letters[0],map,False,'',letters[2])
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result != None

def test_3():
    state = TaxiDriver(start,letters[0],map,False,'',letters[3])
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result != None

def test_4():
    state = TaxiDriver(start,letters[1],map,False,'',letters[2])
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result != None

def test_5():
    state = TaxiDriver(start,letters[1],map,False,'',letters[3])
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result != None

def test_6():
    state = TaxiDriver(start,letters[2],map,False,'',letters[3])
    algorithm = AEstrela()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result != None