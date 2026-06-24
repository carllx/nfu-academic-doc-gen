# How To: Format Integer Names

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate MultiIndex: test format integer names

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
index = MultiIndex(levels=[[0, 1], [0, 1]], codes=[[0, 0, 1, 1], [0, 1, 0, 1]], names=[0, 1])
```


## Complete Example

```python
# Workflow
index = MultiIndex(levels=[[0, 1], [0, 1]], codes=[[0, 0, 1, 1], [0, 1, 0, 1]], names=[0, 1])
```

## Next Steps


---

*Source: test_formats.py:20 | Complexity: Beginner | Last updated: 2026-06-02*