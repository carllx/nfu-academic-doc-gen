# How To: Nested S Blossom

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Create nested S-blossom, use for augmentation:

## Prerequisites

**Required Modules:**
- `math`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'Create nested S-blossom, use for augmentation:'

```python
'Create nested S-blossom, use for augmentation:'
```

**Verification:**
```python
assert answer == expected
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert answer == expected
```

### Step 3: Call G.add_weighted_edges_from()

```python
G.add_weighted_edges_from([(1, 2, 9), (1, 3, 9), (2, 3, 10), (2, 4, 8), (3, 5, 8), (4, 5, 10), (5, 6, 6)])
```

### Step 4: Assign expected_edgeset = value

```python
expected_edgeset = {(1, 3), (2, 4), (5, 6)}
```

### Step 5: Assign expected = value

```python
expected = {frozenset(e) for e in expected_edgeset}
```

### Step 6: Assign answer = value

```python
answer = {frozenset(e) for e in nx.max_weight_matching(G)}
```

**Verification:**
```python
assert answer == expected
```

### Step 7: Assign answer = value

```python
answer = {frozenset(e) for e in nx.min_weight_matching(G)}
```

**Verification:**
```python
assert answer == expected
```


## Complete Example

```python
# Workflow
'Create nested S-blossom, use for augmentation:'
G = nx.Graph()
G.add_weighted_edges_from([(1, 2, 9), (1, 3, 9), (2, 3, 10), (2, 4, 8), (3, 5, 8), (4, 5, 10), (5, 6, 6)])
expected_edgeset = {(1, 3), (2, 4), (5, 6)}
expected = {frozenset(e) for e in expected_edgeset}
answer = {frozenset(e) for e in nx.max_weight_matching(G)}
assert answer == expected
answer = {frozenset(e) for e in nx.min_weight_matching(G)}
assert answer == expected
```

## Next Steps


---

*Source: test_matching.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*