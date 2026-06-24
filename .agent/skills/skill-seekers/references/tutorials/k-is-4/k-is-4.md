# How To: K Is 4

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate Graph: test k is 4

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph([(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 1), (9, 2), (9, 3), (9, 4), (9, 7), (10, 1), (10, 2), (10, 3), (10, 4), (10, 6), (11, 1), (11, 2), (11, 5), (11, 6), (11, 7), (12, 1), (12, 3), (12, 5), (12, 6), (12, 7), (13, 2), (13, 4), (13, 5), (13, 6), (13, 7), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7)])
```


## Complete Example

```python
# Workflow
G = nx.Graph([(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (9, 1), (9, 2), (9, 3), (9, 4), (9, 7), (10, 1), (10, 2), (10, 3), (10, 4), (10, 6), (11, 1), (11, 2), (11, 5), (11, 6), (11, 7), (12, 1), (12, 3), (12, 5), (12, 6), (12, 7), (13, 2), (13, 4), (13, 5), (13, 6), (13, 7), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7)])
```

## Next Steps


---

*Source: test_extendability.py:79 | Complexity: Beginner | Last updated: 2026-06-02*