# How To: From Adjacency Named

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from adjacency named

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = {'A': {'A': 0, 'B': 0, 'C': 0}, 'B': {'A': 1, 'B': 0, 'C': 0}, 'C': {'A': 0, 'B': 1, 'C': 0}}
```

### Step 2: Assign dftrue = pd.DataFrame(...)

```python
dftrue = pd.DataFrame(data, dtype=np.intp)
```

### Step 3: Assign df = value

```python
df = dftrue[['A', 'C', 'B']]
```

### Step 4: Assign G = nx.from_pandas_adjacency(...)

```python
G = nx.from_pandas_adjacency(df, create_using=nx.DiGraph())
```

### Step 5: Assign df = nx.to_pandas_adjacency(...)

```python
df = nx.to_pandas_adjacency(G, dtype=np.intp)
```

### Step 6: Call pd.testing.assert_frame_equal()

```python
pd.testing.assert_frame_equal(df, dftrue)
```


## Complete Example

```python
# Workflow
data = {'A': {'A': 0, 'B': 0, 'C': 0}, 'B': {'A': 1, 'B': 0, 'C': 0}, 'C': {'A': 0, 'B': 1, 'C': 0}}
dftrue = pd.DataFrame(data, dtype=np.intp)
df = dftrue[['A', 'C', 'B']]
G = nx.from_pandas_adjacency(df, create_using=nx.DiGraph())
df = nx.to_pandas_adjacency(G, dtype=np.intp)
pd.testing.assert_frame_equal(df, dftrue)
```

## Next Steps


---

*Source: test_convert_pandas.py:231 | Complexity: Intermediate | Last updated: 2026-06-02*