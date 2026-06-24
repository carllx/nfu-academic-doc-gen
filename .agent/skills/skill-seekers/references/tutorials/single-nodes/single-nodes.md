# How To: Single Nodes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single nodes

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.bipartite`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(2, 3)
```

**Verification:**
```python
assert sbn[1] == pytest.approx(0.85, abs=0.01)
```

### Step 2: Call G.add_edge()

```python
G.add_edge(2, 4)
```

**Verification:**
```python
assert sbn[2] == pytest.approx(0.77, abs=0.01)
```

### Step 3: Assign sbn = sb(...)

```python
sbn = sb(G, nodes=[1, 2])
```

**Verification:**
```python
assert sbn[1] == pytest.approx(0.73, abs=0.01)
```

### Step 4: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(2, 3)
```

**Verification:**
```python
assert sbn[2] == pytest.approx(0.82, abs=0.01)
```

### Step 5: Call G.add_edge()

```python
G.add_edge(0, 1)
```

### Step 6: Assign sbn = sb(...)

```python
sbn = sb(G, nodes=[1, 2])
```

**Verification:**
```python
assert sbn[1] == pytest.approx(0.73, abs=0.01)
```


## Complete Example

```python
# Workflow
G = nx.complete_bipartite_graph(2, 3)
G.add_edge(2, 4)
sbn = sb(G, nodes=[1, 2])
assert sbn[1] == pytest.approx(0.85, abs=0.01)
assert sbn[2] == pytest.approx(0.77, abs=0.01)
G = nx.complete_bipartite_graph(2, 3)
G.add_edge(0, 1)
sbn = sb(G, nodes=[1, 2])
assert sbn[1] == pytest.approx(0.73, abs=0.01)
assert sbn[2] == pytest.approx(0.82, abs=0.01)
```

## Next Steps


---

*Source: test_spectral_bipartivity.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*