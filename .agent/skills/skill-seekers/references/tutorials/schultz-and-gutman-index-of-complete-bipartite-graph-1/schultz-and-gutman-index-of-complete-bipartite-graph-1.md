# How To: Schultz And Gutman Index Of Complete Bipartite Graph 1

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test schultz and gutman index of complete bipartite graph 1

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign n = 3

```python
n = 3
```

**Verification:**
```python
assert expected_1 == actual_1
```

### Step 2: Assign m = 3

```python
m = 3
```

**Verification:**
```python
assert expected_2 == actual_2
```

### Step 3: Assign cbg = nx.complete_bipartite_graph(...)

```python
cbg = nx.complete_bipartite_graph(n, m)
```

### Step 4: Assign expected_1 = value

```python
expected_1 = n * m * (n + m) + 2 * n * (n - 1) * m + 2 * m * (m - 1) * n
```

### Step 5: Assign actual_1 = nx.schultz_index(...)

```python
actual_1 = nx.schultz_index(cbg)
```

### Step 6: Assign expected_2 = value

```python
expected_2 = n * m * (n * m) + n * (n - 1) * m * m + m * (m - 1) * n * n
```

### Step 7: Assign actual_2 = nx.gutman_index(...)

```python
actual_2 = nx.gutman_index(cbg)
```

**Verification:**
```python
assert expected_1 == actual_1
```


## Complete Example

```python
# Workflow
n = 3
m = 3
cbg = nx.complete_bipartite_graph(n, m)
expected_1 = n * m * (n + m) + 2 * n * (n - 1) * m + 2 * m * (m - 1) * n
actual_1 = nx.schultz_index(cbg)
expected_2 = n * m * (n * m) + n * (n - 1) * m * m + m * (m - 1) * n * n
actual_2 = nx.gutman_index(cbg)
assert expected_1 == actual_1
assert expected_2 == actual_2
```

## Next Steps


---

*Source: test_wiener.py:66 | Complexity: Intermediate | Last updated: 2026-06-02*