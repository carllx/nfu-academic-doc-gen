# How To: Directed Weighted

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test directed weighted

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert expected == pytest.approx(actual, abs=1e-07)
```

### Step 2: Call G.add_edge()

```python
G.add_edge('A', 'B', weight=5)
```

### Step 3: Call G.add_edge()

```python
G.add_edge('B', 'C', weight=1)
```

### Step 4: Call G.add_edge()

```python
G.add_edge('B', 'D', weight=0.25)
```

### Step 5: Call G.add_edge()

```python
G.add_edge('D', 'E', weight=1)
```

### Step 6: Assign denom = value

```python
denom = len(G) - 1
```

### Step 7: Assign A_local = value

```python
A_local = sum([5, 3, 2.625, 2.0833333333333]) / denom
```

### Step 8: Assign B_local = value

```python
B_local = sum([1, 0.25, 0.625]) / denom
```

### Step 9: Assign C_local = 0

```python
C_local = 0
```

### Step 10: Assign D_local = value

```python
D_local = sum([1]) / denom
```

### Step 11: Assign E_local = 0

```python
E_local = 0
```

### Step 12: Assign local_reach_ctrs = value

```python
local_reach_ctrs = [A_local, C_local, B_local, D_local, E_local]
```

### Step 13: Assign max_local = max(...)

```python
max_local = max(local_reach_ctrs)
```

### Step 14: Assign expected = value

```python
expected = sum((max_local - lrc for lrc in local_reach_ctrs)) / denom
```

### Step 15: Assign grc = value

```python
grc = nx.global_reaching_centrality
```

### Step 16: Assign actual = grc(...)

```python
actual = grc(G, normalized=False, weight='weight')
```

**Verification:**
```python
assert expected == pytest.approx(actual, abs=1e-07)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_edge('A', 'B', weight=5)
G.add_edge('B', 'C', weight=1)
G.add_edge('B', 'D', weight=0.25)
G.add_edge('D', 'E', weight=1)
denom = len(G) - 1
A_local = sum([5, 3, 2.625, 2.0833333333333]) / denom
B_local = sum([1, 0.25, 0.625]) / denom
C_local = 0
D_local = sum([1]) / denom
E_local = 0
local_reach_ctrs = [A_local, C_local, B_local, D_local, E_local]
max_local = max(local_reach_ctrs)
expected = sum((max_local - lrc for lrc in local_reach_ctrs)) / denom
grc = nx.global_reaching_centrality
actual = grc(G, normalized=False, weight='weight')
assert expected == pytest.approx(actual, abs=1e-07)
```

## Next Steps


---

*Source: test_reaching.py:62 | Complexity: Advanced | Last updated: 2026-06-02*