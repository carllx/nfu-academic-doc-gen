# How To: Degree P4 Weighted

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test degree p4 weighted

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

**Verification:**
```python
assert nd == answer
```

### Step 2: Assign unknown = 4

```python
G[1][2]['weight'] = 4
```

**Verification:**
```python
assert nd == answer
```

### Step 3: Assign answer = value

```python
answer = {1: 2.0, 2: 1.8}
```

**Verification:**
```python
assert nd == answer
```

### Step 4: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(G, weight='weight')
```

**Verification:**
```python
assert nd == answer
```

### Step 5: Assign answer = value

```python
answer = {1: 2.0, 2: 1.5}
```

**Verification:**
```python
assert nd == answer
```

### Step 6: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(G)
```

**Verification:**
```python
assert nd == answer
```

### Step 7: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

### Step 8: Assign answer = value

```python
answer = {2: 2.0, 4: 1.8}
```

### Step 9: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(D, weight='weight')
```

**Verification:**
```python
assert nd == answer
```

### Step 10: Assign answer = value

```python
answer = {1: 2.0, 2: 1.8}
```

### Step 11: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

### Step 12: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(D, weight='weight', source='in', target='in')
```

**Verification:**
```python
assert nd == answer
```

### Step 13: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

### Step 14: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(D, source='in', target='out', weight='weight')
```

**Verification:**
```python
assert nd == answer
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4)
G[1][2]['weight'] = 4
answer = {1: 2.0, 2: 1.8}
nd = nx.average_degree_connectivity(G, weight='weight')
assert nd == answer
answer = {1: 2.0, 2: 1.5}
nd = nx.average_degree_connectivity(G)
assert nd == answer
D = G.to_directed()
answer = {2: 2.0, 4: 1.8}
nd = nx.average_degree_connectivity(D, weight='weight')
assert nd == answer
answer = {1: 2.0, 2: 1.8}
D = G.to_directed()
nd = nx.average_degree_connectivity(D, weight='weight', source='in', target='in')
assert nd == answer
D = G.to_directed()
nd = nx.average_degree_connectivity(D, source='in', target='out', weight='weight')
assert nd == answer
```

## Next Steps


---

*Source: test_connectivity.py:29 | Complexity: Advanced | Last updated: 2026-06-02*