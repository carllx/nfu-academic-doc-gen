# How To: Simple Node Match

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test simple node match

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms`

**Setup Required:**
```python
# Fixtures: graph_class
```

## Step-by-Step Guide

### Step 1: Assign g1 = graph_class(...)

```python
g1 = graph_class([(0, 0), (0, 1), (1, 0)])
```

**Verification:**
```python
assert is_isomorphic(g1, g2, node_match=nm)
```

### Step 2: Assign g2 = g1.copy(...)

```python
g2 = g1.copy()
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm)
```

### Step 3: Assign nm = iso.numerical_node_match(...)

```python
nm = iso.numerical_node_match('size', 1)
```

**Verification:**
```python
assert is_isomorphic(g1, g2, node_match=nm)
```

### Step 4: Assign unknown = 3

```python
g2.nodes[0]['size'] = 3
```

**Verification:**
```python
assert not is_isomorphic(g1, g2, node_match=nm)
```


## Complete Example

```python
# Setup
# Fixtures: graph_class

# Workflow
g1 = graph_class([(0, 0), (0, 1), (1, 0)])
g2 = g1.copy()
nm = iso.numerical_node_match('size', 1)
assert is_isomorphic(g1, g2, node_match=nm)
g2.nodes[0]['size'] = 3
assert not is_isomorphic(g1, g2, node_match=nm)
```

## Next Steps


---

*Source: test_ismags.py:612 | Complexity: Intermediate | Last updated: 2026-06-02*