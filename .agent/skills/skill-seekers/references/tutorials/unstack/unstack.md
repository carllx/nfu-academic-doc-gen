# How To: Unstack

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate MultiIndex: test unstack

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[['bar', 'foo'], ['one', 'three', 'two']], codes=[[1, 1, 0, 0], [0, 1, 0, 2]])
```


## Complete Example

```python
# Workflow
index = MultiIndex(levels=[['bar', 'foo'], ['one', 'three', 'two']], codes=[[1, 1, 0, 0], [0, 1, 0, 2]])
```

## Next Steps


---

*Source: test_unstack.py:28 | Complexity: Beginner | Last updated: 2026-06-02*