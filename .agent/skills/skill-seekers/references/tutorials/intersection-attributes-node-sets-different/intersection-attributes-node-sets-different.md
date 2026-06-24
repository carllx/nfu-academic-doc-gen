# How To: Intersection Attributes Node Sets Different

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection attributes node sets different

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
assert set(gh.nodes()) == set(h.nodes())
```

### Step 2: Call g.add_node()

```python
g.add_node(0, x=4)
```

**Verification:**
```python
assert sorted(gh.edges()) == sorted(g.edges())
```

### Step 3: Call g.add_node()

```python
g.add_node(1, x=5)
```

### Step 4: Call g.add_node()

```python
g.add_node(2, x=3)
```

### Step 5: Call g.add_edge()

```python
g.add_edge(0, 1, size=5)
```

### Step 6: Assign unknown = 'g'

```python
g.graph['name'] = 'g'
```

### Step 7: Assign h = g.copy(...)

```python
h = g.copy()
```

### Step 8: Assign unknown = 'h'

```python
h.graph['name'] = 'h'
```

### Step 9: Assign unknown = 'attr'

```python
h.graph['attr'] = 'attr'
```

### Step 10: Assign unknown = 7

```python
h.nodes[0]['x'] = 7
```

### Step 11: Call h.remove_node()

```python
h.remove_node(2)
```

### Step 12: Assign gh = nx.intersection(...)

```python
gh = nx.intersection(g, h)
```

**Verification:**
```python
assert set(gh.nodes()) == set(h.nodes())
```


## Complete Example

```python
# Workflow
g = nx.Graph()
g.add_node(0, x=4)
g.add_node(1, x=5)
g.add_node(2, x=3)
g.add_edge(0, 1, size=5)
g.graph['name'] = 'g'
h = g.copy()
h.graph['name'] = 'h'
h.graph['attr'] = 'attr'
h.nodes[0]['x'] = 7
h.remove_node(2)
gh = nx.intersection(g, h)
assert set(gh.nodes()) == set(h.nodes())
assert sorted(gh.edges()) == sorted(g.edges())
```

## Next Steps


---

*Source: test_binary.py:76 | Complexity: Advanced | Last updated: 2026-06-02*