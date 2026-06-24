# How To: Hkn Harary Graph

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hkn harary graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.isomorphism.isomorph`
- `networkx.generators.harary_graph`


## Step-by-Step Guide

### Step 1: Assign k = 0

```python
k = 0
```

**Verification:**
```python
assert is_isomorphic(G1, G2)
```

### Step 2: Assign n = 0

```python
n = 0
```

**Verification:**
```python
assert is_isomorphic(G1, G2)
```

### Step 3: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, hkn_harary_graph, k, n)
```

**Verification:**
```python
assert is_isomorphic(G1, G2)
```

### Step 4: Assign k = 6

```python
k = 6
```

**Verification:**
```python
assert eSet1 == eSet2 | eSet3
```

### Step 5: Assign n = 6

```python
n = 6
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, hkn_harary_graph, k, n)
```

### Step 7: Assign G1 = hkn_harary_graph(...)

```python
G1 = hkn_harary_graph(k, n)
```

### Step 8: Assign G2 = nx.path_graph(...)

```python
G2 = nx.path_graph(n)
```

**Verification:**
```python
assert is_isomorphic(G1, G2)
```

### Step 9: Assign G1 = hkn_harary_graph(...)

```python
G1 = hkn_harary_graph(k, n)
```

### Step 10: Assign G2 = nx.circulant_graph(...)

```python
G2 = nx.circulant_graph(n, list(range(1, k // 2 + 1)))
```

**Verification:**
```python
assert is_isomorphic(G1, G2)
```

### Step 11: Assign G1 = hkn_harary_graph(...)

```python
G1 = hkn_harary_graph(k, n)
```

### Step 12: Assign L = list(...)

```python
L = list(range(1, (k + 1) // 2))
```

### Step 13: Call L.append()

```python
L.append(n // 2)
```

### Step 14: Assign G2 = nx.circulant_graph(...)

```python
G2 = nx.circulant_graph(n, L)
```

**Verification:**
```python
assert is_isomorphic(G1, G2)
```

### Step 15: Assign G1 = hkn_harary_graph(...)

```python
G1 = hkn_harary_graph(k, n)
```

### Step 16: Assign G2 = nx.circulant_graph(...)

```python
G2 = nx.circulant_graph(n, list(range(1, (k + 1) // 2)))
```

### Step 17: Assign eSet1 = set(...)

```python
eSet1 = set(G1.edges)
```

### Step 18: Assign eSet2 = set(...)

```python
eSet2 = set(G2.edges)
```

### Step 19: Assign eSet3 = set(...)

```python
eSet3 = set()
```

### Step 20: Assign half = value

```python
half = n // 2
```

**Verification:**
```python
assert eSet1 == eSet2 | eSet3
```

### Step 21: Call eSet3.add()

```python
eSet3.add((i, (i + half) % n))
```


## Complete Example

```python
# Workflow
for k, n in [(1, 6), (1, 7)]:
    G1 = hkn_harary_graph(k, n)
    G2 = nx.path_graph(n)
    assert is_isomorphic(G1, G2)
for k, n in [(2, 6), (2, 7), (4, 6), (4, 7)]:
    G1 = hkn_harary_graph(k, n)
    G2 = nx.circulant_graph(n, list(range(1, k // 2 + 1)))
    assert is_isomorphic(G1, G2)
for k, n in [(3, 6), (5, 8), (7, 10)]:
    G1 = hkn_harary_graph(k, n)
    L = list(range(1, (k + 1) // 2))
    L.append(n // 2)
    G2 = nx.circulant_graph(n, L)
    assert is_isomorphic(G1, G2)
for k, n in [(3, 5), (5, 9), (7, 11)]:
    G1 = hkn_harary_graph(k, n)
    G2 = nx.circulant_graph(n, list(range(1, (k + 1) // 2)))
    eSet1 = set(G1.edges)
    eSet2 = set(G2.edges)
    eSet3 = set()
    half = n // 2
    for i in range(half + 1):
        eSet3.add((i, (i + half) % n))
    assert eSet1 == eSet2 | eSet3
k = 0
n = 0
pytest.raises(nx.NetworkXError, hkn_harary_graph, k, n)
k = 6
n = 6
pytest.raises(nx.NetworkXError, hkn_harary_graph, k, n)
```

## Next Steps


---

*Source: test_harary_graph.py:86 | Complexity: Advanced | Last updated: 2026-06-02*