# How To: Intersection All Attributes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection all attributes

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign g = nx.Graph(...)

```python
g = nx.Graph()
```

**Verification:**
```python
assert set(gh.nodes()) == set(g.nodes())
```

### Step 2: Call g.add_node()

```python
g.add_node(0, x=4)
```

**Verification:**
```python
assert set(gh.nodes()) == set(h.nodes())
```

### Step 3: Call g.add_node()

```python
g.add_node(1, x=5)
```

**Verification:**
```python
assert sorted(gh.edges()) == sorted(g.edges())
```

### Step 4: Call g.add_edge()

```python
g.add_edge(0, 1, size=5)
```

### Step 5: Assign unknown = 'g'

```python
g.graph['name'] = 'g'
```

### Step 6: Assign h = g.copy(...)

```python
h = g.copy()
```

### Step 7: Assign unknown = 'h'

```python
h.graph['name'] = 'h'
```

### Step 8: Assign unknown = 'attr'

```python
h.graph['attr'] = 'attr'
```

### Step 9: Assign unknown = 7

```python
h.nodes[0]['x'] = 7
```

### Step 10: Assign gh = nx.intersection_all(...)

```python
gh = nx.intersection_all([g, h])
```

**Verification:**
```python
assert set(gh.nodes()) == set(g.nodes())
```


## Complete Example

```python
# Workflow
g = nx.Graph()
g.add_node(0, x=4)
g.add_node(1, x=5)
g.add_edge(0, 1, size=5)
g.graph['name'] = 'g'
h = g.copy()
h.graph['name'] = 'h'
h.graph['attr'] = 'attr'
h.nodes[0]['x'] = 7
gh = nx.intersection_all([g, h])
assert set(gh.nodes()) == set(g.nodes())
assert set(gh.nodes()) == set(h.nodes())
assert sorted(gh.edges()) == sorted(g.edges())
```

## Next Steps


---

*Source: test_all.py:73 | Complexity: Advanced | Last updated: 2026-06-02*