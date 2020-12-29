# BFS_Visual
Implemented BFS in Python in a visual way using a grid and pygame. The Nodes are undirected and unweighted nodes.

In order to run my code. You will need to install pygame by running the following command on your terminal: 
  windows: python -m pip install pygame  
  linux: python3 -m pip3 install pygame
 
Controls of the animation:
    Mouse left click: Places the starting node then will place the end node. Any clicks after that will add barriers color Black.
    Mouse right click: will remove any node
    Key C: will clear the window "reset"
    key SPACE bar: will start the algorithm but you need to have a starting and end node to get it starting
    
Implementation: The following is the structure of my Nodes
  I created a class object Grid that keep tracks of each node of their perspective location on the window.
  There is also a class object Node that keep tracks of the status of each node. Ex. If its the starting node, end node or if green then its a node that we will visit soon.
 
 BFSmain.py: handles all the user inputs and updates each node accordling and handles the breath first search implementation
