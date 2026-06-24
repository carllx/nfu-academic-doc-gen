# How To: Difference2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test difference2

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
assert set(D.nodes()) == {1, 2, 3, 4}
```

### Step 2: Assign H = nx.Graph(...)

```python
H = nx.Graph()
```

**Verification:**
```python
assert sorted(D.edges()) == [(2, 3)]
```

### Step 3: Call G.add_nodes_from()

```python
G.add_nodes_from([1, 2, 3, 4])
```

**Verification:**
```python
assert set(D.nodes()) == {1, 2, 3, 4}
```

### Step 4: Call H.add_nodes_from()

```python
H.add_nodes_from([1, 2, 3, 4])
```

**Verification:**
```python
assert sorted(D.edges()) == []
```

### Step 5: Call G.add_edge()

```python
G.add_edge(1, 2)
```

**Verification:**
```python
assert set(D.nodes()) == {1, 2, 3, 4}
```

### Step 6: Call H.add_edge()

```python
H.add_edge(1, 2)
```

**Verification:**
```python
assert sorted(D.edges()) == [(3, 4)]
```

### Step 7: Call G.add_edge()

```python
G.add_edge(2, 3)
```

### Step 8: Assign D = nx.difference(...)

```python
D = nx.difference(G, H)
```

**Verification:**
```python
assert set(D.nodes()) == {1, 2, 3, 4}
```

### Step 9: Assign D = nx.difference(...)

```python
D = nx.difference(H, G)
```

**Verification:**
```python
assert set(D.nodes()) == {1, 2, 3, 4}
```

### Step 10: Call H.add_edge()

```python
H.add_edge(3, 4)
```

### Step 11: Assign D = nx.difference(...)

```python
D = nx.difference(H, G)
```

**Verification:**
```python
assert set(D.nodes()) == {1, 2, 3, 4}
```


## Complete Example

```python
# Workflow
G = nx.Graph()
H = nx.Graph()
G.add_nodes_from([1, 2, 3, 4])
H.add_nodes_from([1, 2, 3, 4])
G.add_edge(1, 2)
H.add_edge(1, 2)
G.add_edge(2, 3)
D = nx.difference(G, H)
assert set(D.nodes()) == {1, 2, 3, 4}
assert sorted(D.edges()) == [(2, 3)]
D = nx.difference(H, G)
assert set(D.nodes()) == {1, 2, 3, 4}
assert sorted(D.edges()) == []
H.add_edge(3, 4)
D = nx.difference(H, G)
assert set(D.nodes()) == {1, 2, 3, 4}
assert sorted(D.edges()) == [(3, 4)]
```

## Next Steps


---

*Source: test_binary.py:146 | Complexity: Advanced | Last updated: 2026-06-02*