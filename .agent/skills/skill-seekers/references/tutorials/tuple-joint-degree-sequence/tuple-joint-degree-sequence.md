# How To: Tuple Joint Degree Sequence

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tuple joint degree sequence

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.random_clustered_graph(...)

```python
G = nx.random_clustered_graph([(1, 2), (2, 1), (1, 1), (1, 1), (1, 1), (2, 0)])
```

**Verification:**
```python
assert G.number_of_nodes() == 6
```


## Complete Example

```python
# Workflow
G = nx.random_clustered_graph([(1, 2), (2, 1), (1, 1), (1, 1), (1, 1), (2, 0)])
assert G.number_of_nodes() == 6
assert G.number_of_edges() == 10
```

## Next Steps


---

*Source: test_random_clustered.py:15 | Complexity: Beginner | Last updated: 2026-06-02*