# import necessary libraries
import networkx as nx  # for creating and manipulating graphs
import matplotlib.pyplot as plt  # for visualization
import math # for the A* algorithm


def astar(G, driver_node, restaurant_node):
   # Initialize open and closed lists
   open_list = [driver_node]
   closed_list = []
   
   # Initialize g and f scores for all nodes
   g_score = {node: float('inf') for node in G.nodes}
   f_score = {node: float('inf') for node in G.nodes}
   
   # Set g and f scores for start node
   g_score[driver_node] = 0
   f_score[driver_node] = heuristic(G.nodes[driver_node]['pos'], G.nodes[restaurant_node]['pos'])
   
   # Initialize dictionary to keep track of parents
   came_from = {}
   
   while open_list:
      # Get current node with lowest f score
      current_node = min(open_list, key=lambda x: f_score[x])
      
      # Check if we have reached the goal
      if current_node == restaurant_node:
         # Reconstruct path from came_from dictionary
         current = restaurant_node
         path = []
         while current != driver_node:
            path.append(current)
            current = came_from[current]
         
         path.append(driver_node)
         
         return g_score[current_node], path[::-1]
      
      # Move current node from open to closed list
      open_list.remove(current_node)
      closed_list.append(current_node)
      
      # Loop over neighbors of current node
      for neighboor in G.neighbors(current_node):
            if neighboor in closed_list:
               continue
            
            # Calculate tentative g score for neighboor
            tentative_g_score = g_score[current_node] + G.edges[current_node, neighboor]['length']
            
            if neighboor not in open_list:
               open_list.append(neighboor)
            elif tentative_g_score >= g_score[neighboor]:
               continue
            
            # Update came_from dictionary and g and f scores for neighboor
            came_from[neighboor] = current_node
            g_score[neighboor] = tentative_g_score
            f_score[neighboor] = g_score[neighboor] + heuristic(G.nodes[neighboor]['pos'], G.nodes[restaurant_node]['pos'])

def heuristic(node1_pos, node2_pos):
   return math.sqrt((node1_pos[0]-node2_pos[0])**2 + (node1_pos[1]-node2_pos[1])**2)

# The astar function returns a tuple containing the shortest distance and the shortest path from neighboorhood to 'Restaurant'.

# --------------------------------------------------------------------------------
# --------------------------------------------------------------------------------


# Encrypt or decrypt customer data using an XOR cipher.
# Iterate over each character in the input data, Convert the character to its ASCII code using the ord() function, Perform an XOR operation with the key.
# Convert the result back to a character using the chr() function, Join the characters together into a new string using the ''.join() method.
def xor_cipher(data, key):
   return ''.join(chr(ord(c) ^ key) for c in data) 

customer_details = [
   {'name': 'John Smith', 'address': '123 Main St, Anytown, USA', 'telephone': '555-1234'},
   {'name': 'Jane Doe', 'address': '456 Park Ave, Somewhere, USA', 'telephone': '555-5678'},
   {'name': 'Bob Johnson', 'address': '789 Elm St, Anytown, USA', 'telephone': '555-9012'},
   {'name': 'Mary Williams', 'address': '321 Oak Ave, Somewhere, USA', 'telephone': '555-9832'}
]

# encrypt each dictionary in the customer_details list
encrypted_customer_details = []
key = 10  # secret key for encryption, can change it to any number to have different encryption outputs
for customer in customer_details:
   # serialize the dictionary to a string and encrypt with XOR cipher
   serialized_customer = str(customer)
   encrypted_customer = xor_cipher(serialized_customer,key)
   
   # add the encrypted customer details to the list
   encrypted_customer_details.append(encrypted_customer)


# prompt the user to add customer details
while True:
   name = input("Enter customer name (or q to quit): ")
   if name == "q":
      break
   address = input("Enter customer address: ")
   telephone = input("Enter customer telephone number: ")
   
   # create a dictionary containing the customer details
   customer = {"name": name,"address": address,"telephone": telephone}
   # append the customer dictionary to the customer_details list
   customer_details.append(customer)
   print(customer_details)
   # serialize the dictionary to a string and encrypt with XOR cipher
   serialized_customer = str(customer)
   encrypted_customer = xor_cipher(serialized_customer,key)
   
   # add the encrypted customer details to the list
   encrypted_customer_details.append(encrypted_customer)


# print the list of encrypted customer details
print(f'List of encrypted customer details:\n{encrypted_customer_details}')

# Create a new graph object empty
G = nx.Graph()

# Static nodes with labels, position and colors
nodes = {
   "Restaurant": {"x": 6.5, "y": 2, "color": "orange"},
   "Customer": {"x": 1, "y": 7.25, "color": "green"},
   "City Centre": {"x": 6, "y": 5, "color": "lightblue"},
   "Small Heath": {"x": 2.5, "y": 0, "color": "lightblue"},
   "Digbeth" :{"x" :3.5, "y": 3, "color": "lightblue"},
   "Chinatown" :{"x" :0.5, "y": 1.5, "color": "lightblue"},
   "Soho":{"x" :8, "y": 3.5, "color": "lightblue"},
   "Chelsea":{"x" :6.5, "y": 7.5, "color": "lightblue"}
}

# Get nodes data items: positions and colors
for node, data in nodes.items():
   G.add_node(node, pos=(data['x'], data['y']), color=data['color'])


