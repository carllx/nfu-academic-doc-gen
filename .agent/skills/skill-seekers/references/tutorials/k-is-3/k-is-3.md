# How To: K Is 3

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: test k is 3

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(1, 6), (1, 7), (1, 8), (1, 9), (2, 6), (2, 7), (2, 8), (2, 10), (3, 6), (3, 8), (3, 9), (3, 10), (4, 7), (4, 8), (4, 9), (4, 10), (5, 6), (5, 7), (5, 9), (5, 10)])
```


## Complete Example

```python
# Workflow
G = nx.Graph([(1, 6), (1, 7), (1, 8), (1, 9), (2, 6), (2, 7), (2, 8), (2, 10), (3, 6), (3, 8), (3, 9), (3, 10), (4, 7), (4, 8), (4, 9), (4, 10), (5, 6), (5, 7), (5, 9), (5, 10)])
```

## Next Steps


---

*Source: test_extendability.py:51 | Complexity: Beginner | Last updated: 2026-06-02*