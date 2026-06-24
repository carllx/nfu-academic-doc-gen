# How To: Contract Scc1

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contract scc1

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert nx.is_directed_acyclic_graph(cG)
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2), (2, 3), (2, 11), (2, 12), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5), (6, 7), (7, 8), (7, 9), (7, 10), (8, 9), (9, 7), (10, 6), (11, 2), (11, 4), (11, 6), (12, 6), (12, 11)])
```

**Verification:**
```python
assert sorted(cG.nodes()) == [0, 1, 2, 3]
```

### Step 3: Assign scc = list(...)

```python
scc = list(nx.strongly_connected_components(G))
```

**Verification:**
```python
assert cG.has_edge(*edge)
```

### Step 4: Assign cG = nx.condensation(...)

```python
cG = nx.condensation(G, scc)
```

**Verification:**
```python
assert cG.has_edge(*edge)
```

### Step 5: Assign mapping = value

```python
mapping = {}
```

**Verification:**
```python
assert cG.has_edge(*edge)
```

### Step 6: Assign edge = value

```python
edge = (mapping[2], mapping[3])
```

**Verification:**
```python
assert cG.has_edge(*edge)
```

### Step 7: Assign edge = value

```python
edge = (mapping[2], mapping[5])
```

**Verification:**
```python
assert cG.has_edge(*edge)
```

### Step 8: Assign edge = value

```python
edge = (mapping[3], mapping[5])
```

**Verification:**
```python
assert cG.has_edge(*edge)
```

### Step 9: Assign unknown = i

```python
mapping[n] = i
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edges_from([(1, 2), (2, 3), (2, 11), (2, 12), (3, 4), (4, 3), (4, 5), (5, 6), (6, 5), (6, 7), (7, 8), (7, 9), (7, 10), (8, 9), (9, 7), (10, 6), (11, 2), (11, 4), (11, 6), (12, 6), (12, 11)])
scc = list(nx.strongly_connected_components(G))
cG = nx.condensation(G, scc)
assert nx.is_directed_acyclic_graph(cG)
assert sorted(cG.nodes()) == [0, 1, 2, 3]
mapping = {}
for i, component in enumerate(scc):
    for n in component:
        mapping[n] = i
edge = (mapping[2], mapping[3])
assert cG.has_edge(*edge)
edge = (mapping[2], mapping[5])
assert cG.has_edge(*edge)
edge = (mapping[3], mapping[5])
assert cG.has_edge(*edge)
```

## Next Steps


---

*Source: test_strongly_connected.py:80 | Complexity: Advanced | Last updated: 2026-06-02*