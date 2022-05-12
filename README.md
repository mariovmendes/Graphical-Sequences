# Graphical-Sequences
Small project for the MD course developed using
the Python Programming Language 🐍

The main purpose of this program is to check if 
a given sequence is a graphical sequence and represent 
it using nodes and edges.

## Preview

Graphical representation of a sequence.
(4,4,4,4,4,4)
![alt text](https://raw.githubusercontent.com/mendes4dev/Graphical-Sequences/main/Graph.gv.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install graphviz.

```bash
pip install graphviz
```

## Graphviz Usage

```python
import graphviz

# Creates Graph
g = graphviz.Graph(format='png')

# Adds a new node to the graph
g.node(chr(ord('A')+count))

# Creates a new connection between node1 and node2
g.edge("node1","node2")

# Generates graph output file
g.view()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
