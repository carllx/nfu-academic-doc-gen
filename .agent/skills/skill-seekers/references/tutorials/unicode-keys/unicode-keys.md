# How To: Unicode Keys

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unicode keys

## Prerequisites

**Required Modules:**
- `json`
- `pytest`
- `networkx`
- `networkx.readwrite.json_graph`


## Step-by-Step Guide

### Step 1: Assign q = 'qualité'

```python
q = 'qualité'
```

**Verification:**
```python
assert H.nodes[1][q] == q
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_node()

```python
G.add_node(1, **{q: q})
```

### Step 4: Assign s = node_link_data(...)

```python
s = node_link_data(G)
```

### Step 5: Assign output = json.dumps(...)

```python
output = json.dumps(s, ensure_ascii=False)
```

### Step 6: Assign data = json.loads(...)

```python
data = json.loads(output)
```

### Step 7: Assign H = node_link_graph(...)

```python
H = node_link_graph(data)
```

**Verification:**
```python
assert H.nodes[1][q] == q
```


## Complete Example

```python
# Workflow
q = 'qualité'
G = nx.Graph()
G.add_node(1, **{q: q})
s = node_link_data(G)
output = json.dumps(s, ensure_ascii=False)
data = json.loads(output)
H = node_link_graph(data)
assert H.nodes[1][q] == q
```

## Next Steps


---

*Source: test_node_link.py:62 | Complexity: Intermediate | Last updated: 2026-06-02*