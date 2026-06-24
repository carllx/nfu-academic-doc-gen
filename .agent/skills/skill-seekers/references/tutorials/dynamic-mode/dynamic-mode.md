# How To: Dynamic Mode

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dynamic mode

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

### Step 3: Assign unknown = 'dynamic'

```python
G.graph['mode'] = 'dynamic'
```

### Step 4: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 5: Call nx.write_gexf()

```python
nx.write_gexf(G, fh)
```

### Step 6: Call fh.seek()

```python
fh.seek(0)
```

### Step 7: Assign H = nx.read_gexf(...)

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
G.graph['mode'] = 'dynamic'
fh = io.BytesIO()
nx.write_gexf(G, fh)
fh.seek(0)
H = nx.read_gexf(fh, node_type=int)
assert sorted(G.nodes()) == sorted(H.nodes())
assert sorted((sorted(e) for e in G.edges())) == sorted((sorted(e) for e in H.edges()))
```

## Next Steps


---

*Source: test_gexf.py:503 | Complexity: Intermediate | Last updated: 2026-06-02*