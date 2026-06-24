# How To: Barbell

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test barbell

## Prerequisites

**Required Modules:**
- `itertools`
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.connectivity`
- `networkx.algorithms.connectivity.edge_augmentation`
- `networkx.utils`
- `math`


## Step-by-Step Guide

### Step 1: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(5, 0)
```

### Step 2: Call _check_augmentations()

```python
_check_augmentations(G)
```

### Step 3: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(5, 2)
```

### Step 4: Call _check_augmentations()

```python
_check_augmentations(G)
```

### Step 5: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(5, 3)
```

### Step 6: Call _check_augmentations()

```python
_check_augmentations(G)
```

### Step 7: Assign G = nx.barbell_graph(...)

```python
G = nx.barbell_graph(5, 4)
```

### Step 8: Call _check_augmentations()

```python
_check_augmentations(G)
```


## Complete Example

```python
# Workflow
G = nx.barbell_graph(5, 0)
_check_augmentations(G)
G = nx.barbell_graph(5, 2)
_check_augmentations(G)
G = nx.barbell_graph(5, 3)
_check_augmentations(G)
G = nx.barbell_graph(5, 4)
_check_augmentations(G)
```

## Next Steps


---

*Source: test_edge_augmentation.py:229 | Complexity: Advanced | Last updated: 2026-06-02*