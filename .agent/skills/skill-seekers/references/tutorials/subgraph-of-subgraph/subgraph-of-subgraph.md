# How To: Subgraph Of Subgraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subgraph of subgraph

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

### Step 1: Assign SGv = nx.subgraph(...)

```python
SGv = nx.subgraph(self.G, range(3, 7))
```

**Verification:**
```python
assert list(SG) == [4, 5, 6]
```

### Step 2: Assign SDGv = nx.subgraph(...)

```python
SDGv = nx.subgraph(self.DG, range(3, 7))
```

**Verification:**
```python
assert list(SSG) == [6]
```

### Step 3: Assign SMGv = nx.subgraph(...)

```python
SMGv = nx.subgraph(self.MG, range(3, 7))
```

**Verification:**
```python
assert SSG._graph is G
```

### Step 4: Assign SMDGv = nx.subgraph(...)

```python
SMDGv = nx.subgraph(self.MDG, range(3, 7))
```

### Step 5: Assign SG = nx.induced_subgraph(...)

```python
SG = nx.induced_subgraph(G, [4, 5, 6])
```

**Verification:**
```python
assert list(SG) == [4, 5, 6]
```

### Step 6: Assign SSG = SG.subgraph(...)

```python
SSG = SG.subgraph([6, 7])
```

**Verification:**
```python
assert list(SSG) == [6]
```


## Complete Example

```python
# Workflow
SGv = nx.subgraph(self.G, range(3, 7))
SDGv = nx.subgraph(self.DG, range(3, 7))
SMGv = nx.subgraph(self.MG, range(3, 7))
SMDGv = nx.subgraph(self.MDG, range(3, 7))
for G in self.graphs + [SGv, SDGv, SMGv, SMDGv]:
    SG = nx.induced_subgraph(G, [4, 5, 6])
    assert list(SG) == [4, 5, 6]
    SSG = SG.subgraph([6, 7])
    assert list(SSG) == [6]
    assert SSG._graph is G
```

## Next Steps


---

*Source: test_graphviews.py:210 | Complexity: Intermediate | Last updated: 2026-06-02*