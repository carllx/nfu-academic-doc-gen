# How To: Complete Bipartite Graph Str

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Ensure G.name is consistent for all inputs accepted by nodes_or_number.
See gh-7396

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numbers`
- `pytest`
- `networkx`
- `generators`

**Setup Required:**
```python
# Fixtures: n, m
```

## Step-by-Step Guide

### Step 1: 'Ensure G.name is consistent for all inputs accepted by nodes_or_number.\n        See gh-7396'

```python
'Ensure G.name is consistent for all inputs accepted by nodes_or_number.\n        See gh-7396'
```

**Verification:**
```python
assert str(G) == ans
```

### Step 2: Assign G = nx.complete_bipartite_graph(...)

```python
G = nx.complete_bipartite_graph(n, m)
```

### Step 3: Assign ans = "Graph named 'complete_bipartite_graph(4, 3)' with 7 nodes and 12 edges"

```python
ans = "Graph named 'complete_bipartite_graph(4, 3)' with 7 nodes and 12 edges"
```

**Verification:**
```python
assert str(G) == ans
```


## Complete Example

```python
# Setup
# Fixtures: n, m

# Workflow
'Ensure G.name is consistent for all inputs accepted by nodes_or_number.\n        See gh-7396'
G = nx.complete_bipartite_graph(n, m)
ans = "Graph named 'complete_bipartite_graph(4, 3)' with 7 nodes and 12 edges"
assert str(G) == ans
```

## Next Steps


---

*Source: test_generators.py:402 | Complexity: Beginner | Last updated: 2026-06-02*