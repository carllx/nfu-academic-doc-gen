# How To: Shoraugmenting Path Two Phase

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shortest augmenting path two phase

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.flow`


## Step-by-Step Guide

### Step 1: Assign k = 5

```python
k = 5
```

**Verification:**
```python
assert R.graph['flow_value'] == k
```

### Step 2: Assign p = 1000

```python
p = 1000
```

**Verification:**
```python
assert R.graph['flow_value'] == k
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 4: Assign R = shortest_augmenting_path(...)

```python
R = shortest_augmenting_path(G, 's', 't', two_phase=True)
```

**Verification:**
```python
assert R.graph['flow_value'] == k
```

### Step 5: Assign R = shortest_augmenting_path(...)

```python
R = shortest_augmenting_path(G, 's', 't', two_phase=False)
```

**Verification:**
```python
assert R.graph['flow_value'] == k
```

### Step 6: Call G.add_edge()

```python
G.add_edge('s', (i, 0), capacity=1)
```

### Step 7: Call nx.add_path()

```python
nx.add_path(G, ((i, j) for j in range(p)), capacity=1)
```

### Step 8: Call G.add_edge()

```python
G.add_edge((i, p - 1), 't', capacity=1)
```


## Complete Example

```python
# Workflow
k = 5
p = 1000
G = nx.DiGraph()
for i in range(k):
    G.add_edge('s', (i, 0), capacity=1)
    nx.add_path(G, ((i, j) for j in range(p)), capacity=1)
    G.add_edge((i, p - 1), 't', capacity=1)
R = shortest_augmenting_path(G, 's', 't', two_phase=True)
assert R.graph['flow_value'] == k
R = shortest_augmenting_path(G, 's', 't', two_phase=False)
assert R.graph['flow_value'] == k
```

## Next Steps


---

*Source: test_maxflow.py:526 | Complexity: Advanced | Last updated: 2026-06-02*