# How To: All Pairs Lca Input Graph With Two Roots

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all pairs lca input graph with two roots

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = self.DG.copy(...)

```python
G = self.DG.copy()
```

### Step 2: Call G.add_edge()

```python
G.add_edge(9, 10)
```

### Step 3: Call G.add_edge()

```python
G.add_edge(9, 4)
```

### Step 4: Assign gold = self.gold.copy(...)

```python
gold = self.gold.copy()
```

### Step 5: Assign unknown = 9

```python
gold[9, 9] = 9
```

### Step 6: Assign unknown = 9

```python
gold[9, 10] = 9
```

### Step 7: Assign unknown = 9

```python
gold[9, 4] = 9
```

### Step 8: Assign unknown = 9

```python
gold[9, 3] = 9
```

### Step 9: Assign unknown = 9

```python
gold[10, 4] = 9
```

### Step 10: Assign unknown = 9

```python
gold[10, 3] = 9
```

### Step 11: Assign unknown = 10

```python
gold[10, 10] = 10
```

### Step 12: Assign testing = dict(...)

```python
testing = dict(all_pairs_lca(G))
```

### Step 13: Call G.add_edge()

```python
G.add_edge(-1, 9)
```

### Step 14: Call G.add_edge()

```python
G.add_edge(-1, 0)
```

### Step 15: Call self.assert_lca_dicts_same()

```python
self.assert_lca_dicts_same(testing, gold, G)
```


## Complete Example

```python
# Workflow
G = self.DG.copy()
G.add_edge(9, 10)
G.add_edge(9, 4)
gold = self.gold.copy()
gold[9, 9] = 9
gold[9, 10] = 9
gold[9, 4] = 9
gold[9, 3] = 9
gold[10, 4] = 9
gold[10, 3] = 9
gold[10, 10] = 10
testing = dict(all_pairs_lca(G))
G.add_edge(-1, 9)
G.add_edge(-1, 0)
self.assert_lca_dicts_same(testing, gold, G)
```

## Next Steps


---

*Source: test_lowest_common_ancestors.py:265 | Complexity: Advanced | Last updated: 2026-06-02*