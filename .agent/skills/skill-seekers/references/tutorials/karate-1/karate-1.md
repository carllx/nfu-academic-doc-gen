# How To: Karate 1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test karate 1

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.approximation`
- `networkx.algorithms.approximation.kcomponents`


## Step-by-Step Guide

### Step 1: Assign karate_k_num = value

```python
karate_k_num = {0: 4, 1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 10: 3, 11: 1, 12: 2, 13: 4, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 3, 20: 2, 21: 2, 22: 2, 23: 3, 24: 3, 25: 3, 26: 2, 27: 3, 28: 3, 29: 3, 30: 4, 31: 3, 32: 4, 33: 4}
```

**Verification:**
```python
assert k_num in (karate_k_num, approx_karate_k_num)
```

### Step 2: Assign approx_karate_k_num = karate_k_num.copy(...)

```python
approx_karate_k_num = karate_k_num.copy()
```

### Step 3: Assign unknown = 2

```python
approx_karate_k_num[24] = 2
```

### Step 4: Assign unknown = 2

```python
approx_karate_k_num[25] = 2
```

### Step 5: Assign G = nx.karate_club_graph(...)

```python
G = nx.karate_club_graph()
```

### Step 6: Assign k_comps = k_components(...)

```python
k_comps = k_components(G)
```

### Step 7: Assign k_num = build_k_number_dict(...)

```python
k_num = build_k_number_dict(k_comps)
```

**Verification:**
```python
assert k_num in (karate_k_num, approx_karate_k_num)
```


## Complete Example

```python
# Workflow
karate_k_num = {0: 4, 1: 4, 2: 4, 3: 4, 4: 3, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2, 10: 3, 11: 1, 12: 2, 13: 4, 14: 2, 15: 2, 16: 2, 17: 2, 18: 2, 19: 3, 20: 2, 21: 2, 22: 2, 23: 3, 24: 3, 25: 3, 26: 2, 27: 3, 28: 3, 29: 3, 30: 4, 31: 3, 32: 4, 33: 4}
approx_karate_k_num = karate_k_num.copy()
approx_karate_k_num[24] = 2
approx_karate_k_num[25] = 2
G = nx.karate_club_graph()
k_comps = k_components(G)
k_num = build_k_number_dict(k_comps)
assert k_num in (karate_k_num, approx_karate_k_num)
```

## Next Steps


---

*Source: test_kcomponents.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*