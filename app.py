

import sys
import math

x1 = int(input("enter x1: "))
x2 = int(input("enter x2: "))
y1 = int(input("enter y1: "))
y2 = int(input("enter y2: "))

# x=[]
# # x11=int(input('no of ele\n'))
# # for i in range(0,x11):
# #     x12=input('ele  ')
# #     x.append(x12)

# y=[]
# y11=int(input('no of ele\n'))
# for i in range(0,y11):
#     y12=input('ele  ')
#     y.append(y12)
# n=len(x)

def distance(x1, x2, y1, y2):

    D = float(math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2)))
    return D
    
print(distance (x1,x2,y1,y2))  


   
def distance_sum(arr, n):
    arr.sort()
    res=0
    sum=0
    for i in range(n):
        res+=(arr[i]*i-sum)
        sum+=arr[i]
        return res

def totaldistancesum(x,y,n):
    return distance_sum(x,n)+distance_sum(y,n)        

x=[-1,1,3,2]
y=[5,6,5,3]  
n=len(x)
print(totaldistancesum(x,y,n))

class Graph:

    def __init__(self, vertices):
        self.V = vertices   # Total number of vertices in the graph
        self.graph = []     # Array of edges

    # Add edges
    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])

    # Print the solution
    def print_solution(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src):

        # Step 1: fill the distance array and predecessor array
        dist = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: relax edges |V| - 1 times
        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)



 
  
class Graphd(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graphd = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
  
    def printSolution(self, dist): 
        print( "Vertex \tDistance from Source")
        for node in range(self.V): 
            print( node, "\t", dist[node] )
  
    # A utility function to find the vertex with  
    # minimum distance value, from the set of vertices  
    # not yet included in shortest path tree 
    def minDistance(self, dist, sptSet): 
  
        # Initilaize minimum distance for next node 
        min = sys.maxint 
  
        # Search not nearest vertex not in the  
        # shortest path tree 
        for v in range(self.V): 
            if dist[v] < min and sptSet[v] == False: 
                min = dist[v] 
                min_index = v 
  
        return min_index 
  
    # Funtion that implements Dijkstra's single source  
    # shortest path algorithm for a graph represented  
    # using adjacency matrix representation 
    def dijkstra(self, src): 
  
        dist = [sys.maxint] * self.V 
        dist[src] = 0
        sptSet = [False] * self.V 
  
        for cout in range(self.V): 
  
            # Pick the minimum distance vertex from  
            # the set of vertices not yet processed.  
            # u is always equal to src in first iteration 
            u = self.minDistance(dist, sptSet) 
  
            # Put the minimum distance vertex in the  
            # shotest path tree 
            sptSet[u] = True
  
            # Update dist value of the adjacent vertices  
            # of the picked vertex only if the current  
            # distance is greater than new distance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                if self.graphd[u][v] > 0 and sptSet[v] == False and  dist[v] > dist[u] + self.graphd[u][v]: 
                    dist[v] = dist[u] + self.graphd[u][v] 
  
        self.printSolution(dist) 
  
# Driver program 
g = Graphd(9) 
g.graphd = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
  
g.dijkstra(0); 


from uber_rides.session import Session
from uber_rides.client import UberRidesClient

session = Session(server_token = <TOKEN>)
client = UberRidesClient(session)

response = client.get_products(37.77, -122.41)
products = response.json.get('products')

response = client.get_products(37.77, -122.41)
products = response.json.get('products')

response = client.get_price_estimates(
    start_latitude=37.770,
    start_longitude=-122.411,
    end_latitude=37.791,
    end_longitude=-122.405,
    seat_count=2
)

estimate = response.json.get('prices')

from uber_rides.auth import AuthorizationCodeGrant
auth_flow = AuthorizationCodeGrant(
    <iFLZGtRPqXq3NlePLU5G_kUsqZEU54rq>,
    <SCOPES>,
    <x0wkEm8IGZgC2L0yrrJ1urQXNF4OKyneI_oWl9hQ>,
    <http://localhost>
)
auth_url = auth_flow.get_authorization_url()

session = auth_flow.get_session(redirect_url)
client = UberRidesClient(session, sandbox_mode=True)
credentials = session.oauth2credential

response = client.get_user_profile()
profile = response.json

first_name = profile.get('first_name')
last_name = profile.get('last_name')
email = profile.get('email')

response = client.get_user_activity()
history = response.json

# Get products for a location
response = client.get_products(37.77, -122.41)
products = response.json.get('products')

product_id = products[0].get('product_id')

# Get upfront fare and start/end locations
estimate = client.estimate_ride(
    product_id=product_id,
    start_latitude=37.77,
    start_longitude=-122.41,
    end_latitude=37.79,
    end_longitude=-122.41,
    seat_count=2
)
fare = estimate.json.get('fare')

# Request a ride with upfront fare and start/end locations
response = client.request_ride(
    product_id=product_id,
    start_latitude=37.77,
    start_longitude=-122.41,
    end_latitude=37.79,
    end_longitude=-122.41,
    seat_count=2,
    fare_id=fare['fare_id']
)

request = response.json
request_id = request.get('request_id')

# Request ride details using `request_id`
response = client.get_ride_details(request_id)
ride = response.json

# Cancel a ride
response = client.cancel_ride(request_id)
ride = response.json

