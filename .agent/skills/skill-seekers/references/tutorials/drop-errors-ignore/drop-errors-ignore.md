# How To: Drop Errors Ignore

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test drop errors ignore

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: labels, level
```

## Step-by-Step Guide

### Step 1: Assign mi = MultiIndex.from_arrays(...)

```python
mi = MultiIndex.from_arrays([[1, 2, 3], [4, 5, 6]], names=['a', 'b'])
```

### Step 2: Assign s = Series(...)

```python
s = Series([10, 20, 30], index=mi)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame([10, 20, 30], index=mi)
```

### Step 4: Assign expected_s = s.drop(...)

```python
expected_s = s.drop(labels, level=level, errors='ignore')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected_s)
```

### Step 6: Assign expected_df = df.drop(...)

```python
expected_df = df.drop(labels, level=level, errors='ignore')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected_df)
```


## Complete Example

```python
# Setup
# Fixtures: labels, level

# Workflow
mi = MultiIndex.from_arrays([[1, 2, 3], [4, 5, 6]], names=['a', 'b'])
s = Series([10, 20, 30], index=mi)
df = DataFrame([10, 20, 30], index=mi)
expected_s = s.drop(labels, level=level, errors='ignore')
tm.assert_series_equal(s, expected_s)
expected_df = df.drop(labels, level=level, errors='ignore')
tm.assert_frame_equal(df, expected_df)
```

## Next Steps


---

*Source: test_drop.py:40 | Complexity: Intermediate | Last updated: 2026-06-02*