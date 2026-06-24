# How To: Transitive Reduction

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transitive reduction

## Prerequisites

**Required Modules:**
- `collections`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
```

**Verification:**
```python
assert edges_equal(transitive_reduction(G).edges(), solution, directed=True)
```

### Step 2: Assign transitive_reduction = value

```python
transitive_reduction = nx.algorithms.dag.transitive_reduction
```

**Verification:**
```python
assert edges_equal(transitive_reduction(G).edges(), solution, directed=True)
```

### Step 3: Assign solution = value

```python
solution = [(1, 2), (2, 3), (3, 4)]
```

**Verification:**
```python
assert edges_equal(transitive_reduction(G).edges(), solution, directed=True)
```

### Step 4: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)])
```

### Step 5: Assign transitive_reduction = value

```python
transitive_reduction = nx.algorithms.dag.transitive_reduction
```

### Step 6: Assign solution = value

```python
solution = [(1, 2), (2, 3), (2, 4)]
```

**Verification:**
```python
assert edges_equal(transitive_reduction(G).edges(), solution, directed=True)
```

### Step 7: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
```

### Step 8: Call pytest.raises()

```python
pytest.raises(nx.NetworkXNotImplemented, transitive_reduction, G)
```


## Complete Example

```python
# Workflow
G = nx.DiGraph([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)])
transitive_reduction = nx.algorithms.dag.transitive_reduction
solution = [(1, 2), (2, 3), (3, 4)]
assert edges_equal(transitive_reduction(G).edges(), solution, directed=True)
G = nx.DiGraph([(1, 2), (1, 3), (1, 4), (2, 3), (2, 4)])
transitive_reduction = nx.algorithms.dag.transitive_reduction
solution = [(1, 2), (2, 3), (2, 4)]
assert edges_equal(transitive_reduction(G).edges(), solution, directed=True)
G = nx.Graph([(1, 2), (2, 3), (3, 4)])
pytest.raises(nx.NetworkXNotImplemented, transitive_reduction, G)
```

## Next Steps


---

*Source: test_dag.py:461 | Complexity: Advanced | Last updated: 2026-06-02*