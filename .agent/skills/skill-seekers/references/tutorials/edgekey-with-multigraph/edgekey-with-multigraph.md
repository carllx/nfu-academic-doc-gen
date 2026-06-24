# How To: Edgekey With Multigraph

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test edgekey with multigraph

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: edge_attr
```

## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'source': {'A': 'N1', 'B': 'N2', 'C': 'N1', 'D': 'N1'}, 'target': {'A': 'N2', 'B': 'N3', 'C': 'N1', 'D': 'N2'}, 'attr1': {'A': 'F1', 'B': 'F2', 'C': 'F3', 'D': 'F4'}, 'attr2': {'A': 1, 'B': 0, 'C': 0, 'D': 0}, 'attr3': {'A': 0, 'B': 1, 'C': 0, 'D': 1}})
```

**Verification:**
```python
assert graphs_equal(G, Gtrue)
```

### Step 2: Assign Gtrue = nx.MultiGraph(...)

```python
Gtrue = nx.MultiGraph([('N1', 'N2', 'F1', {'attr2': 1, 'attr3': 0}), ('N2', 'N3', 'F2', {'attr2': 0, 'attr3': 1}), ('N1', 'N1', 'F3', {'attr2': 0, 'attr3': 0}), ('N1', 'N2', 'F4', {'attr2': 0, 'attr3': 1})])
```

### Step 3: Assign G = nx.from_pandas_edgelist(...)

```python
G = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr=edge_attr, edge_key='attr1', create_using=nx.MultiGraph())
```

**Verification:**
```python
assert graphs_equal(G, Gtrue)
```

### Step 4: Assign df_roundtrip = nx.to_pandas_edgelist(...)

```python
df_roundtrip = nx.to_pandas_edgelist(G, edge_key='attr1')
```

### Step 5: Assign df_roundtrip = df_roundtrip.sort_values(...)

```python
df_roundtrip = df_roundtrip.sort_values('attr1')
```

### Step 6: Assign df_roundtrip.index = value

```python
df_roundtrip.index = ['A', 'B', 'C', 'D']
```

### Step 7: Call pd.testing.assert_frame_equal()

```python
pd.testing.assert_frame_equal(df, df_roundtrip[['source', 'target', 'attr1', 'attr2', 'attr3']])
```


## Complete Example

```python
# Setup
# Fixtures: edge_attr

# Workflow
df = pd.DataFrame({'source': {'A': 'N1', 'B': 'N2', 'C': 'N1', 'D': 'N1'}, 'target': {'A': 'N2', 'B': 'N3', 'C': 'N1', 'D': 'N2'}, 'attr1': {'A': 'F1', 'B': 'F2', 'C': 'F3', 'D': 'F4'}, 'attr2': {'A': 1, 'B': 0, 'C': 0, 'D': 0}, 'attr3': {'A': 0, 'B': 1, 'C': 0, 'D': 1}})
Gtrue = nx.MultiGraph([('N1', 'N2', 'F1', {'attr2': 1, 'attr3': 0}), ('N2', 'N3', 'F2', {'attr2': 0, 'attr3': 1}), ('N1', 'N1', 'F3', {'attr2': 0, 'attr3': 0}), ('N1', 'N2', 'F4', {'attr2': 0, 'attr3': 1})])
G = nx.from_pandas_edgelist(df, source='source', target='target', edge_attr=edge_attr, edge_key='attr1', create_using=nx.MultiGraph())
assert graphs_equal(G, Gtrue)
df_roundtrip = nx.to_pandas_edgelist(G, edge_key='attr1')
df_roundtrip = df_roundtrip.sort_values('attr1')
df_roundtrip.index = ['A', 'B', 'C', 'D']
pd.testing.assert_frame_equal(df, df_roundtrip[['source', 'target', 'attr1', 'attr2', 'attr3']])
```

## Next Steps


---

*Source: test_convert_pandas.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*