# How To: Complement

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complement

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign null = nx.null_graph(...)

```python
null = nx.null_graph()
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.empty_graph(3))
```

### Step 2: Assign empty1 = nx.empty_graph(...)

```python
empty1 = nx.empty_graph(1)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.empty_graph(5))
```

### Step 3: Assign empty10 = nx.empty_graph(...)

```python
empty10 = nx.empty_graph(10)
```

**Verification:**
```python
assert nx.is_isomorphic(P3, P3cc)
```

### Step 4: Assign K3 = nx.complete_graph(...)

```python
K3 = nx.complete_graph(3)
```

**Verification:**
```python
assert nx.is_isomorphic(null, nullcc)
```

### Step 5: Assign K5 = nx.complete_graph(...)

```python
K5 = nx.complete_graph(5)
```

**Verification:**
```python
assert nx.is_isomorphic(b, bcc)
```

### Step 6: Assign K10 = nx.complete_graph(...)

```python
K10 = nx.complete_graph(10)
```

### Step 7: Assign P2 = nx.path_graph(...)

```python
P2 = nx.path_graph(2)
```

### Step 8: Assign P3 = nx.path_graph(...)

```python
P3 = nx.path_graph(3)
```

### Step 9: Assign P5 = nx.path_graph(...)

```python
P5 = nx.path_graph(5)
```

### Step 10: Assign P10 = nx.path_graph(...)

```python
P10 = nx.path_graph(10)
```

### Step 11: Assign G = nx.complement(...)

```python
G = nx.complement(K3)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.empty_graph(3))
```

### Step 12: Assign G = nx.complement(...)

```python
G = nx.complement(K5)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.empty_graph(5))
```

### Step 13: Assign P3cc = nx.complement(...)

```python
P3cc = nx.complement(nx.complement(P3))
```

**Verification:**
```python
assert nx.is_isomorphic(P3, P3cc)
```

### Step 14: Assign nullcc = nx.complement(...)

```python
nullcc = nx.complement(nx.complement(null))
```

**Verification:**
```python
assert nx.is_isomorphic(null, nullcc)
```

### Step 15: Assign b = nx.bull_graph(...)

```python
b = nx.bull_graph()
```

### Step 16: Assign bcc = nx.complement(...)

```python
bcc = nx.complement(nx.complement(b))
```

**Verification:**
```python
assert nx.is_isomorphic(b, bcc)
```


## Complete Example

```python
# Workflow
null = nx.null_graph()
empty1 = nx.empty_graph(1)
empty10 = nx.empty_graph(10)
K3 = nx.complete_graph(3)
K5 = nx.complete_graph(5)
K10 = nx.complete_graph(10)
P2 = nx.path_graph(2)
P3 = nx.path_graph(3)
P5 = nx.path_graph(5)
P10 = nx.path_graph(10)
G = nx.complement(K3)
assert nx.is_isomorphic(G, nx.empty_graph(3))
G = nx.complement(K5)
assert nx.is_isomorphic(G, nx.empty_graph(5))
P3cc = nx.complement(nx.complement(P3))
assert nx.is_isomorphic(P3, P3cc)
nullcc = nx.complement(nx.complement(null))
assert nx.is_isomorphic(null, nullcc)
b = nx.bull_graph()
bcc = nx.complement(nx.complement(b))
assert nx.is_isomorphic(b, bcc)
```

## Next Steps


---

*Source: test_unary.py:6 | Complexity: Advanced | Last updated: 2026-06-02*