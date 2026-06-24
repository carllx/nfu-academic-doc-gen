# How To: Relabel Multidigraph Merge Inplace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel multidigraph merge inplace

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph([(0, 1), (0, 2), (0, 3)])
```

**Verification:**
```python
assert {'value': 'a'} in G[0][4].values()
```

### Step 2: Assign unknown = 'a'

```python
G[0][1][0]['value'] = 'a'
```

**Verification:**
```python
assert {'value': 'b'} in G[0][4].values()
```

### Step 3: Assign unknown = 'b'

```python
G[0][2][0]['value'] = 'b'
```

**Verification:**
```python
assert {'value': 'c'} in G[0][4].values()
```

### Step 4: Assign unknown = 'c'

```python
G[0][3][0]['value'] = 'c'
```

### Step 5: Assign mapping = value

```python
mapping = {1: 4, 2: 4, 3: 4}
```

### Step 6: Call nx.relabel_nodes()

```python
nx.relabel_nodes(G, mapping, copy=False)
```

**Verification:**
```python
assert {'value': 'a'} in G[0][4].values()
```


## Complete Example

```python
# Workflow
G = nx.MultiDiGraph([(0, 1), (0, 2), (0, 3)])
G[0][1][0]['value'] = 'a'
G[0][2][0]['value'] = 'b'
G[0][3][0]['value'] = 'c'
mapping = {1: 4, 2: 4, 3: 4}
nx.relabel_nodes(G, mapping, copy=False)
assert {'value': 'a'} in G[0][4].values()
assert {'value': 'b'} in G[0][4].values()
assert {'value': 'c'} in G[0][4].values()
```

## Next Steps


---

*Source: test_relabel.py:242 | Complexity: Intermediate | Last updated: 2026-06-02*