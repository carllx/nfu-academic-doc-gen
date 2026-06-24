# How To: Dti Snap

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Instantiate DatetimeIndex: test dti snap

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: name, tz, unit
```

## Step-by-Step Guide

### Step 1: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex(['1/1/2002', '1/2/2002', '1/3/2002', '1/4/2002', '1/5/2002', '1/6/2002', '1/7/2002'], name=name, tz=tz, freq='D')
```


## Complete Example

```python
# Setup
# Fixtures: name, tz, unit

# Workflow
dti = DatetimeIndex(['1/1/2002', '1/2/2002', '1/3/2002', '1/4/2002', '1/5/2002', '1/6/2002', '1/7/2002'], name=name, tz=tz, freq='D')
```

## Next Steps


---

*Source: test_snap.py:14 | Complexity: Beginner | Last updated: 2026-06-02*