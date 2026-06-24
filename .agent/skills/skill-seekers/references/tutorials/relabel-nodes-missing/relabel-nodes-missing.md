# How To: Relabel Nodes Missing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel nodes missing

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')])
```

**Verification:**
```python
assert nodes_equal(H.nodes, G.nodes)
```

### Step 2: Assign mapping = value

```python
mapping = {0: 'aardvark'}
```

**Verification:**
```python
assert nodes_equal(G.nodes, GG.nodes)
```

### Step 3: Assign H = nx.relabel_nodes(...)

```python
H = nx.relabel_nodes(G, mapping, copy=True)
```

**Verification:**
```python
assert nodes_equal(H.nodes, G.nodes)
```

### Step 4: Assign GG = G.copy(...)

```python
GG = G.copy()
```

### Step 5: Call nx.relabel_nodes()

```python
nx.relabel_nodes(G, mapping, copy=False)
```

**Verification:**
```python
assert nodes_equal(G.nodes, GG.nodes)
```


## Complete Example

```python
# Workflow
G = nx.Graph([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D')])
mapping = {0: 'aardvark'}
H = nx.relabel_nodes(G, mapping, copy=True)
assert nodes_equal(H.nodes, G.nodes)
GG = G.copy()
nx.relabel_nodes(G, mapping, copy=False)
assert nodes_equal(G.nodes, GG.nodes)
```

## Next Steps


---

*Source: test_relabel.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*