# How To: Write P2G

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write p2g

## Prerequisites

**Required Modules:**
- `io`
- `networkx`
- `networkx.readwrite.p2g`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign s = b'foo\n3 2\n1\n1 \n2\n2 \n3\n\n'

```python
s = b'foo\n3 2\n1\n1 \n2\n2 \n3\n\n'
```

**Verification:**
```python
assert r == s
```

### Step 2: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

### Step 3: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 4: Assign G.name = 'foo'

```python
G.name = 'foo'
```

### Step 5: Call G.add_edges_from()

```python
G.add_edges_from([(1, 2), (2, 3)])
```

### Step 6: Call write_p2g()

```python
write_p2g(G, fh)
```

### Step 7: Call fh.seek()

```python
fh.seek(0)
```

### Step 8: Assign r = fh.read(...)

```python
r = fh.read()
```

**Verification:**
```python
assert r == s
```


## Complete Example

```python
# Workflow
s = b'foo\n3 2\n1\n1 \n2\n2 \n3\n\n'
fh = io.BytesIO()
G = nx.DiGraph()
G.name = 'foo'
G.add_edges_from([(1, 2), (2, 3)])
write_p2g(G, fh)
fh.seek(0)
r = fh.read()
assert r == s
```

## Next Steps


---

*Source: test_p2g.py:36 | Complexity: Advanced | Last updated: 2026-06-02*