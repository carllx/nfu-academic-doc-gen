# How To: Negative Weights

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test negative weights

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.algorithms.approximation`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert len(set1) == len(G.nodes) or len(set2) == len(G.nodes)
```

### Step 2: Call random.seed()

```python
random.seed(5)
```

### Step 3: Assign initial_cut = set(...)

```python
initial_cut = set(random.sample(sorted(G.nodes()), k=5))
```

### Step 4: Assign unknown = maxcut.one_exchange(...)

```python
cut_size, (set1, set2) = maxcut.one_exchange(G, initial_cut, weight='weight')
```

### Step 5: Call _is_valid_cut()

```python
_is_valid_cut(G, set1, set2)
```

### Step 6: Call _cut_is_locally_optimal()

```python
_cut_is_locally_optimal(G, cut_size, set1)
```

**Verification:**
```python
assert len(set1) == len(G.nodes) or len(set2) == len(G.nodes)
```

### Step 7: Assign unknown = value

```python
w['weight'] = -1 * random.random()
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(5)
random.seed(5)
for u, v, w in G.edges(data=True):
    w['weight'] = -1 * random.random()
initial_cut = set(random.sample(sorted(G.nodes()), k=5))
cut_size, (set1, set2) = maxcut.one_exchange(G, initial_cut, weight='weight')
_is_valid_cut(G, set1, set2)
_cut_is_locally_optimal(G, cut_size, set1)
assert len(set1) == len(G.nodes) or len(set2) == len(G.nodes)
```

## Next Steps


---

*Source: test_maxcut.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*