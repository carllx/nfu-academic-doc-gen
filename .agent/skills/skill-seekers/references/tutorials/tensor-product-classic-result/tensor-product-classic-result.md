# How To: Tensor Product Classic Result

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tensor product classic result

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign K2 = nx.complete_graph(...)

```python
K2 = nx.complete_graph(2)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.desargues_graph())
```

### Step 2: Assign G = nx.petersen_graph(...)

```python
G = nx.petersen_graph()
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.cycle_graph(10))
```

### Step 3: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(G, K2)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.cubical_graph())
```

### Step 4: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(5)
```

### Step 5: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(G, K2)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.cycle_graph(10))
```

### Step 6: Assign G = nx.tetrahedral_graph(...)

```python
G = nx.tetrahedral_graph()
```

### Step 7: Assign G = nx.tensor_product(...)

```python
G = nx.tensor_product(G, K2)
```

**Verification:**
```python
assert nx.is_isomorphic(G, nx.cubical_graph())
```


## Complete Example

```python
# Workflow
K2 = nx.complete_graph(2)
G = nx.petersen_graph()
G = nx.tensor_product(G, K2)
assert nx.is_isomorphic(G, nx.desargues_graph())
G = nx.cycle_graph(5)
G = nx.tensor_product(G, K2)
assert nx.is_isomorphic(G, nx.cycle_graph(10))
G = nx.tetrahedral_graph()
G = nx.tensor_product(G, K2)
assert nx.is_isomorphic(G, nx.cubical_graph())
```

## Next Steps


---

*Source: test_product.py:73 | Complexity: Intermediate | Last updated: 2026-06-02*