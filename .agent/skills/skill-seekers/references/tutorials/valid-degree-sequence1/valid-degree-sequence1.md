# How To: Valid Degree Sequence1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test valid degree sequence1

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign n = 100

```python
n = 100
```

**Verification:**
```python
assert nx.is_graphical(deg, method='eg')
```

### Step 2: Assign p = 0.3

```python
p = 0.3
```

**Verification:**
```python
assert nx.is_graphical(deg, method='hh')
```

### Step 3: Assign G = nx.erdos_renyi_graph(...)

```python
G = nx.erdos_renyi_graph(n, p)
```

### Step 4: Assign deg = value

```python
deg = (d for n, d in G.degree())
```

**Verification:**
```python
assert nx.is_graphical(deg, method='eg')
```


## Complete Example

```python
# Workflow
n = 100
p = 0.3
for i in range(10):
    G = nx.erdos_renyi_graph(n, p)
    deg = (d for n, d in G.degree())
    assert nx.is_graphical(deg, method='eg')
    assert nx.is_graphical(deg, method='hh')
```

## Next Steps


---

*Source: test_graphical.py:6 | Complexity: Intermediate | Last updated: 2026-06-02*