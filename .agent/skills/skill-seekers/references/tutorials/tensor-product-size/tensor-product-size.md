# How To: Tensor Product Size

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tensor product size

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
assert nx.number_of_nodes(G) == 3 * 5
```

### Step 3: Assign K5 = nx.complete_graph(...)

```python
K5 = nx.complete_graph(5)
```

### Step 4: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(P5, K3)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 5: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(K3, K5)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 3 * 5
```


## Complete Example

```python
# Workflow
P5 = nx.path_graph(5)
K3 = nx.complete_graph(3)
K5 = nx.complete_graph(5)
G = nx.tensor_product(P5, K3)
assert nx.number_of_nodes(G) == 5 * 3
G = nx.tensor_product(K3, K5)
assert nx.number_of_nodes(G) == 3 * 5
```

## Next Steps


---

*Source: test_product.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*