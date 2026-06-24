# How To: Degree K4

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test degree k4

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

**Verification:**
```python
assert nd == answer
```

### Step 2: Assign answer = value

```python
answer = {0: 3, 1: 3, 2: 3, 3: 3}
```

**Verification:**
```python
assert nd == answer
```

### Step 3: Assign nd = nx.average_neighbor_degree(...)

```python
nd = nx.average_neighbor_degree(G)
```

**Verification:**
```python
assert nd == answer
```

### Step 4: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

**Verification:**
```python
assert nd == answer
```

### Step 5: Assign nd = nx.average_neighbor_degree(...)

```python
nd = nx.average_neighbor_degree(D)
```

**Verification:**
```python
assert nd == answer
```

### Step 6: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

### Step 7: Assign nd = nx.average_neighbor_degree(...)

```python
nd = nx.average_neighbor_degree(D)
```

**Verification:**
```python
assert nd == answer
```

### Step 8: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

### Step 9: Assign nd = nx.average_neighbor_degree(...)

```python
nd = nx.average_neighbor_degree(D, source='in', target='in')
```

**Verification:**
```python
assert nd == answer
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(4)
answer = {0: 3, 1: 3, 2: 3, 3: 3}
nd = nx.average_neighbor_degree(G)
assert nd == answer
D = G.to_directed()
nd = nx.average_neighbor_degree(D)
assert nd == answer
D = G.to_directed()
nd = nx.average_neighbor_degree(D)
assert nd == answer
D = G.to_directed()
nd = nx.average_neighbor_degree(D, source='in', target='in')
assert nd == answer
```

## Next Steps


---

*Source: test_neighbor_degree.py:64 | Complexity: Advanced | Last updated: 2026-06-02*