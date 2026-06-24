# How To: Graph With Tuple Nodes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graph with tuple nodes

## Prerequisites

**Required Modules:**
- `json`
- `pytest`
- `networkx`
- `networkx.readwrite.json_graph`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert H.nodes[0, 0] == G.nodes[0, 0]
```

### Step 2: Call G.add_edge()

```python
G.add_edge((0, 0), (1, 0), color=[255, 255, 0])
```

**Verification:**
```python
assert H[0, 0][1, 0]['color'] == [255, 255, 0]
```

### Step 3: Assign d = node_link_data(...)

```python
d = node_link_data(G)
```

### Step 4: Assign dumped_d = json.dumps(...)

```python
dumped_d = json.dumps(d)
```

### Step 5: Assign dd = json.loads(...)

```python
dd = json.loads(dumped_d)
```

### Step 6: Assign H = node_link_graph(...)

```python
H = node_link_graph(dd)
```

**Verification:**
```python
assert H.nodes[0, 0] == G.nodes[0, 0]
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G.add_edge((0, 0), (1, 0), color=[255, 255, 0])
d = node_link_data(G)
dumped_d = json.dumps(d)
dd = json.loads(dumped_d)
H = node_link_graph(dd)
assert H.nodes[0, 0] == G.nodes[0, 0]
assert H[0, 0][1, 0]['color'] == [255, 255, 0]
```

## Next Steps


---

*Source: test_node_link.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*