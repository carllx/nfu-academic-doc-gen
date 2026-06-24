# How To: Complete Digraph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete digraph

## Prerequisites

**Required Modules:**
- `itertools`
- `typing`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign g = nx.complete_graph(...)

```python
g = nx.complete_graph('abc', create_using=nx.DiGraph)
```

**Verification:**
```python
assert nx.number_of_nodes(g) == m
```

### Step 2: Assign g = nx.complete_graph(...)

```python
g = nx.complete_graph(m, create_using=nx.DiGraph)
```

**Verification:**
```python
assert nx.number_of_edges(g) == m * (m - 1)
```


## Complete Example

```python
# Workflow
for m in [0, 1, 3, 5]:
    g = nx.complete_graph(m, create_using=nx.DiGraph)
    assert nx.number_of_nodes(g) == m
    assert nx.number_of_edges(g) == m * (m - 1)
g = nx.complete_graph('abc', create_using=nx.DiGraph)
assert len(g) == 3
assert g.size() == 6
assert g.is_directed()
```

## Next Steps


---

*Source: test_classic.py:171 | Complexity: Beginner | Last updated: 2026-06-02*