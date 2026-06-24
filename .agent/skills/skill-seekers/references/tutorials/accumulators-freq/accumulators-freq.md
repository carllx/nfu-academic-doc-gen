# How To: Accumulators Freq

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test accumulators freq

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = DatetimeArray._from_sequence._with_freq(...)

```python
arr = DatetimeArray._from_sequence(['2000-01-01', '2000-01-02', '2000-01-03'], dtype='M8[ns]')._with_freq('infer')
```

### Step 2: Assign result = arr._accumulate(...)

```python
result = arr._accumulate('cummin')
```

### Step 3: Assign expected = DatetimeArray._from_sequence(...)

```python
expected = DatetimeArray._from_sequence(['2000-01-01'] * 3, dtype='M8[ns]')
```

### Step 4: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected)
```

### Step 5: Assign result = arr._accumulate(...)

```python
result = arr._accumulate('cummax')
```

### Step 6: Assign expected = DatetimeArray._from_sequence(...)

```python
expected = DatetimeArray._from_sequence(['2000-01-01', '2000-01-02', '2000-01-03'], dtype='M8[ns]')
```

### Step 7: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = DatetimeArray._from_sequence(['2000-01-01', '2000-01-02', '2000-01-03'], dtype='M8[ns]')._with_freq('infer')
result = arr._accumulate('cummin')
expected = DatetimeArray._from_sequence(['2000-01-01'] * 3, dtype='M8[ns]')
tm.assert_datetime_array_equal(result, expected)
result = arr._accumulate('cummax')
expected = DatetimeArray._from_sequence(['2000-01-01', '2000-01-02', '2000-01-03'], dtype='M8[ns]')
tm.assert_datetime_array_equal(result, expected)
```

## Next Steps


---

*Source: test_cumulative.py:8 | Complexity: Intermediate | Last updated: 2026-06-02*