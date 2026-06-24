# How To: Subgraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subgraph

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `importlib.resources`
- `random`
- `struct`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.generators`

**Setup Required:**
```python
# Fixtures: graph_class
```

## Step-by-Step Guide

### Step 1: Assign g1 = graph_class(...)

```python
g1 = graph_class(self.g1edges)
```

**Verification:**
```python
assert not gm.is_isomorphic()
```

### Step 2: Assign g2 = graph_class(...)

```python
g2 = graph_class(self.g2edges)
```

**Verification:**
```python
assert gm.subgraph_is_isomorphic()
```

### Step 3: Assign g3 = g2.subgraph(...)

```python
g3 = g2.subgraph([1, 2, 3, 4])
```

**Verification:**
```python
assert gm.subgraph_is_monomorphic()
```

### Step 4: Assign Matcher = value

```python
Matcher = iso.DiGraphMatcher if g1.is_directed() else iso.GraphMatcher
```

### Step 5: Assign gm = Matcher(...)

```python
gm = Matcher(g1, g3)
```

**Verification:**
```python
assert not gm.is_isomorphic()
```


## Complete Example

```python
# Setup
# Fixtures: graph_class

# Workflow
g1 = graph_class(self.g1edges)
g2 = graph_class(self.g2edges)
g3 = g2.subgraph([1, 2, 3, 4])
Matcher = iso.DiGraphMatcher if g1.is_directed() else iso.GraphMatcher
gm = Matcher(g1, g3)
assert not gm.is_isomorphic()
assert gm.subgraph_is_isomorphic()
assert gm.subgraph_is_monomorphic()
```

## Next Steps


---

*Source: test_isomorphvf2.py:72 | Complexity: Intermediate | Last updated: 2026-06-02*