# How To: Union All Attributes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union all attributes

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
assert set(ghj.nodes()) == {'h0', 'h1', 'g0', 'g1', 'j0', 'j1'}
```

### Step 2: Call g.add_node()

```python
g.add_node(0, x=4)
```

**Verification:**
```python
assert ghj.nodes[n] == eval(graph).nodes[int(node)]
```

### Step 3: Call g.add_node()

```python
g.add_node(1, x=5)
```

**Verification:**
```python
assert ghj.graph['attr'] == 'attr'
```

### Step 4: Call g.add_edge()

```python
g.add_edge(0, 1, size=5)
```

**Verification:**
```python
assert ghj.graph['name'] == 'j'
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

### Step 10: Assign j = g.copy(...)

```python
j = g.copy()
```

### Step 11: Assign unknown = 'j'

```python
j.graph['name'] = 'j'
```

### Step 12: Assign unknown = 'attr'

```python
j.graph['attr'] = 'attr'
```

### Step 13: Assign unknown = 7

```python
j.nodes[0]['x'] = 7
```

### Step 14: Assign ghj = nx.union_all(...)

```python
ghj = nx.union_all([g, h, j], rename=('g', 'h', 'j'))
```

**Verification:**
```python
assert set(ghj.nodes()) == {'h0', 'h1', 'g0', 'g1', 'j0', 'j1'}
```

### Step 15: Assign unknown = n

```python
graph, node = n
```

**Verification:**
```python
assert ghj.nodes[n] == eval(graph).nodes[int(node)]
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
j = g.copy()
j.graph['name'] = 'j'
j.graph['attr'] = 'attr'
j.nodes[0]['x'] = 7
ghj = nx.union_all([g, h, j], rename=('g', 'h', 'j'))
assert set(ghj.nodes()) == {'h0', 'h1', 'g0', 'g1', 'j0', 'j1'}
for n in ghj:
    graph, node = n
    assert ghj.nodes[n] == eval(graph).nodes[int(node)]
assert ghj.graph['attr'] == 'attr'
assert ghj.graph['name'] == 'j'
```

## Next Steps


---

*Source: test_all.py:7 | Complexity: Advanced | Last updated: 2026-06-02*