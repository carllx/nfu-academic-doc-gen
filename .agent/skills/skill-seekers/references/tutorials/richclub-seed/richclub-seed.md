# How To: Richclub Seed

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: test richclub seed

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (4, 5)])
```


## Complete Example

```python
# Workflow
G = nx.Graph([(0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (4, 5)])
```

## Next Steps


---

*Source: test_richclub.py:17 | Complexity: Beginner | Last updated: 2026-06-02*