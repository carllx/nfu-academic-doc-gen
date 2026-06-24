# How To: From Records Series Categorical Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records series categorical index

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = CategoricalIndex(...)

```python
index = CategoricalIndex([Interval(-20, -10), Interval(-10, 0), Interval(0, 10)])
```

### Step 2: Assign series_of_dicts = Series(...)

```python
series_of_dicts = Series([{'a': 1}, {'a': 2}, {'b': 3}], index=index)
```

### Step 3: Assign frame = DataFrame.from_records(...)

```python
frame = DataFrame.from_records(series_of_dicts, index=index)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, np.nan], 'b': [np.nan, np.nan, 3]}, index=index)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(frame, expected)
```


## Complete Example

```python
# Workflow
index = CategoricalIndex([Interval(-20, -10), Interval(-10, 0), Interval(0, 10)])
series_of_dicts = Series([{'a': 1}, {'a': 2}, {'b': 3}], index=index)
frame = DataFrame.from_records(series_of_dicts, index=index)
expected = DataFrame({'a': [1, 2, np.nan], 'b': [np.nan, np.nan, 3]}, index=index)
tm.assert_frame_equal(frame, expected)
```

## Next Steps


---

*Source: test_from_records.py:267 | Complexity: Intermediate | Last updated: 2026-06-02*