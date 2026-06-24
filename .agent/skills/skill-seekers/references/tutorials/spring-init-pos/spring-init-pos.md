# How To: Spring Init Pos

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test spring init pos

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert not has_nan, 'values should not be nan'
```

### Step 2: Call G.add_edges_from()

```python
G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])
```

### Step 3: Assign init_pos = value

```python
init_pos = {0: (0.0, 0.0)}
```

### Step 4: Assign fixed_pos = value

```python
fixed_pos = [0]
```

### Step 5: Assign pos = nx.fruchterman_reingold_layout(...)

```python
pos = nx.fruchterman_reingold_layout(G, pos=init_pos, fixed=fixed_pos)
```

### Step 6: Assign has_nan = any(...)

```python
has_nan = any((math.isnan(c) for coords in pos.values() for c in coords))
```

**Verification:**
```python
assert not has_nan, 'values should not be nan'
```


## Complete Example

```python
# Workflow
import math
G = nx.Graph()
G.add_edges_from([(0, 1), (1, 2), (2, 0), (2, 3)])
init_pos = {0: (0.0, 0.0)}
fixed_pos = [0]
pos = nx.fruchterman_reingold_layout(G, pos=init_pos, fixed=fixed_pos)
has_nan = any((math.isnan(c) for coords in pos.values() for c in coords))
assert not has_nan, 'values should not be nan'
```

## Next Steps


---

*Source: test_layout.py:34 | Complexity: Intermediate | Last updated: 2026-06-02*