# How To: Final Size

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test final size

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign N = 10

```python
N = 10
```

**Verification:**
```python
assert len(G) == N
```

### Step 2: Assign n = 5

```python
n = 5
```

**Verification:**
```python
assert len(G) == N
```

### Step 3: Assign p = 0.5

```python
p = 0.5
```

### Step 4: Assign q = 0.5

```python
q = 0.5
```

### Step 5: Assign G = nx.partial_duplication_graph(...)

```python
G = nx.partial_duplication_graph(N, n, p, q)
```

**Verification:**
```python
assert len(G) == N
```

### Step 6: Assign G = nx.partial_duplication_graph(...)

```python
G = nx.partial_duplication_graph(N, n, p, q, seed=42)
```

**Verification:**
```python
assert len(G) == N
```


## Complete Example

```python
# Workflow
N = 10
n = 5
p = 0.5
q = 0.5
G = nx.partial_duplication_graph(N, n, p, q)
assert len(G) == N
G = nx.partial_duplication_graph(N, n, p, q, seed=42)
assert len(G) == N
```

## Next Steps


---

*Source: test_duplication.py:60 | Complexity: Intermediate | Last updated: 2026-06-02*