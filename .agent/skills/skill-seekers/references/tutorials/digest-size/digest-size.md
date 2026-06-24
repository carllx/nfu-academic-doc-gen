# How To: Digest Size

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: The hash string lengths should be as expected for a variety of graphs and
digest sizes

## Prerequisites

**Required Modules:**
- `copy`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: '\n    The hash string lengths should be as expected for a variety of graphs and\n    digest sizes\n    '

```python
'\n    The hash string lengths should be as expected for a variety of graphs and\n    digest sizes\n    '
```

**Verification:**
```python
assert h16 != h32
```

### Step 2: Assign unknown = value

```python
n, r = (100, 10)
```

**Verification:**
```python
assert len(h16) == 16 * 2
```

### Step 3: Assign p = value

```python
p = 1.0 / r
```

**Verification:**
```python
assert len(h32) == 32 * 2
```

### Step 4: Assign G = nx.erdos_renyi_graph(...)

```python
G = nx.erdos_renyi_graph(n, p * i, seed=1000 + i)
```

### Step 5: Assign h16 = nx.weisfeiler_lehman_graph_hash(...)

```python
h16 = nx.weisfeiler_lehman_graph_hash(G)
```

### Step 6: Assign h32 = nx.weisfeiler_lehman_graph_hash(...)

```python
h32 = nx.weisfeiler_lehman_graph_hash(G, digest_size=32)
```

**Verification:**
```python
assert h16 != h32
```


## Complete Example

```python
# Workflow
'\n    The hash string lengths should be as expected for a variety of graphs and\n    digest sizes\n    '
n, r = (100, 10)
p = 1.0 / r
for i in range(1, r + 1):
    G = nx.erdos_renyi_graph(n, p * i, seed=1000 + i)
    h16 = nx.weisfeiler_lehman_graph_hash(G)
    h32 = nx.weisfeiler_lehman_graph_hash(G, digest_size=32)
    assert h16 != h32
    assert len(h16) == 16 * 2
    assert len(h32) == 32 * 2
```

## Next Steps


---

*Source: test_graph_hashing.py:263 | Complexity: Intermediate | Last updated: 2026-06-02*