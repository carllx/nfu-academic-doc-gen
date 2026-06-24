# How To: Shorpath

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shortest path

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.threshold`


## Step-by-Step Guide

### Step 1: Assign deg = value

```python
deg = [3, 2, 2, 1]
```

**Verification:**
```python
assert nxt.shortest_path(cs1, n, m) == nx.shortest_path(G, n, m)
```

### Step 2: Assign G = nx.generators.havel_hakimi_graph(...)

```python
G = nx.generators.havel_hakimi_graph(deg)
```

**Verification:**
```python
assert spl == spl2
```

### Step 3: Assign cs1 = nxt.creation_sequence(...)

```python
cs1 = nxt.creation_sequence(deg, with_labels=True)
```

**Verification:**
```python
assert spld == nx.single_source_shortest_path_length(G, 3)
```

### Step 4: Assign spl = nxt.shortest_path_length(...)

```python
spl = nxt.shortest_path_length(cs1, 3)
```

**Verification:**
```python
assert nxt.shortest_path(['d', 'd', 'd', 'i', 'd', 'd'], 1, 2) == [1, 2]
```

### Step 5: Assign spl2 = nxt.shortest_path_length(...)

```python
spl2 = nxt.shortest_path_length([t for v, t in cs1], 2)
```

**Verification:**
```python
assert nxt.shortest_path([3, 1, 2], 1, 2) == [1, 2]
```

### Step 6: Assign spld = value

```python
spld = {}
```

**Verification:**
```python
assert nxt.shortest_path([3, 1, 2], 1, 1) == [1]
```

### Step 7: Call pytest.raises()

```python
pytest.raises(TypeError, nxt.shortest_path, [3.0, 1.0, 2.0], 1, 2)
```

### Step 8: Call pytest.raises()

```python
pytest.raises(ValueError, nxt.shortest_path, [3, 1, 2], 'a', 2)
```

### Step 9: Call pytest.raises()

```python
pytest.raises(ValueError, nxt.shortest_path, [3, 1, 2], 1, 'b')
```

**Verification:**
```python
assert nxt.shortest_path([3, 1, 2], 1, 1) == [1]
```

### Step 10: Assign n = value

```python
n = cs1[j][0]
```

### Step 11: Assign unknown = pl

```python
spld[n] = pl
```


## Complete Example

```python
# Workflow
deg = [3, 2, 2, 1]
G = nx.generators.havel_hakimi_graph(deg)
cs1 = nxt.creation_sequence(deg, with_labels=True)
for n, m in [(3, 0), (0, 3), (0, 2), (0, 1), (1, 3), (3, 1), (1, 2), (2, 3)]:
    assert nxt.shortest_path(cs1, n, m) == nx.shortest_path(G, n, m)
spl = nxt.shortest_path_length(cs1, 3)
spl2 = nxt.shortest_path_length([t for v, t in cs1], 2)
assert spl == spl2
spld = {}
for j, pl in enumerate(spl):
    n = cs1[j][0]
    spld[n] = pl
assert spld == nx.single_source_shortest_path_length(G, 3)
assert nxt.shortest_path(['d', 'd', 'd', 'i', 'd', 'd'], 1, 2) == [1, 2]
assert nxt.shortest_path([3, 1, 2], 1, 2) == [1, 2]
pytest.raises(TypeError, nxt.shortest_path, [3.0, 1.0, 2.0], 1, 2)
pytest.raises(ValueError, nxt.shortest_path, [3, 1, 2], 'a', 2)
pytest.raises(ValueError, nxt.shortest_path, [3, 1, 2], 1, 'b')
assert nxt.shortest_path([3, 1, 2], 1, 1) == [1]
```

## Next Steps


---

*Source: test_threshold.py:103 | Complexity: Advanced | Last updated: 2026-06-02*