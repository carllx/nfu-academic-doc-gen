# How To: Modularity Communities Weighted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test modularity communities weighted

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign G = nx.balanced_tree(...)

```python
G = nx.balanced_tree(2, 3)
```

**Verification:**
```python
assert func(G, weight='weight') == expected
```

### Step 2: Assign expected = value

```python
expected = [{0, 1, 3, 4, 7, 8, 9, 10}, {2, 5, 6, 11, 12, 13, 14}]
```

**Verification:**
```python
assert func(G, weight='weight', resolution=0.9) == expected
```

### Step 3: Assign unknown = 10.0

```python
G[a][b]['weight'] = 10.0
```

**Verification:**
```python
assert func(G, weight='weight', resolution=0.3) == expected
```

### Step 4: Assign unknown = 1.0

```python
G[a][b]['weight'] = 1.0
```

**Verification:**
```python
assert func(G, weight='weight', resolution=1.1) != expected
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
G = nx.balanced_tree(2, 3)
for a, b in G.edges:
    if (a == 1 or a == 2) and b != 0:
        G[a][b]['weight'] = 10.0
    else:
        G[a][b]['weight'] = 1.0
expected = [{0, 1, 3, 4, 7, 8, 9, 10}, {2, 5, 6, 11, 12, 13, 14}]
assert func(G, weight='weight') == expected
assert func(G, weight='weight', resolution=0.9) == expected
assert func(G, weight='weight', resolution=0.3) == expected
assert func(G, weight='weight', resolution=1.1) != expected
```

## Next Steps


---

*Source: test_modularity_max.py:97 | Complexity: Intermediate | Last updated: 2026-06-02*