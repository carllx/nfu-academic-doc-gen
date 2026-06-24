# How To: Morphic And Number Of Mappings

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test morphic and number of mappings

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
# Fixtures: graph_class, numb_maps
```

## Step-by-Step Guide

### Step 1: Assign g1 = graph_class(...)

```python
g1 = graph_class(self.g1edges)
```

**Verification:**
```python
assert gm.is_isomorphic()
```

### Step 2: Assign g2 = graph_class(...)

```python
g2 = graph_class(self.g2edges)
```

**Verification:**
```python
assert gm.subgraph_is_monomorphic()
```

### Step 3: Assign Matcher = value

```python
Matcher = iso.DiGraphMatcher if g1.is_directed() else iso.GraphMatcher
```

**Verification:**
```python
assert gm.subgraph_is_isomorphic()
```

### Step 4: Assign gm = Matcher(...)

```python
gm = Matcher(g1, g2)
```

**Verification:**
```python
assert len(all_mappings) == numb_maps
```

### Step 5: Assign mapping = list(...)

```python
mapping = list(gm.mapping.items())
```

**Verification:**
```python
assert dict(mapping) in all_mappings
```

### Step 6: Assign all_mappings = list(...)

```python
all_mappings = list(gm.isomorphisms_iter())
```

**Verification:**
```python
assert len(all_mappings) == numb_maps
```


## Complete Example

```python
# Setup
# Fixtures: graph_class, numb_maps

# Workflow
g1 = graph_class(self.g1edges)
g2 = graph_class(self.g2edges)
Matcher = iso.DiGraphMatcher if g1.is_directed() else iso.GraphMatcher
gm = Matcher(g1, g2)
assert gm.is_isomorphic()
assert gm.subgraph_is_monomorphic()
assert gm.subgraph_is_isomorphic()
mapping = list(gm.mapping.items())
all_mappings = list(gm.isomorphisms_iter())
assert len(all_mappings) == numb_maps
assert dict(mapping) in all_mappings
```

## Next Steps


---

*Source: test_isomorphvf2.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*