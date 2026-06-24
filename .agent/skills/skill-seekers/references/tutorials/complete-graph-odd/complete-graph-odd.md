# How To: Complete Graph Odd

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test complete graph odd

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.complete_graph(...)

```python
G = nx.complete_graph(11)
```

**Verification:**
```python
assert nx.is_edge_cover(G, min_cover)
```

### Step 2: Assign min_cover = nx.min_edge_cover(...)

```python
min_cover = nx.min_edge_cover(G)
```

**Verification:**
```python
assert len(min_cover) == 6
```


## Complete Example

```python
# Workflow
G = nx.complete_graph(11)
min_cover = nx.min_edge_cover(G)
assert nx.is_edge_cover(G, min_cover)
assert len(min_cover) == 6
```

## Next Steps


---

*Source: test_covering.py:60 | Complexity: Beginner | Last updated: 2026-06-02*