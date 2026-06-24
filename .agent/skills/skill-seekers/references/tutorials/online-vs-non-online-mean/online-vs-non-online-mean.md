# How To: Online Vs Non Online Mean

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: pytest

## Overview

Configuration example: test online vs non online mean

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: obj, nogil, parallel, nopython, adjust, ignore_na
```

## Step-by-Step Guide

### Step 1: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```


## Complete Example

```python
# Setup
# Fixtures: obj, nogil, parallel, nopython, adjust, ignore_na

# Workflow
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

## Next Steps


---

*Source: test_online.py:44 | Complexity: Beginner | Last updated: 2026-06-02*