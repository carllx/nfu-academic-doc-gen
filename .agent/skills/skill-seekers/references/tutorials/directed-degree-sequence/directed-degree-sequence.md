# How To: Directed Degree Sequence

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed degree sequence

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
n, r = (100, 10)
```

**Verification:**
```python
assert nx.is_digraphical(din, dout)
```

### Step 2: Assign p = value

```python
p = 1.0 / r
```

### Step 3: Assign G = nx.erdos_renyi_graph(...)

```python
G = nx.erdos_renyi_graph(n, p * (i + 1), None, True)
```

### Step 4: Assign din = value

```python
din = (d for n, d in G.in_degree())
```

### Step 5: Assign dout = value

```python
dout = (d for n, d in G.out_degree())
```

**Verification:**
```python
assert nx.is_digraphical(din, dout)
```


## Complete Example

```python
# Workflow
n, r = (100, 10)
p = 1.0 / r
for i in range(r):
    G = nx.erdos_renyi_graph(n, p * (i + 1), None, True)
    din = (d for n, d in G.in_degree())
    dout = (d for n, d in G.out_degree())
    assert nx.is_digraphical(din, dout)
```

## Next Steps


---

*Source: test_graphical.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*