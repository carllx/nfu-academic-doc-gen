# How To: Node Not Found

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test node not found

## Prerequisites

**Required Modules:**
- `math`
- `functools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (0, 2), (2, 3)])
```

### Step 3: Assign unknown = 0

```python
G.nodes[0]['community'] = 0
```

### Step 4: Assign unknown = 1

```python
G.nodes[1]['community'] = 1
```

### Step 5: Assign unknown = 0

```python
G.nodes[2]['community'] = 0
```

### Step 6: Assign unknown = 0

```python
G.nodes[3]['community'] = 0
```

### Step 7: Call self.func()

```python
self.func(G, [(0, 4)])
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (2, 3)])
G.nodes[0]['community'] = 0
G.nodes[1]['community'] = 1
G.nodes[2]['community'] = 0
G.nodes[3]['community'] = 0
with pytest.raises(nx.NodeNotFound):
    self.func(G, [(0, 4)])
```

## Next Steps


---

*Source: test_link_prediction.py:407 | Complexity: Intermediate | Last updated: 2026-06-02*