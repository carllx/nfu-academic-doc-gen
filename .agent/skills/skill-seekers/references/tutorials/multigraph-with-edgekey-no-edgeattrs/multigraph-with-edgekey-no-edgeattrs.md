# How To: Multigraph With Edgekey No Edgeattrs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multigraph with edgekey no edgeattrs

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign Gtrue = nx.MultiGraph(...)

```python
Gtrue = nx.MultiGraph()
```

**Verification:**
```python
assert graphs_equal(Gtrue, G)
```

### Step 2: Call Gtrue.add_edge()

```python
Gtrue.add_edge(0, 1, key=0)
```

### Step 3: Call Gtrue.add_edge()

```python
Gtrue.add_edge(0, 1, key=3)
```

### Step 4: Assign df = nx.to_pandas_edgelist(...)

```python
df = nx.to_pandas_edgelist(Gtrue, edge_key='key')
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'source': [0, 0], 'target': [1, 1], 'key': [0, 3]})
```

### Step 6: Call pd.testing.assert_frame_equal()

```python
pd.testing.assert_frame_equal(expected, df)
```

### Step 7: Assign G = nx.from_pandas_edgelist(...)

```python
G = nx.from_pandas_edgelist(df, edge_key='key', create_using=nx.MultiGraph)
```

**Verification:**
```python
assert graphs_equal(Gtrue, G)
```


## Complete Example

```python
# Workflow
Gtrue = nx.MultiGraph()
Gtrue.add_edge(0, 1, key=0)
Gtrue.add_edge(0, 1, key=3)
df = nx.to_pandas_edgelist(Gtrue, edge_key='key')
expected = pd.DataFrame({'source': [0, 0], 'target': [1, 1], 'key': [0, 3]})
pd.testing.assert_frame_equal(expected, df)
G = nx.from_pandas_edgelist(df, edge_key='key', create_using=nx.MultiGraph)
assert graphs_equal(Gtrue, G)
```

## Next Steps


---

*Source: test_convert_pandas.py:303 | Complexity: Intermediate | Last updated: 2026-06-02*