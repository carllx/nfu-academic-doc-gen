# How To: Cartesian Product Null

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cartesian product null

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign null = nx.null_graph(...)

```python
null = nx.null_graph()
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 2: Assign empty10 = nx.empty_graph(...)

```python
empty10 = nx.empty_graph(10)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 3: Assign K3 = nx.complete_graph(...)

```python
K3 = nx.complete_graph(3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 4: Assign K10 = nx.complete_graph(...)

```python
K10 = nx.complete_graph(10)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 5: Assign P3 = nx.path_graph(...)

```python
P3 = nx.path_graph(3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 6: Assign P10 = nx.path_graph(...)

```python
P10 = nx.path_graph(10)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 7: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(null, null)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 8: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(null, empty10)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 9: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(null, K3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 10: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(null, K10)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 11: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(null, P3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 12: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(null, P10)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 13: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(empty10, null)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 14: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(K3, null)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 15: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(K10, null)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 16: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(P3, null)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```

### Step 17: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(P10, null)
```

**Verification:**
```python
assert nx.is_isomorphic(G, null)
```


## Complete Example

```python
# Workflow
null = nx.null_graph()
empty10 = nx.empty_graph(10)
K3 = nx.complete_graph(3)
K10 = nx.complete_graph(10)
P3 = nx.path_graph(3)
P10 = nx.path_graph(10)
G = nx.cartesian_product(null, null)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(null, empty10)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(null, K3)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(null, K10)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(null, P3)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(null, P10)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(empty10, null)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(K3, null)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(K10, null)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(P3, null)
assert nx.is_isomorphic(G, null)
G = nx.cartesian_product(P10, null)
assert nx.is_isomorphic(G, null)
```

## Next Steps


---

*Source: test_product.py:130 | Complexity: Advanced | Last updated: 2026-06-02*