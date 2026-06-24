# How To: Rolling Pairwise Cov Corr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling pairwise cov corr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`

**Setup Required:**
```python
# Fixtures: func, frame
```

## Step-by-Step Guide

### Step 1: Assign result = getattr(...)

```python
result = getattr(frame.rolling(window=10, min_periods=5), func)()
```

### Step 2: Assign result = value

```python
result = result.loc[(slice(None), 1), 5]
```

### Step 3: Assign result.index = result.index.droplevel(...)

```python
result.index = result.index.droplevel(1)
```

### Step 4: Assign expected = getattr(...)

```python
expected = getattr(frame[1].rolling(window=10, min_periods=5), func)(frame[5])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected, check_names=False)
```


## Complete Example

```python
# Setup
# Fixtures: func, frame

# Workflow
result = getattr(frame.rolling(window=10, min_periods=5), func)()
result = result.loc[(slice(None), 1), 5]
result.index = result.index.droplevel(1)
expected = getattr(frame[1].rolling(window=10, min_periods=5), func)(frame[5])
tm.assert_series_equal(result, expected, check_names=False)
```

## Next Steps


---

*Source: test_pairwise.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*