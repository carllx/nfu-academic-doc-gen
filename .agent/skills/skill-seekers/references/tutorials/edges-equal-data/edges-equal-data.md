# How To: Edges Equal Data

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test whether ``edges_equal`` properly compares edges with attribute dictionaries.

## Prerequisites

**Required Modules:**
- `random`
- `copy`
- `pytest`
- `networkx`
- `networkx.utils`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: 'Test whether ``edges_equal`` properly compares edges with attribute dictionaries.'

```python
'Test whether ``edges_equal`` properly compares edges with attribute dictionaries.'
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), G.edges(data=True))
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

**Verification:**
```python
assert not edges_equal(G.edges(data=True), G.edges())
```

### Step 3: Assign H = nx.path_graph(...)

```python
H = nx.path_graph(3)
```

**Verification:**
```python
assert edges_equal(G.edges(), H.edges())
```

### Step 4: Assign I = nx.path_graph(...)

```python
I = nx.path_graph(3, create_using=nx.MultiGraph)
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), H.edges(data=True))
```

### Step 5: Assign attrs = value

```python
attrs = {(0, 1): {'attr1': 20, 'attr2': 'nothing'}, (1, 2): {'attr2': 3}}
```

**Verification:**
```python
assert edges_equal(G.edges(), H.edges())
```

### Step 6: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(G, attrs)
```

**Verification:**
```python
assert not edges_equal(G.edges(data=True), H.edges(data=True))
```

### Step 7: Call nx.set_edge_attributes()

```python
nx.set_edge_attributes(H, attrs)
```

**Verification:**
```python
assert edges_equal(G.edges(), H.edges())
```

### Step 8: Assign unknown = 'something'

```python
H[0][1]['attr2'] = 'something'
```

**Verification:**
```python
assert edges_equal(G.edges(), H.edges())
```


## Complete Example

```python
# Workflow
'Test whether ``edges_equal`` properly compares edges with attribute dictionaries.'
G = nx.path_graph(3)
H = nx.path_graph(3)
I = nx.path_graph(3, create_using=nx.MultiGraph)
attrs = {(0, 1): {'attr1': 20, 'attr2': 'nothing'}, (1, 2): {'attr2': 3}}
nx.set_edge_attributes(G, attrs)
assert edges_equal(G.edges(data=True), G.edges(data=True))
assert not edges_equal(G.edges(data=True), G.edges())
nx.set_edge_attributes(H, attrs)
assert edges_equal(G.edges(), H.edges())
assert edges_equal(G.edges(data=True), H.edges(data=True))
H[0][1]['attr2'] = 'something'
assert edges_equal(G.edges(), H.edges())
assert not edges_equal(G.edges(data=True), H.edges(data=True))
```

## Next Steps


---

*Source: test_misc.py:333 | Complexity: Advanced | Last updated: 2026-06-02*