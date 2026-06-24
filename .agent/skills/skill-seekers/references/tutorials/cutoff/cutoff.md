# How To: Cutoff

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cutoff

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
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 2: Assign p = 1000

```python
p = 1000
```

**Verification:**
```python
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 4: Assign R = shortest_augmenting_path(...)

```python
R = shortest_augmenting_path(G, 's', 't', two_phase=True, cutoff=k)
```

**Verification:**
```python
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 5: Assign R = shortest_augmenting_path(...)

```python
R = shortest_augmenting_path(G, 's', 't', two_phase=False, cutoff=k)
```

**Verification:**
```python
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 6: Assign R = edmonds_karp(...)

```python
R = edmonds_karp(G, 's', 't', cutoff=k)
```

**Verification:**
```python
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 7: Assign R = dinitz(...)

```python
R = dinitz(G, 's', 't', cutoff=k)
```

**Verification:**
```python
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 8: Assign R = boykov_kolmogorov(...)

```python
R = boykov_kolmogorov(G, 's', 't', cutoff=k)
```

**Verification:**
```python
assert k <= R.graph['flow_value'] <= 2 * k
```

### Step 9: Call G.add_edge()

```python
G.add_edge('s', (i, 0), capacity=2)
```

### Step 10: Call nx.add_path()

```python
nx.add_path(G, ((i, j) for j in range(p)), capacity=2)
```

### Step 11: Call G.add_edge()

```python
G.add_edge((i, p - 1), 't', capacity=2)
```


## Complete Example

```python
# Workflow
k = 5
p = 1000
G = nx.DiGraph()
for i in range(k):
    G.add_edge('s', (i, 0), capacity=2)
    nx.add_path(G, ((i, j) for j in range(p)), capacity=2)
    G.add_edge((i, p - 1), 't', capacity=2)
R = shortest_augmenting_path(G, 's', 't', two_phase=True, cutoff=k)
assert k <= R.graph['flow_value'] <= 2 * k
R = shortest_augmenting_path(G, 's', 't', two_phase=False, cutoff=k)
assert k <= R.graph['flow_value'] <= 2 * k
R = edmonds_karp(G, 's', 't', cutoff=k)
assert k <= R.graph['flow_value'] <= 2 * k
R = dinitz(G, 's', 't', cutoff=k)
assert k <= R.graph['flow_value'] <= 2 * k
R = boykov_kolmogorov(G, 's', 't', cutoff=k)
assert k <= R.graph['flow_value'] <= 2 * k
```

## Next Steps


---

*Source: test_maxflow.py:541 | Complexity: Advanced | Last updated: 2026-06-02*