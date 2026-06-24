# How To: Schultz And Gutman Index Of Complete Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test schultz and gutman index of complete graph

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign n = 5

```python
n = 5
```

**Verification:**
```python
assert expected_1 == actual_1
```

### Step 2: Assign cg = nx.complete_graph(...)

```python
cg = nx.complete_graph(n)
```

**Verification:**
```python
assert expected_2 == actual_2
```

### Step 3: Assign expected_1 = value

```python
expected_1 = n * (n - 1) * (n - 1)
```

### Step 4: Assign actual_1 = nx.schultz_index(...)

```python
actual_1 = nx.schultz_index(cg)
```

**Verification:**
```python
assert expected_1 == actual_1
```

### Step 5: Assign expected_2 = value

```python
expected_2 = n * (n - 1) * (n - 1) * (n - 1) / 2
```

### Step 6: Assign actual_2 = nx.gutman_index(...)

```python
actual_2 = nx.gutman_index(cg)
```

**Verification:**
```python
assert expected_2 == actual_2
```


## Complete Example

```python
# Workflow
n = 5
cg = nx.complete_graph(n)
expected_1 = n * (n - 1) * (n - 1)
actual_1 = nx.schultz_index(cg)
assert expected_1 == actual_1
expected_2 = n * (n - 1) * (n - 1) * (n - 1) / 2
actual_2 = nx.gutman_index(cg)
assert expected_2 == actual_2
```

## Next Steps


---

*Source: test_wiener.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*