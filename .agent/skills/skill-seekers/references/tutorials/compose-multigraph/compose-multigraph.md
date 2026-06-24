# How To: Compose Multigraph

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compose multigraph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.MultiGraph(...)

```python
G = nx.MultiGraph()
```

**Verification:**
```python
assert set(GH) == set(G) | set(H)
```

### Step 2: Call G.add_edge()

```python
G.add_edge(1, 2, key=0)
```

**Verification:**
```python
assert set(GH.edges(keys=True)) == set(G.edges(keys=True)) | set(H.edges(keys=True))
```

### Step 3: Call G.add_edge()

```python
G.add_edge(1, 2, key=1)
```

**Verification:**
```python
assert set(GH) == set(G) | set(H)
```

### Step 4: Assign H = nx.MultiGraph(...)

```python
H = nx.MultiGraph()
```

**Verification:**
```python
assert set(GH.edges(keys=True)) == set(G.edges(keys=True)) | set(H.edges(keys=True))
```

### Step 5: Call H.add_edge()

```python
H.add_edge(3, 4, key=0)
```

### Step 6: Call H.add_edge()

```python
H.add_edge(3, 4, key=1)
```

### Step 7: Assign GH = nx.compose(...)

```python
GH = nx.compose(G, H)
```

**Verification:**
```python
assert set(GH) == set(G) | set(H)
```

### Step 8: Call H.add_edge()

```python
H.add_edge(1, 2, key=2)
```

### Step 9: Assign GH = nx.compose(...)

```python
GH = nx.compose(G, H)
```

**Verification:**
```python
assert set(GH) == set(G) | set(H)
```


## Complete Example

```python
# Workflow
G = nx.MultiGraph()
G.add_edge(1, 2, key=0)
G.add_edge(1, 2, key=1)
H = nx.MultiGraph()
H.add_edge(3, 4, key=0)
H.add_edge(3, 4, key=1)
GH = nx.compose(G, H)
assert set(GH) == set(G) | set(H)
assert set(GH.edges(keys=True)) == set(G.edges(keys=True)) | set(H.edges(keys=True))
H.add_edge(1, 2, key=2)
GH = nx.compose(G, H)
assert set(GH) == set(G) | set(H)
assert set(GH.edges(keys=True)) == set(G.edges(keys=True)) | set(H.edges(keys=True))
```

## Next Steps


---

*Source: test_binary.py:339 | Complexity: Advanced | Last updated: 2026-06-02*