# How To: Lexicographic Product Size

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lexicographic product size

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
assert nx.number_of_nodes(G) == 3 * 5
```

### Step 3: Assign K3 = nx.complete_graph(...)

```python
K3 = nx.complete_graph(3)
```

### Step 4: Assign G = nx.lexicographic_product(...)

```python
G = nx.lexicographic_product(P5, K3)
```

**Verification:**
```python
assert nx.number_of_nodes(G) == 5 * 3
```

### Step 5: Assign G = nx.lexicographic_product(...)

```python
G = nx.lexicographic_product(K3, K5)
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
G = nx.lexicographic_product(P5, K3)
assert nx.number_of_nodes(G) == 5 * 3
G = nx.lexicographic_product(K3, K5)
assert nx.number_of_nodes(G) == 3 * 5
```

## Next Steps


---

*Source: test_product.py:247 | Complexity: Intermediate | Last updated: 2026-06-02*