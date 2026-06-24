# How To: Default Attribute

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test default attribute

## Prerequisites

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```

### Step 2: Call G.add_node()

```python
G.add_node(1, label='1', color='green')
```

**Verification:**
```python
assert sorted((sorted(e) for e in G.edges())) == sorted((sorted(e) for e in H.edges()))
```

### Step 3: Call nx.add_path()

```python
nx.add_path(G, [0, 1, 2, 3])
```

**Verification:**
```python
assert G.graph == H.graph
```

### Step 4: Call G.add_edge()

```python
G.add_edge(1, 2, foo=3)
```

### Step 5: Assign unknown = value

```python
G.graph['node_default'] = {'color': 'yellow'}
```

### Step 6: Assign unknown = value

```python
G.graph['edge_default'] = {'foo': 7}
```

### Step 7: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 8: Call nx.write_gexf()

```python
nx.write_gexf(G, fh)
```

### Step 9: Call fh.seek()

```python
fh.seek(0)
```

### Step 10: Assign H = nx.read_gexf(...)

```python
H = nx.read_gexf(fh, node_type=int)
```

**Verification:**
```python
assert sorted(G.nodes()) == sorted(H.nodes())
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_node(1, label='1', color='green')
nx.add_path(G, [0, 1, 2, 3])
G.add_edge(1, 2, foo=3)
G.graph['node_default'] = {'color': 'yellow'}
G.graph['edge_default'] = {'foo': 7}
fh = io.BytesIO()
nx.write_gexf(G, fh)
fh.seek(0)
H = nx.read_gexf(fh, node_type=int)
assert sorted(G.nodes()) == sorted(H.nodes())
assert sorted((sorted(e) for e in G.edges())) == sorted((sorted(e) for e in H.edges()))
del H.graph['mode']
assert G.graph == H.graph
```

## Next Steps


---

*Source: test_gexf.py:301 | Complexity: Advanced | Last updated: 2026-06-02*