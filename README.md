# TaxiDriver

### OpenAI Gym Taxi Driver v3 Solver
#### Edgard Ortiz Neto
<br>
<br>
Tudo começa pelo arquivo "main.py", onde será criado um ambiente do "OpenAI Gym Taxi Driver v3" e as posições tanto do Taxi quanto do destino e o passageiro são escolhidas de maneira aleatória. Feito isso, os dados do problema são passados para a classe MeuTaxi, que executará o algoritmo A* com a heurística Distância de Manhattan presentes no arquivo TaxiDriver.py. Uma vez com a solução obtida, o método path() registra a sequência de passos do início até o final do trajeto do taxi. Com a solução em mãos, é feito uma iteração no path() para mostrar ao usuário como o taxi saiu do seu ponto inicial até o destino final.
<br><br>
No arquivo TaxiDriver.py, a classe TaxiDriver recebe a posição de início do Taxi, local de onde está o passageiro, o mapa do trajeto, uma booleana para
saber se o passageiro está no taxi e o destino final.  

```{python3}
class TaxiDriver(State):

    def __init__(self, taxi, pax, barriers, onBoard, op, goal):
```
Para representar os estados, foi necessário registrar a posição do táxi, mais a informação se estava carregando o passageiro e sua operação, para que não houvesse nenhum estado repetido.
```{python3}
def env(self):
    return str(self.operator)+str(self.taxi)+str(self.onBoard)
```
Na geração de sucessores, foi preciso criar as opções do taxi poder ir para cima, baixo, esquerda e direita (north,south,etc) além de pegar o passageiro, porém, com algumas atenções, já que o táxi não pode passar por cima dos obstáculos nem pegar um passageiro se este já estiver carregando, logo é preciso checar as posições futuras na hora de gerar sucessores além de verificar se o passageiro está a bordo. Observação feita ao fato de que é preciso avançar 2 posições caso seja necessário ir para direita ou esquerda, já que as ruas possuem um intervalo de uma coluna, que pode ser ou uma entrada ou parede.
```{python3}
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
```
A Heurística utilizada foi a distância de Manhattan, que consiste na somatória de distâncias laterais e verticais de um ponto A até o B. No nosso caso, a busca A* vai buscar aquele sucessor que estiver mais próximo, com menor custo de heurística, agilizando a nossa resolução.
```{python3}
def distanciaManhattan(self):
        if not self.onBoard:
            distX = abs(self.pax[1] - self.taxi[1])
            distY = abs(self.pax[0] - self.taxi[0])
        else:
            distX = abs(self.goal[1] - self.taxi[1])
            distY = abs(self.goal[0] - self.taxi[0])
        return distX + distY
```