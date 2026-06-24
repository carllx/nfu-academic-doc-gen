# How To: Modularity Communities

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test modularity communities

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

### Step 1: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

**Verification:**
```python
assert set(func(G, weight=None)) == expected
```

### Step 2: Assign john_a = frozenset(...)

```python
john_a = frozenset([8, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
```

### Step 3: Assign mr_hi = frozenset(...)

```python
mr_hi = frozenset([0, 4, 5, 6, 10, 11, 16, 19])
```

### Step 4: Assign overlap = frozenset(...)

```python
overlap = frozenset([1, 2, 3, 7, 9, 12, 13, 17, 21])
```

### Step 5: Assign expected = value

```python
expected = {john_a, overlap, mr_hi}
```

**Verification:**
```python
assert set(func(G, weight=None)) == expected
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
G = nx.karate_club_graph()
john_a = frozenset([8, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33])
mr_hi = frozenset([0, 4, 5, 6, 10, 11, 16, 19])
overlap = frozenset([1, 2, 3, 7, 9, 12, 13, 17, 21])
expected = {john_a, overlap, mr_hi}
assert set(func(G, weight=None)) == expected
```

## Next Steps


---

*Source: test_modularity_max.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*