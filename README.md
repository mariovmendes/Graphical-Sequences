# Graphical-Sequences
Small Project for the MD course developed using
the Python Programming Language

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
