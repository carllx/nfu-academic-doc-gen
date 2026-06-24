# How To: Reverse Cuthill Mckee

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: test reverse cuthill mckee

## Prerequisites

**Required Modules:**
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(0, 3), (0, 5), (1, 2), (1, 4), (1, 6), (1, 9), (2, 3), (2, 4), (3, 5), (3, 8), (4, 6), (5, 6), (5, 7), (6, 7)])
```


## Complete Example

```python
# Workflow
G = nx.Graph([(0, 3), (0, 5), (1, 2), (1, 4), (1, 6), (1, 9), (2, 3), (2, 4), (3, 5), (3, 8), (4, 6), (5, 6), (5, 7), (6, 7)])
```

## Next Steps


---

*Source: test_rcm.py:8 | Complexity: Beginner | Last updated: 2026-06-02*