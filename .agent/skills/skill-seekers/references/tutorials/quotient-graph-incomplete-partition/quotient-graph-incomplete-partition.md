# How To: Quotient Graph Incomplete Partition

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quotient graph incomplete partition

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(6)
```

**Verification:**
```python
assert nodes_equal(H.nodes(), [])
```

### Step 2: Assign partition = value

```python
partition = []
```

**Verification:**
```python
assert edges_equal(H.edges(), [])
```

### Step 3: Assign H = nx.quotient_graph(...)

```python
H = nx.quotient_graph(G, partition, relabel=True)
```

**Verification:**
```python
assert nodes_equal(H.nodes(), [0, 1, 2])
```

### Step 4: Assign partition = value

```python
partition = [[0, 1], [2, 3], [5]]
```

**Verification:**
```python
assert edges_equal(H.edges(), [(0, 1)])
```

### Step 5: Assign H = nx.quotient_graph(...)

```python
H = nx.quotient_graph(G, partition, relabel=True)
```

**Verification:**
```python
assert nodes_equal(H.nodes(), [0, 1, 2])
```


## Complete Example

```python
# Workflow
G = nx.path_graph(6)
partition = []
H = nx.quotient_graph(G, partition, relabel=True)
assert nodes_equal(H.nodes(), [])
assert edges_equal(H.edges(), [])
partition = [[0, 1], [2, 3], [5]]
H = nx.quotient_graph(G, partition, relabel=True)
assert nodes_equal(H.nodes(), [0, 1, 2])
assert edges_equal(H.edges(), [(0, 1)])
```

## Next Steps


---

*Source: test_contraction.py:273 | Complexity: Intermediate | Last updated: 2026-06-02*