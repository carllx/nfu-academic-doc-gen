# How To: Contract Scc Edge

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contract scc edge

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
assert sorted(cG.nodes()) == [0, 1]
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2)
```

**Verification:**
```python
assert list(cG.edges()) == [edge]
```

### Step 3: Call G.add_edge()

```python
G.add_edge(2, 1)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(2, 3)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(3, 4)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(4, 3)
```

### Step 7: Assign scc = list(...)

```python
scc = list(nx.strongly_connected_components(G))
```

### Step 8: Assign cG = nx.condensation(...)

```python
cG = nx.condensation(G, scc)
```

**Verification:**
```python
assert sorted(cG.nodes()) == [0, 1]
```

### Step 9: Assign edge = value

```python
edge = (0, 1)
```

### Step 10: Assign edge = value

```python
edge = (1, 0)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge(1, 2)
G.add_edge(2, 1)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 3)
scc = list(nx.strongly_connected_components(G))
cG = nx.condensation(G, scc)
assert sorted(cG.nodes()) == [0, 1]
if 1 in scc[0]:
    edge = (0, 1)
else:
    edge = (1, 0)
assert list(cG.edges()) == [edge]
```

## Next Steps


---

*Source: test_strongly_connected.py:135 | Complexity: Advanced | Last updated: 2026-06-02*