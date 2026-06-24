# How To: Read Sparse6

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read sparse6

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign data = b':Q___eDcdFcDeFcE`GaJ`IaHbKNbLM'

```python
data = b':Q___eDcdFcDeFcE`GaJ`IaHbKNbLM'
```

**Verification:**
```python
assert nodes_equal(G.nodes(), Gin.nodes())
```

### Step 2: Assign G = nx.from_sparse6_bytes(...)

```python
G = nx.from_sparse6_bytes(data)
```

**Verification:**
```python
assert edges_equal(G.edges(), Gin.edges())
```

### Step 3: Assign fh = BytesIO(...)

```python
fh = BytesIO(data)
```

### Step 4: Assign Gin = nx.read_sparse6(...)

```python
Gin = nx.read_sparse6(fh)
```

**Verification:**
```python
assert nodes_equal(G.nodes(), Gin.nodes())
```


## Complete Example

```python
# Workflow
data = b':Q___eDcdFcDeFcE`GaJ`IaHbKNbLM'
G = nx.from_sparse6_bytes(data)
fh = BytesIO(data)
Gin = nx.read_sparse6(fh)
assert nodes_equal(G.nodes(), Gin.nodes())
assert edges_equal(G.edges(), Gin.edges())
```

## Next Steps


---

*Source: test_sparse6.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*