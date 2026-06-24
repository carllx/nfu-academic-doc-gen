# How To: Insufficient Community Information

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insufficient community information

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
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
```

### Step 3: Assign unknown = 0

```python
G.nodes[0]['community'] = 0
```

### Step 4: Assign unknown = 0

```python
G.nodes[1]['community'] = 0
```

### Step 5: Assign unknown = 0

```python
G.nodes[3]['community'] = 0
```

### Step 6: Call list()

```python
list(self.func(G, [(0, 3)]))
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3)])
G.nodes[0]['community'] = 0
G.nodes[1]['community'] = 0
G.nodes[3]['community'] = 0
with pytest.raises(nx.NetworkXAlgorithmError):
    list(self.func(G, [(0, 3)]))
```

## Next Steps


---

*Source: test_link_prediction.py:445 | Complexity: Intermediate | Last updated: 2026-06-02*