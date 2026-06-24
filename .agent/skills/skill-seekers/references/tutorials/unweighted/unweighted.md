# How To: Unweighted

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unweighted

## Prerequisites

**Required Modules:**
- `collections`
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(1, 2), (2, 3), (2, 4), (3, 5), (5, 6), (5, 7)]
```

**Verification:**
```python
assert nx.dag_longest_path_length(G) == 4
```

### Step 2: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(edges)
```

**Verification:**
```python
assert nx.dag_longest_path_length(G) == 4
```

### Step 3: Assign edges = value

```python
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5), (3, 5)]
```

**Verification:**
```python
assert nx.dag_longest_path_length(G) == 0
```

### Step 4: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph(edges)
```

**Verification:**
```python
assert nx.dag_longest_path_length(G) == 4
```

### Step 5: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

### Step 6: Call G.add_node()

```python
G.add_node(1)
```

**Verification:**
```python
assert nx.dag_longest_path_length(G) == 0
```


## Complete Example

```python
# Workflow
edges = [(1, 2), (2, 3), (2, 4), (3, 5), (5, 6), (5, 7)]
G = nx.DiGraph(edges)
assert nx.dag_longest_path_length(G) == 4
edges = [(1, 2), (2, 3), (3, 4), (4, 5), (1, 3), (1, 5), (3, 5)]
G = nx.DiGraph(edges)
assert nx.dag_longest_path_length(G) == 4
G = nx.DiGraph()
G.add_node(1)
assert nx.dag_longest_path_length(G) == 0
```

## Next Steps


---

*Source: test_dag.py:95 | Complexity: Intermediate | Last updated: 2026-06-02*