# Step 1: Import the necessary libraries
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Define the file path to the interaction data
# ✨ Make sure your downloaded file is named this!
file_path = '/Users/manoharpaturi/Desktop/bio/string_interactions_short.tsv'

# Step 2: Load the interaction data into a pandas DataFrame
df = pd.read_csv(file_path, sep='\t')
df.columns = df.columns.str.strip().str.replace('#', '')

# Let's look at the first few rows to make sure it loaded correctly
print("--- First 5 rows of the data ---")
print(df.head())
print("\n") # Adds a blank line for spacing

# Step 3: Create the graph from the DataFrame
G = nx.from_pandas_edgelist(df, source='node1', target='node2')

# Step 4: Check if the graph was built correctly
print("--- Network Stats ---")
print(f"Number of nodes (proteins): {G.number_of_nodes()}")
print(f"Number of edges (interactions): {G.number_of_edges()}")


# Step 5: Calculate Centrality Measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Helper function to sort and print the top results
def print_top_nodes(centrality_dict, measure_name, top_n=5):
    # Sort the dictionary by values in descending order
    sorted_nodes = sorted(centrality_dict.items(), key=lambda item: item[1], reverse=True)
    
    print(f"--- Top {top_n} Proteins by {measure_name} ---")
    for i in range(min(top_n, len(sorted_nodes))):
        node, score = sorted_nodes[i]
        print(f"{i+1}. {node}: {score:.4f}") # Print score rounded to 4 decimal places
    print("\n")

# Step 6: Print the results
print_top_nodes(degree_centrality, "Degree Centrality")
print_top_nodes(betweenness_centrality, "Betweenness Centrality")
print_top_nodes(closeness_centrality, "Closeness Centrality")



# Step 7: Visualize and save the network graph
plt.figure(figsize=(8, 8)) # Adjust size for better layout

# Draw the network
nx.draw_networkx(G, 
                 with_labels=True, 
                 node_color='skyblue', 
                 node_size=2000, 
                 font_size=10, 
                 width=1.5,
                 edge_color='gray')

plt.title("Protein-Protein Interaction Network in Type 1 Diabetes") # ✨ Updated title
plt.savefig("T1D_Network_Graph.png") # ✨ Updated filename

print("\n--- Network graph saved as T1D_Network_Graph.png ---") # ✨ Updated message