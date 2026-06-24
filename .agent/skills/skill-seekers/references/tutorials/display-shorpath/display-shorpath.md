# How To: Display Shorpath

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test display shortest path

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `itertools`


## Step-by-Step Guide

### Step 1: Assign unknown = plt.subplots(...)

```python
fig, ax = plt.subplots()
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_nodes_from()

```python
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
```

### Step 4: Call G.add_edge()

```python
G.add_edge('A', 'B', weight=4)
```

### Step 5: Call G.add_edge()

```python
G.add_edge('A', 'H', weight=8)
```

### Step 6: Call G.add_edge()

```python
G.add_edge('B', 'C', weight=8)
```

### Step 7: Call G.add_edge()

```python
G.add_edge('B', 'H', weight=11)
```

### Step 8: Call G.add_edge()

```python
G.add_edge('C', 'D', weight=7)
```

### Step 9: Call G.add_edge()

```python
G.add_edge('C', 'F', weight=4)
```

### Step 10: Call G.add_edge()

```python
G.add_edge('C', 'I', weight=2)
```

### Step 11: Call G.add_edge()

```python
G.add_edge('D', 'E', weight=9)
```

### Step 12: Call G.add_edge()

```python
G.add_edge('D', 'F', weight=14)
```

### Step 13: Call G.add_edge()

```python
G.add_edge('E', 'F', weight=10)
```

### Step 14: Call G.add_edge()

```python
G.add_edge('F', 'G', weight=2)
```

### Step 15: Call G.add_edge()

```python
G.add_edge('G', 'H', weight=1)
```

### Step 16: Call G.add_edge()

```python
G.add_edge('G', 'I', weight=6)
```

### Step 17: Call G.add_edge()

```python
G.add_edge('H', 'I', weight=7)
```

### Step 18: Assign path = nx.shortest_path(...)

```python
path = nx.shortest_path(G, 'A', 'E', weight='weight')
```

### Step 19: Assign path_edges = list(...)

```python
path_edges = list(zip(path, path[1:]))
```

### Step 20: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, nx.spring_layout(G, seed=37), 'pos')
```

### Step 21: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(u, v): {'color': 'red' if (u, v) in path_edges or tuple(reversed((u, v))) in path_edges else 'black', 'label': {'label': d['weight'], 'rotate': False}} for u, v, d in G.edges(data=True)})
```

### Step 22: Call nx.display()

```python
nx.display(G, canvas=ax)
```

### Step 23: Call plt.tight_layout()

```python
plt.tight_layout()
```

### Step 24: Call plt.axis()

```python
plt.axis('off')
```


## Complete Example

```python
# Workflow
fig, ax = plt.subplots()
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'H', weight=8)
G.add_edge('B', 'C', weight=8)
G.add_edge('B', 'H', weight=11)
G.add_edge('C', 'D', weight=7)
G.add_edge('C', 'F', weight=4)
G.add_edge('C', 'I', weight=2)
G.add_edge('D', 'E', weight=9)
G.add_edge('D', 'F', weight=14)
G.add_edge('E', 'F', weight=10)
G.add_edge('F', 'G', weight=2)
G.add_edge('G', 'H', weight=1)
G.add_edge('G', 'I', weight=6)
G.add_edge('H', 'I', weight=7)
path = nx.shortest_path(G, 'A', 'E', weight='weight')
path_edges = list(zip(path, path[1:]))
nx.set_node_attributes(G, nx.spring_layout(G, seed=37), 'pos')
nx.set_edge_attributes(G, {(u, v): {'color': 'red' if (u, v) in path_edges or tuple(reversed((u, v))) in path_edges else 'black', 'label': {'label': d['weight'], 'rotate': False}} for u, v, d in G.edges(data=True)})
nx.display(G, canvas=ax)
plt.tight_layout()
plt.axis('off')
return fig
```

## Next Steps


---

*Source: test_image_comparison_pylab_mpl.py:151 | Complexity: Advanced | Last updated: 2026-06-02*