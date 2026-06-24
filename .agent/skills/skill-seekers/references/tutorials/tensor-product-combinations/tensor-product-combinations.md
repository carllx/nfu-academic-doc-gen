# How To: Tensor Product Combinations

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tensor product combinations

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign P5 = nx.path_graph(...)

```python
P5 = nx.path_graph(5)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 2: Assign K3 = nx.complete_graph(...)

```python
K3 = nx.complete_graph(3)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 3: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(P5, K3)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 4: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(P5, nx.MultiGraph(K3))
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 5: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(nx.MultiGraph(P5), K3)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 6: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(nx.MultiGraph(P5), nx.MultiGraph(K3))
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 7: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(nx.DiGraph(P5), nx.DiGraph(K3))
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```


## Complete Example

```python
# Workflow
P5 = nx.path_graph(5)
K3 = nx.complete_graph(3)
G = nx.tensor_product(P5, K3)
assert nx.number_of_nodes(G) == 5 * 3
G = nx.tensor_product(P5, nx.MultiGraph(K3))
assert nx.number_of_nodes(G) == 5 * 3
G = nx.tensor_product(nx.MultiGraph(P5), K3)
assert nx.number_of_nodes(G) == 5 * 3
G = nx.tensor_product(nx.MultiGraph(P5), nx.MultiGraph(K3))
assert nx.number_of_nodes(G) == 5 * 3
G = nx.tensor_product(nx.DiGraph(P5), nx.DiGraph(K3))
assert nx.number_of_nodes(G) == 5 * 3
```

## Next Steps


---

*Source: test_product.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*