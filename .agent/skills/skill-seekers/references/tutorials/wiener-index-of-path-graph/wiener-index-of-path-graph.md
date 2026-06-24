# How To: Wiener Index Of Path Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wiener index of path graph

## Prerequisites

**Required Modules:**
- `networkx`


## Step-by-Step Guide

### Step 1: Assign n = 9

```python
n = 9
```

**Verification:**
```python
assert expected == actual
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(n)
```

### Step 3: Assign expected = value

```python
expected = 2 * sum((i * (n - i) for i in range(1, n // 2 + 1)))
```

### Step 4: Assign actual = nx.wiener_index(...)

```python
actual = nx.wiener_index(G)
```

**Verification:**
```python
assert expected == actual
```


## Complete Example

```python
# Workflow
n = 9
G = nx.path_graph(n)
expected = 2 * sum((i * (n - i) for i in range(1, n // 2 + 1)))
actual = nx.wiener_index(G)
assert expected == actual
```

## Next Steps


---

*Source: test_wiener.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*