# How To: Dt64 Mean

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate take: test dt64 mean

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture, box
```

## Step-by-Step Guide

### Step 1: Assign dti = dti.take(...)

```python
dti = dti.take([4, 1, 3, 10, 9, 7, 8, 5, 0, 2, 6])
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture, box

# Workflow
dti = dti.take([4, 1, 3, 10, 9, 7, 8, 5, 0, 2, 6])
```

## Next Steps


---

*Source: test_stat_reductions.py:25 | Complexity: Beginner | Last updated: 2026-06-02*