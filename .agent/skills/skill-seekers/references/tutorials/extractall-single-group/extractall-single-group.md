# How To: Extractall Single Group

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test extractall single group

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a3', 'b3', 'd4c2'], name='series_name', dtype=any_string_dtype)
```

### Step 2: Assign expected_index = MultiIndex.from_tuples(...)

```python
expected_index = MultiIndex.from_tuples([(0, 0), (1, 0), (2, 0), (2, 1)], names=(None, 'match'))
```

### Step 3: Assign result = s.str.extractall(...)

```python
result = s.str.extractall('(?P<letter>[a-z])')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'letter': ['a', 'b', 'd', 'c']}, index=expected_index, dtype=any_string_dtype)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = s.str.extractall(...)

```python
result = s.str.extractall('([a-z])')
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame(['a', 'b', 'd', 'c'], index=expected_index, dtype=any_string_dtype)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['a3', 'b3', 'd4c2'], name='series_name', dtype=any_string_dtype)
expected_index = MultiIndex.from_tuples([(0, 0), (1, 0), (2, 0), (2, 1)], names=(None, 'match'))
result = s.str.extractall('(?P<letter>[a-z])')
expected = DataFrame({'letter': ['a', 'b', 'd', 'c']}, index=expected_index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
result = s.str.extractall('([a-z])')
expected = DataFrame(['a', 'b', 'd', 'c'], index=expected_index, dtype=any_string_dtype)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_extract.py:504 | Complexity: Advanced | Last updated: 2026-06-02*