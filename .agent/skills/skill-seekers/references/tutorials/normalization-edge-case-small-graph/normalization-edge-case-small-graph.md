# How To: Normalization Edge Case Small Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test normalization edge case small graph

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(2)
```

**Verification:**
```python
assert len(result_norm) == 2
```

### Step 2: Assign result_norm = approximate_cfbc(...)

```python
result_norm = approximate_cfbc(G, normalized=True, seed=42)
```

**Verification:**
```python
assert len(result_unnorm) == 2
```

### Step 3: Assign result_unnorm = approximate_cfbc(...)

```python
result_unnorm = approximate_cfbc(G, normalized=False, seed=42)
```

**Verification:**
```python
assert all((v == 0.0 for v in result_norm.values()))
```

### Step 4: Assign G1 = nx.Graph(...)

```python
G1 = nx.Graph()
```

**Verification:**
```python
assert all((v == 0.0 for v in result_unnorm.values()))
```

### Step 5: Call G1.add_node()

```python
G1.add_node(0)
```

**Verification:**
```python
assert result1 == {0: 0.0}
```

### Step 6: Assign result1 = approximate_cfbc(...)

```python
result1 = approximate_cfbc(G1, normalized=True, seed=42)
```

**Verification:**
```python
assert result1 == {0: 0.0}
```


## Complete Example

```python
# Workflow
G = nx.path_graph(2)
result_norm = approximate_cfbc(G, normalized=True, seed=42)
result_unnorm = approximate_cfbc(G, normalized=False, seed=42)
assert len(result_norm) == 2
assert len(result_unnorm) == 2
assert all((v == 0.0 for v in result_norm.values()))
assert all((v == 0.0 for v in result_unnorm.values()))
G1 = nx.Graph()
G1.add_node(0)
result1 = approximate_cfbc(G1, normalized=True, seed=42)
assert result1 == {0: 0.0}
```

## Next Steps


---

*Source: test_current_flow_betweenness_centrality.py:182 | Complexity: Intermediate | Last updated: 2026-06-02*