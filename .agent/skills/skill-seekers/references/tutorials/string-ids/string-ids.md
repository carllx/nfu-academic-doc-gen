# How To: String Ids

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test string ids

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
assert data['edges'][0]['source'] == 'A'
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert data['edges'][0]['target'] == q
```

### Step 3: Call G.add_node()

```python
G.add_node('A')
```

**Verification:**
```python
assert nx.is_isomorphic(G, H)
```

### Step 4: Call G.add_node()

```python
G.add_node(q)
```

### Step 5: Call G.add_edge()

```python
G.add_edge('A', q)
```

### Step 6: Assign data = node_link_data(...)

```python
data = node_link_data(G)
```

**Verification:**
```python
assert data['edges'][0]['source'] == 'A'
```

### Step 7: Assign H = node_link_graph(...)

```python
H = node_link_graph(data)
```

**Verification:**
```python
assert nx.is_isomorphic(G, H)
```


## Complete Example

```python
# Workflow
q = 'qualité'
G = nx.DiGraph()
G.add_node('A')
G.add_node(q)
G.add_edge('A', q)
data = node_link_data(G)
assert data['edges'][0]['source'] == 'A'
assert data['edges'][0]['target'] == q
H = node_link_graph(data)
assert nx.is_isomorphic(G, H)
```

## Next Steps


---

*Source: test_node_link.py:78 | Complexity: Intermediate | Last updated: 2026-06-02*