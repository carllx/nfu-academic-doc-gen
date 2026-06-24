# How To: Intersection All

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test intersection all

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert set(I.nodes()) == {1, 2, 3, 4}
```

### Step 2: Assign H = nx.Graph(...)

```python
H = nx.Graph()
```

**Verification:**
```python
assert sorted(I.edges()) == [(2, 3)]
```

### Step 3: Assign R = nx.Graph(...)

```python
R = nx.Graph(awesome=True)
```

**Verification:**
```python
assert I.graph == {}
```

### Step 4: Call G.add_nodes_from()

```python
G.add_nodes_from([1, 2, 3, 4])
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 2)
```

### Step 6: Call G.add_edge()

```python
G.add_edge(2, 3)
```

### Step 7: Call H.add_nodes_from()

```python
H.add_nodes_from([1, 2, 3, 4])
```

### Step 8: Call H.add_edge()

```python
H.add_edge(2, 3)
```

### Step 9: Call H.add_edge()

```python
H.add_edge(3, 4)
```

### Step 10: Call R.add_nodes_from()

```python
R.add_nodes_from([1, 2, 3, 4])
```

### Step 11: Call R.add_edge()

```python
R.add_edge(2, 3)
```

### Step 12: Call R.add_edge()

```python
R.add_edge(4, 1)
```

### Step 13: Assign I = nx.intersection_all(...)

```python
I = nx.intersection_all([G, H, R])
```

**Verification:**
```python
assert set(I.nodes()) == {1, 2, 3, 4}
```


## Complete Example

```python
# Workflow
G = nx.Graph()
H = nx.Graph()
R = nx.Graph(awesome=True)
G.add_nodes_from([1, 2, 3, 4])
G.add_edge(1, 2)
G.add_edge(2, 3)
H.add_nodes_from([1, 2, 3, 4])
H.add_edge(2, 3)
H.add_edge(3, 4)
R.add_nodes_from([1, 2, 3, 4])
R.add_edge(2, 3)
R.add_edge(4, 1)
I = nx.intersection_all([G, H, R])
assert set(I.nodes()) == {1, 2, 3, 4}
assert sorted(I.edges()) == [(2, 3)]
assert I.graph == {}
```

## Next Steps


---

*Source: test_all.py:34 | Complexity: Advanced | Last updated: 2026-06-02*