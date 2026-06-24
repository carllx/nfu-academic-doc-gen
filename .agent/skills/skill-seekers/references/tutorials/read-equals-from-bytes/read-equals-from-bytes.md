# How To: Read Equals From Bytes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read equals from bytes

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.readwrite.graph6`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign data = b'DF{'

```python
data = b'DF{'
```

**Verification:**
```python
assert nodes_equal(G.nodes(), Gin.nodes())
```

### Step 2: Assign G = nx.from_graph6_bytes(...)

```python
G = nx.from_graph6_bytes(data)
```

**Verification:**
```python
assert edges_equal(G.edges(), Gin.edges())
```

### Step 3: Assign fh = BytesIO(...)

```python
fh = BytesIO(data)
```

### Step 4: Assign Gin = nx.read_graph6(...)

```python
Gin = nx.read_graph6(fh)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), Gin.nodes())
```


## Complete Example

```python
# Workflow
data = b'DF{'
G = nx.from_graph6_bytes(data)
fh = BytesIO(data)
Gin = nx.read_graph6(fh)
assert nodes_equal(G.nodes(), Gin.nodes())
assert edges_equal(G.edges(), Gin.edges())
```

## Next Steps


---

*Source: test_graph6.py:40 | Complexity: Intermediate | Last updated: 2026-06-02*