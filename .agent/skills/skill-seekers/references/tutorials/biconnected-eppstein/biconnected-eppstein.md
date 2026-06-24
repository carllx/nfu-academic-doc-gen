# How To: Biconnected Eppstein

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test biconnected eppstein

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph({0: [1, 2, 5], 1: [0, 5], 2: [0, 3, 4], 3: [2, 4, 5, 6], 4: [2, 3, 5, 6], 5: [0, 1, 3, 4], 6: [3, 4]})
```

**Verification:**
```python
assert nx.is_biconnected(G1)
```

### Step 2: Assign G2 = nx.Graph(...)

```python
G2 = nx.Graph({0: [2, 5], 1: [3, 8], 2: [0, 3, 5], 3: [1, 2, 6, 8], 4: [7], 5: [0, 2], 6: [3, 8], 7: [4], 8: [1, 3, 6]})
```

**Verification:**
```python
assert not nx.is_biconnected(G2)
```

### Step 3: Assign answer_G2 = value

```python
answer_G2 = [{1, 3, 6, 8}, {0, 2, 5}, {2, 3}, {4, 7}]
```

**Verification:**
```python
assert_components_equal(bcc, answer_G2)
```

### Step 4: Assign bcc = list(...)

```python
bcc = list(nx.biconnected_components(G2))
```

### Step 5: Call assert_components_equal()

```python
assert_components_equal(bcc, answer_G2)
```


## Complete Example

```python
# Workflow
G1 = nx.Graph({0: [1, 2, 5], 1: [0, 5], 2: [0, 3, 4], 3: [2, 4, 5, 6], 4: [2, 3, 5, 6], 5: [0, 1, 3, 4], 6: [3, 4]})
G2 = nx.Graph({0: [2, 5], 1: [3, 8], 2: [0, 3, 5], 3: [1, 2, 6, 8], 4: [7], 5: [0, 2], 6: [3, 8], 7: [4], 8: [1, 3, 6]})
assert nx.is_biconnected(G1)
assert not nx.is_biconnected(G2)
answer_G2 = [{1, 3, 6, 8}, {0, 2, 5}, {2, 3}, {4, 7}]
bcc = list(nx.biconnected_components(G2))
assert_components_equal(bcc, answer_G2)
```

## Next Steps


---

*Source: test_biconnected.py:199 | Complexity: Intermediate | Last updated: 2026-06-02*