# How To: From Adjacency

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from adjacency

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign nodelist = value

```python
nodelist = [1, 2]
```

### Step 2: Assign dftrue = pd.DataFrame(...)

```python
dftrue = pd.DataFrame([[1, 1], [1, 0]], dtype=int, index=nodelist, columns=nodelist)
```

### Step 3: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 1), (1, 2)])
```

### Step 4: Assign df = nx.to_pandas_adjacency(...)

```python
df = nx.to_pandas_adjacency(G, dtype=int)
```

### Step 5: Call pd.testing.assert_frame_equal()

```python
pd.testing.assert_frame_equal(df, dftrue)
```


## Complete Example

```python
# Workflow
nodelist = [1, 2]
dftrue = pd.DataFrame([[1, 1], [1, 0]], dtype=int, index=nodelist, columns=nodelist)
G = nx.Graph([(1, 1), (1, 2)])
df = nx.to_pandas_adjacency(G, dtype=int)
pd.testing.assert_frame_equal(df, dftrue)
```

## Next Steps


---

*Source: test_convert_pandas.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*