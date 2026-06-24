# How To: All Triangles Complete Graph Exact

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all triangles complete graph exact

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(4)
```

**Verification:**
```python
assert {frozenset(t) for t in nx.all_triangles(G)} == expected
```

### Step 2: Assign expected = value

```python
expected = {frozenset({0, 1, 2}), frozenset({0, 1, 3}), frozenset({0, 2, 3}), frozenset({1, 2, 3})}
```

**Verification:**
```python
assert {frozenset(t) for t in nx.all_triangles(G)} == expected
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(4)
expected = {frozenset({0, 1, 2}), frozenset({0, 1, 3}), frozenset({0, 2, 3}), frozenset({1, 2, 3})}
assert {frozenset(t) for t in nx.all_triangles(G)} == expected
```

## Next Steps


---

*Source: test_cluster.py:147 | Complexity: Beginner | Last updated: 2026-06-02*