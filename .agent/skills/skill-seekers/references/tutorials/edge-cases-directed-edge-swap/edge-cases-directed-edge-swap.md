# How To: Edge Cases Directed Edge Swap

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate DiGraph: test edge cases directed edge swap

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign graph = nx.DiGraph(...)

```python
graph = nx.DiGraph([(0, 0), (0, 1), (1, 0), (2, 3), (3, 2)])
```


## Complete Example

```python
# Workflow
graph = nx.DiGraph([(0, 0), (0, 1), (1, 0), (2, 3), (3, 2)])
```

## Next Steps


---

*Source: test_swap.py:45 | Complexity: Beginner | Last updated: 2026-06-02*