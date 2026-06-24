# How To: Relabel Multidigraph Inout Copy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test relabel multidigraph inout copy

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators.classic`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiDiGraph(...)

```python
G = nx.MultiDiGraph([(0, 4), (1, 4), (4, 2), (4, 3)])
```

**Verification:**
```python
assert {'value': 'a'} in H[9][4].values()
```

### Step 2: Assign unknown = 'a'

```python
G[0][4][0]['value'] = 'a'
```

**Verification:**
```python
assert {'value': 'b'} in H[9][4].values()
```

### Step 3: Assign unknown = 'b'

```python
G[1][4][0]['value'] = 'b'
```

**Verification:**
```python
assert {'value': 'c'} in H[4][9].values()
```

### Step 4: Assign unknown = 'c'

```python
G[4][2][0]['value'] = 'c'
```

**Verification:**
```python
assert len(H[4][9]) == 3
```

### Step 5: Assign unknown = 'd'

```python
G[4][3][0]['value'] = 'd'
```

**Verification:**
```python
assert {'value': 'd'} in H[4][9].values()
```

### Step 6: Call G.add_edge()

```python
G.add_edge(0, 4, key='x', value='e')
```

**Verification:**
```python
assert {'value': 'e'} in H[9][4].values()
```

### Step 7: Call G.add_edge()

```python
G.add_edge(4, 3, key='x', value='f')
```

**Verification:**
```python
assert {'value': 'f'} in H[4][9].values()
```

### Step 8: Assign mapping = value

```python
mapping = {0: 9, 1: 9, 2: 9, 3: 9}
```

**Verification:**
```python
assert len(H[9][4]) == 3
```

### Step 9: Assign H = nx.relabel_nodes(...)

```python
H = nx.relabel_nodes(G, mapping, copy=True)
```

**Verification:**
```python
assert {'value': 'a'} in H[9][4].values()
```


## Complete Example

```python
# Workflow
G = nx.MultiDiGraph([(0, 4), (1, 4), (4, 2), (4, 3)])
G[0][4][0]['value'] = 'a'
G[1][4][0]['value'] = 'b'
G[4][2][0]['value'] = 'c'
G[4][3][0]['value'] = 'd'
G.add_edge(0, 4, key='x', value='e')
G.add_edge(4, 3, key='x', value='f')
mapping = {0: 9, 1: 9, 2: 9, 3: 9}
H = nx.relabel_nodes(G, mapping, copy=True)
assert {'value': 'a'} in H[9][4].values()
assert {'value': 'b'} in H[9][4].values()
assert {'value': 'c'} in H[4][9].values()
assert len(H[4][9]) == 3
assert {'value': 'd'} in H[4][9].values()
assert {'value': 'e'} in H[9][4].values()
assert {'value': 'f'} in H[4][9].values()
assert len(H[9][4]) == 3
```

## Next Steps


---

*Source: test_relabel.py:254 | Complexity: Advanced | Last updated: 2026-06-02*