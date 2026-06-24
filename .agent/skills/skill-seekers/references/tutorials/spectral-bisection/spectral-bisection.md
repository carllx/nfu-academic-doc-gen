# How To: Spectral Bisection

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test spectral bisection

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

**Verification:**
```python
assert C == ({0, 1, 2}, {3, 4, 5})
```

### Step 2: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(3, 0)
```

**Verification:**
```python
assert C == ({mapping[0], mapping[1], mapping[2]}, {mapping[3], mapping[4], mapping[5]})
```

### Step 3: Assign C = nx.spectral_bisection(...)

```python
C = nx.spectral_bisection(G)
```

**Verification:**
```python
assert C == ({0, 1, 2}, {3, 4, 5})
```

### Step 4: Assign mapping = dict(...)

```python
mapping = dict(enumerate('badfec'))
```

### Step 5: Assign G = nx.relabel_nodes(...)

```python
G = nx.relabel_nodes(G, mapping)
```

### Step 6: Assign C = nx.spectral_bisection(...)

```python
C = nx.spectral_bisection(G)
```

**Verification:**
```python
assert C == ({mapping[0], mapping[1], mapping[2]}, {mapping[3], mapping[4], mapping[5]})
```


## Complete Example

```python
# Workflow
pytest.importorskip('scipy')
G = nx.barbell_graph(3, 0)
C = nx.spectral_bisection(G)
assert C == ({0, 1, 2}, {3, 4, 5})
mapping = dict(enumerate('badfec'))
G = nx.relabel_nodes(G, mapping)
C = nx.spectral_bisection(G)
assert C == ({mapping[0], mapping[1], mapping[2]}, {mapping[3], mapping[4], mapping[5]})
```

## Next Steps


---

*Source: test_algebraic_connectivity.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*