# Initialize a dictionary to keep track of the number of edges for each node
max_connections = 3
num_edges = {node: 0 for node in G.nodes}

# connect pairs of nodes with edges, and calculate the distance as the edge length
for node1 in G.nodes:
   for node2 in G.nodes:
      if num_edges[node1] < max_connections and num_edges[node2] < max_connections:
         if node1 != node2:  # avoid self-loops
            if not ((node1 == "Customer" and node2 == "Restaurant") or (node1 == "Restaurant" and node2 == "Customer")):
                  dist = round(heuristic(G.nodes[node1]['pos'], G.nodes[node2]['pos']), 2)  # calculate Euclidean distance
                  # connect all other pairs of nodes
                  G.add_edge(node1,node2,length=dist,color='black')
                  num_edges[node1] += 1
                  num_edges[node2] += 1

# Define a function for animating the graph
def animate_graph(G):
   # Clear any previous plot
   plt.clf() 
   
   # Get all node positions and colors
   pos = nx.get_node_attributes(G,'pos')
   colors = [G.nodes[n]['color'] for n in G.nodes]
   # Draw nodes with updated colors
   nx.draw(G, pos, node_color=colors, with_labels=True)
   
   # Get edge lengths and colors
   edge_labels = nx.get_edge_attributes(G,'length')
   edge_colors = [G.edges[e]['color'] for e in G.edges]
   
   # Draw edges with updated colors
   nx.draw_networkx_edges(G, pos, edge_color=edge_colors)
   
   # Draw edge labels
   nx.draw_networkx_edge_labels(G,pos=pos,edge_labels=edge_labels) # comment or uncomment to view the edge value distance 
   
   # Update plot
   plt.pause(1)

# animate the initial graph
animate_graph(G)

# initialize variables for finding an available driver at the nearest neighboorhood to the restaurant
minimum_dist=float('inf')
closest_driver=None

# Loop over a range of neighboorhoods only
for neighboorhood in nodes:
   if neighboorhood == 'Restaurant' or neighboorhood == 'Customer':
      continue
   try:
      # Calculate the shortest path length from the neighboorhoods to the restaurant using A* algorithm
      # assign only the first element of the tuple (the shortest distance) to the variable length, while discarding the second element (the shortest path).
      length, _ = astar(G, neighboorhood, 'Restaurant')
      
      # If this length is less than the previous minimum, update the minimum distance and the neighboorhood
      if length<minimum_dist:
            minimum_dist=length
            closest_driver=neighboorhood
      
      # Print the length of the path from the neighboorhood to the restaurant
      print(f'{neighboorhood} -> Restaurant: {length:.2f}')
   
   # If there is no path from the neighboorhoods to the restaurant, print a message
   except nx.NetworkXNoPath:
      print(f'No path from {neighboorhood} to Restaurant')

# Print the nearest neighboorhood to the restaurant
print(f'\nNearest Driver allocated from neighboorhood: {closest_driver}')

# Color the node corresponding to the nearest neighboorhood yellow
G.nodes[closest_driver]['color']='yellow'

# Calculate shortest distance and shortest path from closest_driver to Restaurant using astar function 
distance, path = astar(G, closest_driver, 'Restaurant')
print(f'Shortest Distance: {distance}')
print(f'Shortest Path: {path}')

# Color the edges of the path from the nearest neighboorhoods to the restaurant orange
for i in range(len(path)-1):
   G[path[i]][path[i+1]]['color']='yellow'

# Animate the graph to show the path from the nearest neighboorhoods to the restaurant
animate_graph(G)

try:
   # Calculate the shortest path length from the restaurant to the customer using A* algorithm
   length, _ = astar(G, 'Restaurant', 'Customer')
# If there is no path from the restaurant to the customer, print a message
except nx.NetworkXNoPath:
   print(f'No path from Restaurant to Customer')

# Print the length of the path from the restaurant to the customer
print(f'\nRestaurant -> Customer: {length:.2f}')

# Calculate the shortest path from the restaurant to the customer using A* algorithm
distance, path = astar(G, 'Restaurant', 'Customer')
print(f'Shortest Distance: {distance}')
print(f'Shortest Path: {path}')

# Color the edges of the path from the restaurant to the customer green
for i in range(len(path)-1):
   G[path[i]][path[i+1]]['color']='orange'

# Animate the graph to show the path from the restaurant to the customer
animate_graph(G)

# Ask the user whether they want to see all simple paths from the restaurant to the customer
while True:
   show_all_paths=input("\nWould you like to see all simple paths from Restaurant to Customer? \n(yes/no): ")
   
   # If the user enters yes, calculate and print the length of all simple paths from the restaurant to the customer
   if show_all_paths.lower()=='yes' or show_all_paths.lower()=='y':
      all_simple_paths=list(nx.all_simple_paths(G,'Restaurant','Customer'))
      for path in all_simple_paths:
            total_length=sum([G[path[i]][path[i+1]]['length'] for i in range(len(path)-1)])
            print(f"Length of {'-'.join(path)}: {total_length:.2f}")
      break
   # If the user enters no, break out of the loop
   elif show_all_paths.lower()=='no' or show_all_paths.lower()=='n':
      break

# Display the final graph
plt.show()
