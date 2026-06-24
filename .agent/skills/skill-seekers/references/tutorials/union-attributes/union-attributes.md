# How To: Union Attributes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union attributes

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
assert set(gh.nodes()) == {'h0', 'h1', 'g0', 'g1'}
```

### Step 2: Call g.add_node()

```python
g.add_node(0, x=4)
```

**Verification:**
```python
assert gh.nodes[n] == eval(graph).nodes[int(node)]
```

### Step 3: Call g.add_node()

```python
g.add_node(1, x=5)
```

**Verification:**
```python
assert gh.graph['attr'] == 'attr'
```

### Step 4: Call g.add_edge()

```python
g.add_edge(0, 1, size=5)
```

**Verification:**
```python
assert gh.graph['name'] == 'h'
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

### Step 10: Assign gh = nx.union(...)

```python
gh = nx.union(g, h, rename=('g', 'h'))
```

**Verification:**
```python
assert set(gh.nodes()) == {'h0', 'h1', 'g0', 'g1'}
```

### Step 11: Assign unknown = n

```python
graph, node = n
```

**Verification:**
```python
assert gh.nodes[n] == eval(graph).nodes[int(node)]
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
gh = nx.union(g, h, rename=('g', 'h'))
assert set(gh.nodes()) == {'h0', 'h1', 'g0', 'g1'}
for n in gh:
    graph, node = n
    assert gh.nodes[n] == eval(graph).nodes[int(node)]
assert gh.graph['attr'] == 'attr'
assert gh.graph['name'] == 'h'
```

## Next Steps


---

*Source: test_binary.py:7 | Complexity: Advanced | Last updated: 2026-06-02*