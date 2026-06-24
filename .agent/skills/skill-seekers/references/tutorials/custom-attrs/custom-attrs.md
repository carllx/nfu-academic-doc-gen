# How To: Custom Attrs

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test custom attrs

## Prerequisites

**Required Modules:**
- `json`
- `pytest`
- `networkx`
- `networkx.readwrite.json_graph`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(4)
```

**Verification:**
```python
assert nx.is_isomorphic(G, H)
```

### Step 2: Call G.add_node()

```python
G.add_node(1, color='red')
```

**Verification:**
```python
assert H.graph['foo'] == 'bar'
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 2, width=7)
```

**Verification:**
```python
assert H.nodes[1]['color'] == 'red'
```

### Step 4: Assign unknown = 'one'

```python
G.graph[1] = 'one'
```

**Verification:**
```python
assert H[1][2]['width'] == 7
```

### Step 5: Assign unknown = 'bar'

```python
G.graph['foo'] = 'bar'
```

### Step 6: Assign attrs = value

```python
attrs = {'source': 'c_source', 'target': 'c_target', 'name': 'c_id', 'key': 'c_key', 'edges': 'c_links'}
```

### Step 7: Assign H = node_link_graph(...)

```python
H = node_link_graph(node_link_data(G, **attrs), multigraph=False, **attrs)
```

**Verification:**
```python
assert nx.is_isomorphic(G, H)
```


## Complete Example

```python
# Workflow
G = nx.path_graph(4)
G.add_node(1, color='red')
G.add_edge(1, 2, width=7)
G.graph[1] = 'one'
G.graph['foo'] = 'bar'
attrs = {'source': 'c_source', 'target': 'c_target', 'name': 'c_id', 'key': 'c_key', 'edges': 'c_links'}
H = node_link_graph(node_link_data(G, **attrs), multigraph=False, **attrs)
assert nx.is_isomorphic(G, H)
assert H.graph['foo'] == 'bar'
assert H.nodes[1]['color'] == 'red'
assert H[1][2]['width'] == 7
```

## Next Steps


---

*Source: test_node_link.py:90 | Complexity: Intermediate | Last updated: 2026-06-02*