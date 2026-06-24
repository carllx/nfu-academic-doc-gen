# How To: Single Bridge

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test single bridge

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (1, 3), (1, 4), (2, 5), (5, 10), (6, 8)]
```

**Verification:**
```python
assert bridges == [(5, 6)]
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph(edges)
```

### Step 3: Assign source = 1

```python
source = 1
```

### Step 4: Assign bridges = list(...)

```python
bridges = list(nx.bridges(G, source))
```

**Verification:**
```python
assert bridges == [(5, 6)]
```


## Complete Example

```python
# Workflow
edges = [(1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (6, 7), (7, 8), (5, 9), (9, 10), (1, 3), (1, 4), (2, 5), (5, 10), (6, 8)]
G = nx.Graph(edges)
source = 1
bridges = list(nx.bridges(G, source))
assert bridges == [(5, 6)]
```

## Next Steps


---

*Source: test_bridges.py:11 | Complexity: Intermediate | Last updated: 2026-06-02*