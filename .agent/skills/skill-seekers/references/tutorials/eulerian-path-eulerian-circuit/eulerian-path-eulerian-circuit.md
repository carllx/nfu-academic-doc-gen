# How To: Eulerian Path Eulerian Circuit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eulerian path eulerian circuit

## Prerequisites

**Required Modules:**
- `collections`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert result == list(nx.eulerian_path(G))
```

### Step 2: Assign result = value

```python
result = [(1, 2), (2, 3), (3, 4), (4, 1)]
```

**Verification:**
```python
assert result == list(nx.eulerian_path(G, source=1))
```

### Step 3: Assign result2 = value

```python
result2 = [(2, 3), (3, 4), (4, 1), (1, 2)]
```

**Verification:**
```python
assert result2 == list(nx.eulerian_path(G, source=2))
```

### Step 4: Assign result3 = value

```python
result3 = [(3, 4), (4, 1), (1, 2), (2, 3)]
```

**Verification:**
```python
assert result3 == list(nx.eulerian_path(G, source=3))
```

### Step 5: Call G.add_edges_from()

```python
G.add_edges_from(result)
```

**Verification:**
```python
assert result == list(nx.eulerian_path(G))
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
result = [(1, 2), (2, 3), (3, 4), (4, 1)]
result2 = [(2, 3), (3, 4), (4, 1), (1, 2)]
result3 = [(3, 4), (4, 1), (1, 2), (2, 3)]
G.add_edges_from(result)
assert result == list(nx.eulerian_path(G))
assert result == list(nx.eulerian_path(G, source=1))
assert result2 == list(nx.eulerian_path(G, source=2))
assert result3 == list(nx.eulerian_path(G, source=3))
```

## Next Steps


---

*Source: test_euler.py:214 | Complexity: Intermediate | Last updated: 2026-06-02*