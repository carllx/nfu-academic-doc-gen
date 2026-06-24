# How To: Schultz And Gutman Index Of Odd Cycle Graph

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test schultz and gutman index of odd cycle graph

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign k = 5

```python
k = 5
```

**Verification:**
```python
assert expected_1 == actual_1
```

### Step 2: Assign n = value

```python
n = 2 * k + 1
```

**Verification:**
```python
assert expected_2 == actual_2
```

### Step 3: Assign ocg = nx.cycle_graph(...)

```python
ocg = nx.cycle_graph(n)
```

### Step 4: Assign expected_1 = value

```python
expected_1 = 2 * n * k * (k + 1)
```

### Step 5: Assign actual_1 = nx.schultz_index(...)

```python
actual_1 = nx.schultz_index(ocg)
```

### Step 6: Assign expected_2 = value

```python
expected_2 = 2 * n * k * (k + 1)
```

### Step 7: Assign actual_2 = nx.gutman_index(...)

```python
actual_2 = nx.gutman_index(ocg)
```

**Verification:**
```python
assert expected_1 == actual_1
```


## Complete Example

```python
# Workflow
k = 5
n = 2 * k + 1
ocg = nx.cycle_graph(n)
expected_1 = 2 * n * k * (k + 1)
actual_1 = nx.schultz_index(ocg)
expected_2 = 2 * n * k * (k + 1)
actual_2 = nx.gutman_index(ocg)
assert expected_1 == actual_1
assert expected_2 == actual_2
```

## Next Steps


---

*Source: test_wiener.py:111 | Complexity: Intermediate | Last updated: 2026-06-02*