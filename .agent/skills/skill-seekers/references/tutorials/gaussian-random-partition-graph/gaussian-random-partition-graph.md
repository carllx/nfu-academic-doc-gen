# How To: Gaussian Random Partition Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gaussian random partition graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.gaussian_random_partition_graph(...)

```python
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01)
```

**Verification:**
```python
assert len(G) == 100
```

### Step 2: Assign G = nx.gaussian_random_partition_graph(...)

```python
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01, directed=True)
```

**Verification:**
```python
assert len(G) == 100
```

### Step 3: Assign G = nx.gaussian_random_partition_graph(...)

```python
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01, directed=False, seed=42)
```

**Verification:**
```python
assert len(G) == 100
```

### Step 4: Assign G = nx.gaussian_random_partition_graph(...)

```python
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01, directed=True, seed=42)
```

**Verification:**
```python
assert not isinstance(G, nx.DiGraph)
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.gaussian_random_partition_graph, 100, 101, 10, 1, 0)
```

**Verification:**
```python
assert len(G) == 100
```

### Step 6: Assign G = nx.gaussian_random_partition_graph(...)

```python
G = nx.gaussian_random_partition_graph(10, 0.5, 0.5, 0.5, 0.5, seed=1)
```

**Verification:**
```python
assert isinstance(G, nx.DiGraph)
```


## Complete Example

```python
# Workflow
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01)
assert len(G) == 100
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01, directed=True)
assert len(G) == 100
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01, directed=False, seed=42)
assert len(G) == 100
assert not isinstance(G, nx.DiGraph)
G = nx.gaussian_random_partition_graph(100, 10, 10, 0.3, 0.01, directed=True, seed=42)
assert len(G) == 100
assert isinstance(G, nx.DiGraph)
pytest.raises(nx.NetworkXError, nx.gaussian_random_partition_graph, 100, 101, 10, 1, 0)
G = nx.gaussian_random_partition_graph(10, 0.5, 0.5, 0.5, 0.5, seed=1)
assert len(G) == 10
```

## Next Steps


---

*Source: test_community.py:122 | Complexity: Intermediate | Last updated: 2026-06-02*