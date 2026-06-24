# How To: Copy And Deepcopy

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate MultiIndex: test copy and deepcopy

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex(...)

```python
idx = MultiIndex(levels=[['foo', 'bar'], ['fizz', 'buzz']], codes=[[0, 0, 0, 1], [0, 0, 1, 1]], names=['first', 'second'])
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
idx = MultiIndex(levels=[['foo', 'bar'], ['fizz', 'buzz']], codes=[[0, 0, 0, 1], [0, 0, 1, 1]], names=['first', 'second'])
```

## Next Steps


---

*Source: test_copy.py:48 | Complexity: Beginner | Last updated: 2026-06-02*