# How To: Eulerian Circuit Digraph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test eulerian circuit digraph

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
assert nodes == [0, 1, 2, 3]
```

### Step 2: Call nx.add_cycle()

```python
nx.add_cycle(G, [0, 1, 2, 3])
```

**Verification:**
```python
assert edges == [(0, 1), (1, 2), (2, 3), (3, 0)]
```

### Step 3: Assign edges = list(...)

```python
edges = list(nx.eulerian_circuit(G, source=0))
```

**Verification:**
```python
assert nodes == [1, 2, 3, 0]
```

### Step 4: Assign nodes = value

```python
nodes = [u for u, v in edges]
```

**Verification:**
```python
assert edges == [(1, 2), (2, 3), (3, 0), (0, 1)]
```

### Step 5: Assign edges = list(...)

```python
edges = list(nx.eulerian_circuit(G, source=1))
```

### Step 6: Assign nodes = value

```python
nodes = [u for u, v in edges]
```

**Verification:**
```python
assert nodes == [1, 2, 3, 0]
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
nx.add_cycle(G, [0, 1, 2, 3])
edges = list(nx.eulerian_circuit(G, source=0))
nodes = [u for u, v in edges]
assert nodes == [0, 1, 2, 3]
assert edges == [(0, 1), (1, 2), (2, 3), (3, 0)]
edges = list(nx.eulerian_circuit(G, source=1))
nodes = [u for u, v in edges]
assert nodes == [1, 2, 3, 0]
assert edges == [(1, 2), (2, 3), (3, 0), (0, 1)]
```

## Next Steps


---

*Source: test_euler.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*