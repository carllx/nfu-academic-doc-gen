# How To: Copy Multisubgraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test copy multisubgraph

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

### Step 1: Assign G = self.MG.copy(...)

```python
G = self.MG.copy()
```

**Verification:**
```python
assert hasattr(CSG, '_graph')
```

### Step 2: Assign SG = G.subgraph(...)

```python
SG = G.subgraph([4, 5, 6])
```

**Verification:**
```python
assert not hasattr(DCSG, '_graph')
```

### Step 3: Assign CSG = SG.copy(...)

```python
CSG = SG.copy(as_view=True)
```

### Step 4: Assign DCSG = SG.copy(...)

```python
DCSG = SG.copy(as_view=False)
```

**Verification:**
```python
assert hasattr(CSG, '_graph')
```


## Complete Example

```python
# Workflow
G = self.MG.copy()
SG = G.subgraph([4, 5, 6])
CSG = SG.copy(as_view=True)
DCSG = SG.copy(as_view=False)
assert hasattr(CSG, '_graph')
assert not hasattr(DCSG, '_graph')
```

## Next Steps


---

*Source: test_graphviews.py:321 | Complexity: Intermediate | Last updated: 2026-06-02*