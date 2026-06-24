# How To: Sort Index Ignore Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test sort index ignore index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: inplace, original_list, sorted_list, ascending, ignore_index, output_index
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(original_list)
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(sorted_list, index=output_index)
```

### Step 3: Assign kwargs = value

```python
kwargs = {'ascending': ascending, 'ignore_index': ignore_index, 'inplace': inplace}
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_ser, expected)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, Series(original_list))
```

### Step 6: Assign result_ser = ser.copy(...)

```python
result_ser = ser.copy()
```

### Step 7: Call result_ser.sort_index()

```python
result_ser.sort_index(**kwargs)
```

### Step 8: Assign result_ser = ser.sort_index(...)

```python
result_ser = ser.sort_index(**kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: inplace, original_list, sorted_list, ascending, ignore_index, output_index

# Workflow
ser = Series(original_list)
expected = Series(sorted_list, index=output_index)
kwargs = {'ascending': ascending, 'ignore_index': ignore_index, 'inplace': inplace}
if inplace:
    result_ser = ser.copy()
    result_ser.sort_index(**kwargs)
else:
    result_ser = ser.sort_index(**kwargs)
tm.assert_series_equal(result_ser, expected)
tm.assert_series_equal(ser, Series(original_list))
```

## Next Steps


---

*Source: test_sort_index.py:159 | Complexity: Advanced | Last updated: 2026-06-02*