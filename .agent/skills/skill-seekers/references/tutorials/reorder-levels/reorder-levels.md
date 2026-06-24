# How To: Reorder Levels

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate MultiIndex: test reorder levels

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign e_idx = MultiIndex(...)

```python
e_idx = MultiIndex(levels=[['one', 'two', 'three'], [0, 1], ['bar']], codes=[[0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0]], names=['L1', 'L2', 'L0'])
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
e_idx = MultiIndex(levels=[['one', 'two', 'three'], [0, 1], ['bar']], codes=[[0, 1, 2, 0, 1, 2], [0, 1, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0]], names=['L1', 'L2', 'L0'])
```

## Next Steps


---

*Source: test_reorder_levels.py:31 | Complexity: Beginner | Last updated: 2026-06-02*