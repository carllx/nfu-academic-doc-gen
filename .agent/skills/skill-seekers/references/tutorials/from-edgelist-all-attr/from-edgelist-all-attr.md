# How To: From Edgelist All Attr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from edgelist all attr

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign Gtrue = nx.Graph(...)

```python
Gtrue = nx.Graph([('E', 'C', {'cost': 9, 'weight': 10}), ('B', 'A', {'cost': 1, 'weight': 7}), ('A', 'D', {'cost': 7, 'weight': 4})])
```

**Verification:**
```python
assert graphs_equal(G, Gtrue)
```

### Step 2: Assign G = nx.from_pandas_edgelist(...)

```python
G = nx.from_pandas_edgelist(self.df, 0, 'b', True)
```

**Verification:**
```python
assert graphs_equal(MG, MGtrue)
```

### Step 3: Assign MGtrue = nx.MultiGraph(...)

```python
MGtrue = nx.MultiGraph(Gtrue)
```

### Step 4: Call MGtrue.add_edge()

```python
MGtrue.add_edge('A', 'D', cost=16, weight=4)
```

### Step 5: Assign MG = nx.from_pandas_edgelist(...)

```python
MG = nx.from_pandas_edgelist(self.mdf, 0, 'b', True, nx.MultiGraph())
```

**Verification:**
```python
assert graphs_equal(MG, MGtrue)
```


## Complete Example

```python
# Workflow
Gtrue = nx.Graph([('E', 'C', {'cost': 9, 'weight': 10}), ('B', 'A', {'cost': 1, 'weight': 7}), ('A', 'D', {'cost': 7, 'weight': 4})])
G = nx.from_pandas_edgelist(self.df, 0, 'b', True)
assert graphs_equal(G, Gtrue)
MGtrue = nx.MultiGraph(Gtrue)
MGtrue.add_edge('A', 'D', cost=16, weight=4)
MG = nx.from_pandas_edgelist(self.mdf, 0, 'b', True, nx.MultiGraph())
assert graphs_equal(MG, MGtrue)
```

## Next Steps


---

*Source: test_convert_pandas.py:32 | Complexity: Intermediate | Last updated: 2026-06-02*