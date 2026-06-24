# How To: Issue 2127

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test from issue 2127

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.algorithms.bipartite.matching`


## Step-by-Step Guide

### Step 1: 'Test from issue 2127'

```python
'Test from issue 2127'
```

**Verification:**
```python
assert {'B', 'D', 'F', 'I', 'H'} == independent_set
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Call G.add_edge()

```python
G.add_edge('A', 'C')
```

### Step 4: Call G.add_edge()

```python
G.add_edge('A', 'B')
```

### Step 5: Call G.add_edge()

```python
G.add_edge('C', 'E')
```

### Step 6: Call G.add_edge()

```python
G.add_edge('C', 'D')
```

### Step 7: Call G.add_edge()

```python
G.add_edge('E', 'G')
```

### Step 8: Call G.add_edge()

```python
G.add_edge('E', 'F')
```

### Step 9: Call G.add_edge()

```python
G.add_edge('G', 'I')
```

### Step 10: Call G.add_edge()

```python
G.add_edge('G', 'H')
```

### Step 11: Assign tc = nx.transitive_closure(...)

```python
tc = nx.transitive_closure(G)
```

### Step 12: Assign btc = nx.Graph(...)

```python
btc = nx.Graph()
```

### Step 13: Assign top_nodes = value

```python
top_nodes = {n for n in btc if n[0] == 0}
```

### Step 14: Assign matching = hopcroft_karp_matching(...)

```python
matching = hopcroft_karp_matching(btc, top_nodes)
```

### Step 15: Assign vertex_cover = to_vertex_cover(...)

```python
vertex_cover = to_vertex_cover(btc, matching, top_nodes)
```

### Step 16: Assign independent_set = value

```python
independent_set = set(G) - {v for _, v in vertex_cover}
```

**Verification:**
```python
assert {'B', 'D', 'F', 'I', 'H'} == independent_set
```

### Step 17: Call btc.add_node()

```python
btc.add_node((0, v))
```

### Step 18: Call btc.add_node()

```python
btc.add_node((1, v))
```

### Step 19: Call btc.add_edge()

```python
btc.add_edge((0, u), (1, v))
```


## Complete Example

```python
# Workflow
'Test from issue 2127'
G = nx.DiGraph()
G.add_edge('A', 'C')
G.add_edge('A', 'B')
G.add_edge('C', 'E')
G.add_edge('C', 'D')
G.add_edge('E', 'G')
G.add_edge('E', 'F')
G.add_edge('G', 'I')
G.add_edge('G', 'H')
tc = nx.transitive_closure(G)
btc = nx.Graph()
for v in tc.nodes():
    btc.add_node((0, v))
    btc.add_node((1, v))
for u, v in tc.edges():
    btc.add_edge((0, u), (1, v))
top_nodes = {n for n in btc if n[0] == 0}
matching = hopcroft_karp_matching(btc, top_nodes)
vertex_cover = to_vertex_cover(btc, matching, top_nodes)
independent_set = set(G) - {v for _, v in vertex_cover}
assert {'B', 'D', 'F', 'I', 'H'} == independent_set
```

## Next Steps


---

*Source: test_matching.py:148 | Complexity: Advanced | Last updated: 2026-06-02*