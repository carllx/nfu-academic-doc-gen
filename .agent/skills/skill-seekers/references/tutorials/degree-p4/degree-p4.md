# How To: Degree P4

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test degree p4

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

### Step 2: Assign answer = value

```python
answer = {1: 2.0, 2: 1.5}
```

**Verification:**
```python
assert nd == answer
```

### Step 3: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(G)
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

### Step 5: Assign answer = value

```python
answer = {2: 2.0, 4: 1.5}
```

### Step 6: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(D)
```

**Verification:**
```python
assert nd == answer
```

### Step 7: Assign answer = value

```python
answer = {1: 2.0, 2: 1.5}
```

### Step 8: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

### Step 9: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(D, source='in', target='in')
```

**Verification:**
```python
assert nd == answer
```

### Step 10: Assign D = G.to_directed(...)

```python
D = G.to_directed()
```

### Step 11: Assign nd = nx.average_degree_connectivity(...)

```python
nd = nx.average_degree_connectivity(D, source='in', target='in')
```

**Verification:**
```python
assert nd == answer
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4)
answer = {1: 2.0, 2: 1.5}
nd = nx.average_degree_connectivity(G)
assert nd == answer
D = G.to_directed()
answer = {2: 2.0, 4: 1.5}
nd = nx.average_degree_connectivity(D)
assert nd == answer
answer = {1: 2.0, 2: 1.5}
D = G.to_directed()
nd = nx.average_degree_connectivity(D, source='in', target='in')
assert nd == answer
D = G.to_directed()
nd = nx.average_degree_connectivity(D, source='in', target='in')
assert nd == answer
```

## Next Steps


---

*Source: test_connectivity.py:9 | Complexity: Advanced | Last updated: 2026-06-02*