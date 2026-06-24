# How To: Format Sparse Display

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate MultiIndex: test format sparse display

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
index = MultiIndex(levels=[[0, 1], [0, 1], [0, 1], [0]], codes=[[0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0]])
```


## Complete Example

```python
# Workflow
index = MultiIndex(levels=[[0, 1], [0, 1], [0, 1], [0]], codes=[[0, 0, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0]])
```

## Next Steps


---

*Source: test_formats.py:38 | Complexity: Beginner | Last updated: 2026-06-02*