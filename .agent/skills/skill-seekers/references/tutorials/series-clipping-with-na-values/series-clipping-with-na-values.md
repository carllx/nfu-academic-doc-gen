# How To: Series Clipping With Na Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series clipping with na values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_ea_dtype, nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([nulls_fixture, 1.0, 3.0], dtype=any_numeric_ea_dtype)
```

### Step 2: Assign s_clipped_upper = ser.clip(...)

```python
s_clipped_upper = ser.clip(upper=2.0)
```

### Step 3: Assign s_clipped_lower = ser.clip(...)

```python
s_clipped_lower = ser.clip(lower=2.0)
```

### Step 4: Assign expected_upper = Series(...)

```python
expected_upper = Series([nulls_fixture, 1.0, 2.0], dtype=any_numeric_ea_dtype)
```

### Step 5: Assign expected_lower = Series(...)

```python
expected_lower = Series([nulls_fixture, 2.0, 3.0], dtype=any_numeric_ea_dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s_clipped_upper, expected_upper)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s_clipped_lower, expected_lower)
```

### Step 8: Call pytest.skip()

```python
pytest.skip('See test_constructor_mismatched_null_nullable_dtype')
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_ea_dtype, nulls_fixture

# Workflow
if nulls_fixture is pd.NaT:
    pytest.skip('See test_constructor_mismatched_null_nullable_dtype')
ser = Series([nulls_fixture, 1.0, 3.0], dtype=any_numeric_ea_dtype)
s_clipped_upper = ser.clip(upper=2.0)
s_clipped_lower = ser.clip(lower=2.0)
expected_upper = Series([nulls_fixture, 1.0, 2.0], dtype=any_numeric_ea_dtype)
expected_lower = Series([nulls_fixture, 2.0, 3.0], dtype=any_numeric_ea_dtype)
tm.assert_series_equal(s_clipped_upper, expected_upper)
tm.assert_series_equal(s_clipped_lower, expected_lower)
```

## Next Steps


---

*Source: test_clip.py:44 | Complexity: Advanced | Last updated: 2026-06-02*