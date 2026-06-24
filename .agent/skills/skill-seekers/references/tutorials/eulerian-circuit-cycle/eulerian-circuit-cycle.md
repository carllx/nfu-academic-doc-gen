# How To: Eulerian Circuit Cycle

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eulerian circuit cycle

## Prerequisites

**Required Modules:**
- `collections`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4)
```

**Verification:**
```python
assert nodes == [0, 3, 2, 1]
```

### Step 2: Assign edges = list(...)

```python
edges = list(nx.eulerian_circuit(G, source=0))
```

**Verification:**
```python
assert edges == [(0, 3), (3, 2), (2, 1), (1, 0)]
```

### Step 3: Assign nodes = value

```python
nodes = [u for u, v in edges]
```

**Verification:**
```python
assert nodes == [1, 2, 3, 0]
```

### Step 4: Assign edges = list(...)

```python
edges = list(nx.eulerian_circuit(G, source=1))
```

**Verification:**
```python
assert edges == [(1, 2), (2, 3), (3, 0), (0, 1)]
```

### Step 5: Assign nodes = value

```python
nodes = [u for u, v in edges]
```

**Verification:**
```python
assert nodes == [0, 2, 1]
```

### Step 6: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(3)
```

**Verification:**
```python
assert edges == [(0, 2), (2, 1), (1, 0)]
```

### Step 7: Assign edges = list(...)

```python
edges = list(nx.eulerian_circuit(G, source=0))
```

**Verification:**
```python
assert nodes == [1, 2, 0]
```

### Step 8: Assign nodes = value

```python
nodes = [u for u, v in edges]
```

**Verification:**
```python
assert edges == [(1, 2), (2, 0), (0, 1)]
```

### Step 9: Assign edges = list(...)

```python
edges = list(nx.eulerian_circuit(G, source=1))
```

### Step 10: Assign nodes = value

```python
nodes = [u for u, v in edges]
```

**Verification:**
```python
assert nodes == [1, 2, 0]
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(4)
edges = list(nx.eulerian_circuit(G, source=0))
nodes = [u for u, v in edges]
assert nodes == [0, 3, 2, 1]
assert edges == [(0, 3), (3, 2), (2, 1), (1, 0)]
edges = list(nx.eulerian_circuit(G, source=1))
nodes = [u for u, v in edges]
assert nodes == [1, 2, 3, 0]
assert edges == [(1, 2), (2, 3), (3, 0), (0, 1)]
G = nx.complete_graph(3)
edges = list(nx.eulerian_circuit(G, source=0))
nodes = [u for u, v in edges]
assert nodes == [0, 2, 1]
assert edges == [(0, 2), (2, 1), (1, 0)]
edges = list(nx.eulerian_circuit(G, source=1))
nodes = [u for u, v in edges]
assert nodes == [1, 2, 0]
assert edges == [(1, 2), (2, 0), (0, 1)]
```

## Next Steps


---

*Source: test_euler.py:48 | Complexity: Advanced | Last updated: 2026-06-02*