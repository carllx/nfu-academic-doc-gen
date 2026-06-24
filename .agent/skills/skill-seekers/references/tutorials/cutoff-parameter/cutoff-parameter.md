# How To: Cutoff Parameter

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cutoff parameter

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.community`


## Step-by-Step Guide

### Step 1: Assign G = nx.circular_ladder_graph(...)

```python
G = nx.circular_ladder_graph(4)
```

**Verification:**
```python
assert greedy_modularity_communities(G, cutoff=8) == expected
```

### Step 2: Assign expected = value

```python
expected = [{k} for k in range(8)]
```

**Verification:**
```python
assert greedy_modularity_communities(G, cutoff=4) == expected
```

### Step 3: Assign expected = value

```python
expected = [{k, k + 1} for k in range(0, 8, 2)]
```

**Verification:**
```python
assert greedy_modularity_communities(G, cutoff=1) == expected
```

### Step 4: Assign expected = value

```python
expected = [frozenset(range(4)), frozenset(range(4, 8))]
```

**Verification:**
```python
assert greedy_modularity_communities(G, cutoff=1) == expected
```


## Complete Example

```python
# Workflow
G = nx.circular_ladder_graph(4)
expected = [{k} for k in range(8)]
assert greedy_modularity_communities(G, cutoff=8) == expected
expected = [{k, k + 1} for k in range(0, 8, 2)]
assert greedy_modularity_communities(G, cutoff=4) == expected
expected = [frozenset(range(4)), frozenset(range(4, 8))]
assert greedy_modularity_communities(G, cutoff=1) == expected
```

## Next Steps


---

*Source: test_modularity_max.py:301 | Complexity: Intermediate | Last updated: 2026-06-02*