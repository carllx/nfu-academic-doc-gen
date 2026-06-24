# How To: Write Read P2G

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write read p2g

## Prerequisites

**Required Modules:**
- `io`
- `networkx`
- `networkx.readwrite.p2g`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

**Verification:**
```python
assert edges_equal(G.edges(), H.edges(), directed=True)
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 3: Assign G.name = 'foo'

```python
G.name = 'foo'
```

### Step 4: Call G.add_edges_from()

```python
G.add_edges_from([('a', 'b'), ('b', 'c')])
```

### Step 5: Call write_p2g()

```python
write_p2g(G, fh)
```

### Step 6: Call fh.seek()

```python
fh.seek(0)
```

### Step 7: Assign H = read_p2g(...)

```python
H = read_p2g(fh)
```

**Verification:**
```python
assert edges_equal(G.edges(), H.edges(), directed=True)
```


## Complete Example

```python
# Workflow
fh = io.BytesIO()
G = nx.DiGraph()
G.name = 'foo'
G.add_edges_from([('a', 'b'), ('b', 'c')])
write_p2g(G, fh)
fh.seek(0)
H = read_p2g(fh)
assert edges_equal(G.edges(), H.edges(), directed=True)
```

## Next Steps


---

*Source: test_p2g.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*