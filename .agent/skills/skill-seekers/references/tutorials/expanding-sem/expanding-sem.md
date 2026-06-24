# How To: Expanding Sem

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test expanding sem

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

### Step 1: Assign obj = frame_or_series(...)

```python
obj = frame_or_series([0, 1, 2])
```

### Step 2: Assign result = obj.expanding.sem(...)

```python
result = obj.expanding().sem()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([np.nan] + [0.707107] * 2)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = Series(...)

```python
result = Series(result[0].values)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
obj = frame_or_series([0, 1, 2])
result = obj.expanding().sem()
if isinstance(result, DataFrame):
    result = Series(result[0].values)
expected = Series([np.nan] + [0.707107] * 2)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_expanding.py:221 | Complexity: Intermediate | Last updated: 2026-06-02*