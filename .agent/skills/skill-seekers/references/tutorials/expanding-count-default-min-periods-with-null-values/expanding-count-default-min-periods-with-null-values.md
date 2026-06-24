# How To: Expanding Count Default Min Periods With Null Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test expanding count default min periods with null values

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

### Step 1: Assign values = value

```python
values = [1, 2, 3, np.nan, 4, 5, 6]
```

### Step 2: Assign expected_counts = value

```python
expected_counts = [1.0, 2.0, 3.0, 3.0, 4.0, 5.0, 6.0]
```

### Step 3: Assign result = frame_or_series.expanding.count(...)

```python
result = frame_or_series(values).expanding().count()
```

### Step 4: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(expected_counts)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
values = [1, 2, 3, np.nan, 4, 5, 6]
expected_counts = [1.0, 2.0, 3.0, 3.0, 4.0, 5.0, 6.0]
result = frame_or_series(values).expanding().count()
expected = frame_or_series(expected_counts)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_expanding.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*