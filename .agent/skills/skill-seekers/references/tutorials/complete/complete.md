# How To: Complete

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.algorithms.approximation`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(5)
```

**Verification:**
```python
assert average_clustering(G, trials=len(G) // 2) == 1
```

### Step 2: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(7)
```

**Verification:**
```python
assert average_clustering(G, trials=len(G) // 2) == 1
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(5)
assert average_clustering(G, trials=len(G) // 2) == 1
G = nx.complete_graph(7)
assert average_clustering(G, trials=len(G) // 2) == 1
```

## Next Steps


---

*Source: test_approx_clust_coeff.py:37 | Complexity: Beginner | Last updated: 2026-06-02*