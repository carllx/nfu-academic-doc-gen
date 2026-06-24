# How To: Trophic Levels Singular With Basal

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Should fail to compute if there are any parts of the graph which are not
reachable from any basal node (with in-degree zero).

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: 'Should fail to compute if there are any parts of the graph which are not\n    reachable from any basal node (with in-degree zero).\n    '

```python
'Should fail to compute if there are any parts of the graph which are not\n    reachable from any basal node (with in-degree zero).\n    '
```

**Verification:**
```python
assert msg in str(e.value)
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert msg in str(e.value)
```

### Step 3: Call G.add_edge()

```python
G.add_edge('a', 'b')
```

### Step 4: Call G.add_edge()

```python
G.add_edge('c', 'b')
```

### Step 5: Call G.add_edge()

```python
G.add_edge('d', 'b')
```

### Step 6: Call G.add_edge()

```python
G.add_edge('c', 'd')
```

### Step 7: Call G.add_edge()

```python
G.add_edge('d', 'c')
```

### Step 8: Assign msg = value

```python
msg = 'Trophic levels are only defined for graphs where every node ' + 'has a path from a basal node (basal nodes are nodes with no ' + 'incoming edges).'
```

**Verification:**
```python
assert msg in str(e.value)
```

### Step 9: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 10: Call G.add_edge()

```python
G.add_edge('a', 'b')
```

### Step 11: Call G.add_edge()

```python
G.add_edge('c', 'b')
```

### Step 12: Call G.add_edge()

```python
G.add_edge('c', 'c')
```

### Step 13: Assign msg = value

```python
msg = 'Trophic levels are only defined for graphs where every node ' + 'has a path from a basal node (basal nodes are nodes with no ' + 'incoming edges).'
```

**Verification:**
```python
assert msg in str(e.value)
```

### Step 14: Call nx.trophic_levels()

```python
nx.trophic_levels(G)
```

### Step 15: Call nx.trophic_levels()

```python
nx.trophic_levels(G)
```


## Complete Example

```python
# Workflow
'Should fail to compute if there are any parts of the graph which are not\n    reachable from any basal node (with in-degree zero).\n    '
G = nx.DiGraph()
G.add_edge('a', 'b')
G.add_edge('c', 'b')
G.add_edge('d', 'b')
G.add_edge('c', 'd')
G.add_edge('d', 'c')
with pytest.raises(nx.NetworkXError) as e:
    nx.trophic_levels(G)
msg = 'Trophic levels are only defined for graphs where every node ' + 'has a path from a basal node (basal nodes are nodes with no ' + 'incoming edges).'
assert msg in str(e.value)
G = nx.DiGraph()
G.add_edge('a', 'b')
G.add_edge('c', 'b')
G.add_edge('c', 'c')
with pytest.raises(nx.NetworkXError) as e:
    nx.trophic_levels(G)
msg = 'Trophic levels are only defined for graphs where every node ' + 'has a path from a basal node (basal nodes are nodes with no ' + 'incoming edges).'
assert msg in str(e.value)
```

## Next Steps


---

*Source: test_trophic.py:153 | Complexity: Advanced | Last updated: 2026-06-02*