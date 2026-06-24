# How To: Display Labels And Colors

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: See 'Labels and Colors' gallery example

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `itertools`


## Step-by-Step Guide

### Step 1: "See 'Labels and Colors' gallery example"

```python
"See 'Labels and Colors' gallery example"
```

### Step 2: Assign unknown = plt.subplots(...)

```python
fig, ax = plt.subplots()
```

### Step 3: Assign G = nx.cubical_graph(...)

```python
G = nx.cubical_graph()
```

### Step 4: Assign pos = nx.spring_layout(...)

```python
pos = nx.spring_layout(G, seed=3113794652)
```

### Step 5: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, pos, 'pos')
```

### Step 6: Assign labels = iter(...)

```python
labels = iter(['$a$', '$b$', '$c$', '$d$', '$\\alpha$', '$\\beta$', '$\\gamma$', '$\\delta$'])
```

### Step 7: Call nx.set_node_attributes()

```python
nx.set_node_attributes(G, {n: {'size': 800, 'alpha': 0.9, 'color': 'tab:red' if n < 4 else 'tab:blue', 'label': {'label': next(labels), 'size': 22, 'color': 'whitesmoke'}} for n in G.nodes()})
```

### Step 8: Call nx.display()

```python
nx.display(G, node_pos='pos', edge_color='tab:grey')
```

### Step 9: Assign edgelist = value

```python
edgelist = [(0, 1), (1, 2), (2, 3), (0, 3)]
```

### Step 10: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(u, v): {'width': 8, 'alpha': 0.5, 'color': 'tab:red', 'visible': (u, v) in edgelist} for u, v in G.edges()})
```

### Step 11: Call nx.display()

```python
nx.display(G, node_pos='pos', node_visible=False)
```

### Step 12: Assign edgelist = value

```python
edgelist = [(4, 5), (5, 6), (6, 7), (4, 7)]
```

### Step 13: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, {(u, v): {'color': 'tab:blue', 'visible': (u, v) in edgelist} for u, v in G.edges()})
```

### Step 14: Call nx.display()

```python
nx.display(G, node_pos='pos', node_visible=False)
```

### Step 15: Call plt.tight_layout()

```python
plt.tight_layout()
```

### Step 16: Call plt.axis()

```python
plt.axis('off')
```


## Complete Example

```python
# Workflow
"See 'Labels and Colors' gallery example"
fig, ax = plt.subplots()
G = nx.cubical_graph()
pos = nx.spring_layout(G, seed=3113794652)
nx.set_node_attributes(G, pos, 'pos')
labels = iter(['$a$', '$b$', '$c$', '$d$', '$\\alpha$', '$\\beta$', '$\\gamma$', '$\\delta$'])
nx.set_node_attributes(G, {n: {'size': 800, 'alpha': 0.9, 'color': 'tab:red' if n < 4 else 'tab:blue', 'label': {'label': next(labels), 'size': 22, 'color': 'whitesmoke'}} for n in G.nodes()})
nx.display(G, node_pos='pos', edge_color='tab:grey')
edgelist = [(0, 1), (1, 2), (2, 3), (0, 3)]
nx.set_edge_attributes(G, {(u, v): {'width': 8, 'alpha': 0.5, 'color': 'tab:red', 'visible': (u, v) in edgelist} for u, v in G.edges()})
nx.display(G, node_pos='pos', node_visible=False)
edgelist = [(4, 5), (5, 6), (6, 7), (4, 7)]
nx.set_edge_attributes(G, {(u, v): {'color': 'tab:blue', 'visible': (u, v) in edgelist} for u, v in G.edges()})
nx.display(G, node_pos='pos', node_visible=False)
plt.tight_layout()
plt.axis('off')
return fig
```

## Next Steps


---

*Source: test_image_comparison_pylab_mpl.py:54 | Complexity: Advanced | Last updated: 2026-06-02*