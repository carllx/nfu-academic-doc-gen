# How To: Cartesian Product Size

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cartesian product size

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign K5 = nx.complete_graph(...)

```python
K5 = nx.complete_graph(5)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 2: Assign P5 = nx.path_graph(...)

```python
P5 = nx.path_graph(5)
```

**Verification:**
```python
assert nx.number_of_edges(G) == nx.number_of_edges(P5) * nx.number_of_nodes(K3) + nx.number_of_edges(K3) * nx.number_of_nodes(P5)
```

### Step 3: Assign K3 = nx.complete_graph(...)

```python
K3 = nx.complete_graph(3)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 3 * 5
```

### Step 4: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(P5, K3)
```

**Verification:**
```python
assert nx.number_of_edges(G) == nx.number_of_edges(K5) * nx.number_of_nodes(K3) + nx.number_of_edges(K3) * nx.number_of_nodes(K5)
```

### Step 5: Assign G = nx.cartesian_product(...)

```python
G = nx.cartesian_product(K3, K5)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 3 * 5
```


## Complete Example

```python
# Workflow
K5 = nx.complete_graph(5)
P5 = nx.path_graph(5)
K3 = nx.complete_graph(3)
G = nx.cartesian_product(P5, K3)
assert nx.number_of_nodes(G) == 5 * 3
assert nx.number_of_edges(G) == nx.number_of_edges(P5) * nx.number_of_nodes(K3) + nx.number_of_edges(K3) * nx.number_of_nodes(P5)
G = nx.cartesian_product(K3, K5)
assert nx.number_of_nodes(G) == 3 * 5
assert nx.number_of_edges(G) == nx.number_of_edges(K5) * nx.number_of_nodes(K3) + nx.number_of_edges(K3) * nx.number_of_nodes(K5)
```

## Next Steps


---

*Source: test_product.py:163 | Complexity: Intermediate | Last updated: 2026-06-02*