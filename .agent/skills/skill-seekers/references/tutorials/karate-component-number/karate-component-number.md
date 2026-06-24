# How To: Karate Component Number

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test karate component number

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.algorithms.connectivity.kcomponents`


## Step-by-Step Guide

### Step 1: Assign karate_k_num = value

```python
karate_k_num = {0: 4, 1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 10: 3, 11: 1, 12: 2, 13: 4, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 3, 20: 2, 21: 2, 22: 2, 23: 3, 24: 3, 25: 3, 26: 2, 27: 3, 28: 3, 29: 3, 30: 4, 31: 3, 32: 4, 33: 4}
```

**Verification:**
```python
assert karate_k_num == k_num
```

### Step 2: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

### Step 3: Assign k_components = nx.k_components(...)

```python
k_components = nx.k_components(G)
```

### Step 4: Assign k_num = build_k_number_dict(...)

```python
k_num = build_k_number_dict(k_components)
```

**Verification:**
```python
assert karate_k_num == k_num
```


## Complete Example

```python
# Workflow
karate_k_num = {0: 4, 1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 10: 3, 11: 1, 12: 2, 13: 4, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 3, 20: 2, 21: 2, 22: 2, 23: 3, 24: 3, 25: 3, 26: 2, 27: 3, 28: 3, 29: 3, 30: 4, 31: 3, 32: 4, 33: 4}
G = nx.karate_club_graph()
k_components = nx.k_components(G)
k_num = build_k_number_dict(k_components)
assert karate_k_num == k_num
```

## Next Steps


---

*Source: test_kcomponents.py:166 | Complexity: Intermediate | Last updated: 2026-06-02*