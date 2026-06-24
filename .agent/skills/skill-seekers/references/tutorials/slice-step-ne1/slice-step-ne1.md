# How To: Slice Step Ne1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice step ne1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: series_with_interval_index
```

## Step-by-Step Guide

### Step 1: Assign ser = series_with_interval_index.copy(...)

```python
ser = series_with_interval_index.copy()
```

### Step 2: Assign expected = value

```python
expected = ser.iloc[0:4:2]
```

### Step 3: Assign result = value

```python
result = ser[0:4:2]
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result2 = value

```python
result2 = ser[0:4][::2]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected)
```


## Complete Example

```python
# Setup
# Fixtures: series_with_interval_index

# Workflow
ser = series_with_interval_index.copy()
expected = ser.iloc[0:4:2]
result = ser[0:4:2]
tm.assert_series_equal(result, expected)
result2 = ser[0:4][::2]
tm.assert_series_equal(result2, expected)
```

## Next Steps


---

*Source: test_interval_new.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*