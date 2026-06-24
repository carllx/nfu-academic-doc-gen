# How To: Simple List

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test simple list

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
assert H.nodes[1]['networkx_key'] == list_value
```

### Step 2: Assign list_value = value

```python
list_value = [(1, 2, 3), (9, 1, 2)]
```

### Step 3: Call G.add_node()

```python
G.add_node(1, key=list_value)
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
assert H.nodes[1]['networkx_key'] == list_value
```


## Complete Example

```python
# Workflow
G = nx.Graph()
list_value = [(1, 2, 3), (9, 1, 2)]
G.add_node(1, key=list_value)
fh = io.BytesIO()
nx.write_gexf(G, fh)
fh.seek(0)
H = nx.read_gexf(fh, node_type=int)
assert H.nodes[1]['networkx_key'] == list_value
```

## Next Steps


---

*Source: test_gexf.py:493 | Complexity: Intermediate | Last updated: 2026-06-02*