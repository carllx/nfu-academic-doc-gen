# How To: Subgraph Edgesubgraph Toundirected

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subgraph edgesubgraph toundirected

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`
- `pickle`
- `pickle`
- `pickle`
- `pickle`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign G = self.G.copy(...)

```python
G = self.G.copy()
```

**Verification:**
```python
assert list(USSG) == [4, 5]
```

### Step 2: Assign SG = G.subgraph(...)

```python
SG = G.subgraph([4, 5, 6])
```

**Verification:**
```python
assert sorted(USSG.edges) == [(4, 5)]
```

### Step 3: Assign SSG = SG.edge_subgraph(...)

```python
SSG = SG.edge_subgraph([(4, 5), (5, 4)])
```

### Step 4: Assign USSG = SSG.to_undirected(...)

```python
USSG = SSG.to_undirected()
```

**Verification:**
```python
assert list(USSG) == [4, 5]
```


## Complete Example

```python
# Workflow
G = self.G.copy()
SG = G.subgraph([4, 5, 6])
SSG = SG.edge_subgraph([(4, 5), (5, 4)])
USSG = SSG.to_undirected()
assert list(USSG) == [4, 5]
assert sorted(USSG.edges) == [(4, 5)]
```

## Next Steps


---

*Source: test_graphviews.py:289 | Complexity: Intermediate | Last updated: 2026-06-02*