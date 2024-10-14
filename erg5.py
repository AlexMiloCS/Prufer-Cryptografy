import random

class encryptAgentNames:
    def __init__(self,data):
        self.graph = {}
        self.agent_numbers = {}
        with open(data, 'r') as file:
            for line in file:
                sender, receiver= line.strip().split(',')
                if sender not in self.graph:
                    self.graph[sender] = []
                if receiver not in self.graph:
                    self.graph[receiver] = []
                self.graph[sender].append(receiver)
                self.graph[receiver].append(sender)

    def assignNumbersToAgents(self):
        self.agent_number = 1
        for agent in self.graph:
            self.agent_numbers[agent] = self.agent_number
            self.agent_number +=1
        return self.agent_numbers

    def CreateTree(self):
        treeConnections = []
        for agent in self.graph:
            agent_num = self.agent_numbers[agent]
            agent_conn = self.graph[agent]
            for i in range(len(agent_conn)):
                connection = [agent_num,self.agent_numbers[agent_conn[i]]]
                if [self.agent_numbers[agent_conn[i]],agent_num] not in treeConnections:
                    treeConnections.append(connection)
        return treeConnections

    def getGraph(self):
        return self.graph
    
class myPrufer:
    def __init__(self,graph,agent_numbers,treeConnections):
        self.agent_numbers = agent_numbers
        self.num_of_con = {}
        self.treeConnections = treeConnections
        for agent in graph:
            values =  graph[agent]
            self.num_of_con[agent_numbers.get(agent)] = len(values)

    def find_min_label(self,conn):
        min = 10000
        min_agent = 0
        for agent in conn:
            if conn[agent]<min:
                min = conn[agent]
                min_agent = agent
        return min_agent

    def pruferEncoding(self):
        s = []
        temp_connections = self.treeConnections
        temp_num_of_con = self.num_of_con
        for i in range(len(self.agent_numbers)-2):
            min = self.find_min_label(temp_num_of_con)
            flag = True
            j=0
            while flag:                
                if temp_connections[j][0]== min  :
                    s.append(temp_connections[j][1])
                    temp_num_of_con[temp_connections[j][1]] -= 1
                    temp_connections.remove(temp_connections[j])                    
                    del temp_num_of_con[min]
                    flag = False
                elif temp_connections[j][1]== min  :
                    s.append(temp_connections[j][0])
                    temp_num_of_con[temp_connections[j][0]] -= 1
                    temp_connections.remove(temp_connections[j])                   
                    del temp_num_of_con[min]
                    flag = False 
                j+=1
        return s
    
    def pruferDecoding(self,s):
        l=[]
        connections = []
        for agent in self.agent_numbers:
            l.append(self.agent_numbers[agent])
        while s!=[]:
            flag = True
            j=0
            while flag:
                if l[j] not in s:
                    connection = [s[0],l[j]]
                    connections.append(connection)
                    flag = False
                    s.remove(s[0])
                    l.remove(l[j])
                j+=1
        connection = [l[0],l[1]]
        connections.append(connection)
        return connections

class myCryptography:
    def __init__(self,s,k):
        self.s =s
        self.k=k
    
    def encryption(self):
        for i in range(len(self.s)):
            self.s[i] += self.k
        return self.s

    def decryption(self):
        for i in range(len(self.s)):
            self.s[i] -= self.k
        return self.s

file_path = 'agents.txt' 
start = encryptAgentNames(file_path)
my_graph = start.getGraph()
agent_numbers = start.assignNumbersToAgents()
print(f'my agent numbers are: {agent_numbers}')
treeConnections = start.CreateTree()
print(f'my tree΄s connections are: {treeConnections}')
pruf = myPrufer(my_graph,agent_numbers,treeConnections)
coded = pruf.pruferEncoding()
print(f'Prufers encoding of the graph: {coded}')
coder = myCryptography(coded,2)
encrypted = coder.encryption()
print(f'Coded message sent: {encrypted}')
decrypted = coder.decryption()
print(f'Decoded message sent: {decrypted}')
decoded = pruf.pruferDecoding(decrypted)
print(f'Prufers decoding of the graph: {decoded}')