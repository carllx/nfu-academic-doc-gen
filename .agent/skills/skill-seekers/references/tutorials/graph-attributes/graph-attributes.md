# How To: Graph Attributes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph attributes

## Prerequisites

**Required Modules:**
- `json`
- `pytest`
- `networkx`
- `networkx.readwrite.json_graph`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert H.nodes[1]['color'] == 'red'
```

### Step 2: Call G.add_nodes_from()

```python
G.add_nodes_from([1, 2, 3], color='red')
```

**Verification:**
```python
assert H.nodes[1]['color'] == 'red'
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 2, foo=7)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(1, 3, foo=10)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(3, 4, foo=10)
```

### Step 6: Assign H = tree_graph(...)

```python
H = tree_graph(tree_data(G, 1))
```

**Verification:**
```python
assert H.nodes[1]['color'] == 'red'
```

### Step 7: Assign d = json.dumps(...)

```python
d = json.dumps(tree_data(G, 1))
```

### Step 8: Assign H = tree_graph(...)

```python
H = tree_graph(json.loads(d))
```

**Verification:**
```python
assert H.nodes[1]['color'] == 'red'
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3], color='red')
G.add_edge(1, 2, foo=7)
G.add_edge(1, 3, foo=10)
G.add_edge(3, 4, foo=10)
H = tree_graph(tree_data(G, 1))
assert H.nodes[1]['color'] == 'red'
d = json.dumps(tree_data(G, 1))
H = tree_graph(json.loads(d))
assert H.nodes[1]['color'] == 'red'
```

## Next Steps


---

*Source: test_tree.py:19 | Complexity: Advanced | Last updated: 2026-06-02*