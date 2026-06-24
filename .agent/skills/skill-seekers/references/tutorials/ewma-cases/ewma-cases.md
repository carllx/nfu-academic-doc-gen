# How To: Ewma Cases

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ewma cases

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: adjust, ignore_na
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1.0, 2.0, 4.0, 8.0])
```

### Step 2: Assign result = s.ewm.mean(...)

```python
result = s.ewm(com=2.0, adjust=adjust, ignore_na=ignore_na).mean()
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1.0, 1.6, 2.736842, 4.923077])
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([1.0, 1.333333, 2.222222, 4.148148])
```


## Complete Example

```python
# Setup
# Fixtures: adjust, ignore_na

# Workflow
s = Series([1.0, 2.0, 4.0, 8.0])
if adjust:
    expected = Series([1.0, 1.6, 2.736842, 4.923077])
else:
    expected = Series([1.0, 1.333333, 2.222222, 4.148148])
result = s.ewm(com=2.0, adjust=adjust, ignore_na=ignore_na).mean()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_ewm.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*