# How To: Size Axis 1

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test size axis 1

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df, axis_1, by, sort, dropna
```

## Step-by-Step Guide

### Step 1: Assign counts = value

```python
counts = {key: sum((value == key for value in by)) for key in dict.fromkeys(by)}
```

### Step 2: Assign expected = Series(...)

```python
expected = Series(counts, dtype='int64')
```

### Step 3: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 4: Assign result = grouped.size(...)

```python
result = grouped.size()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign counts = value

```python
counts = {key: value for key, value in counts.items() if key is not None}
```

### Step 7: Assign expected = expected.sort_index(...)

```python
expected = expected.sort_index()
```

### Step 8: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(int)
```

### Step 9: Assign grouped = df.groupby(...)

```python
grouped = df.groupby(by=by, axis=axis_1, sort=sort, dropna=dropna)
```


## Complete Example

```python
# Setup
# Fixtures: df, axis_1, by, sort, dropna

# Workflow
counts = {key: sum((value == key for value in by)) for key in dict.fromkeys(by)}
if dropna:
    counts = {key: value for key, value in counts.items() if key is not None}
expected = Series(counts, dtype='int64')
if sort:
    expected = expected.sort_index()
if is_integer_dtype(expected.index.dtype) and (not any((x is None for x in by))):
    expected.index = expected.index.astype(int)
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grouped = df.groupby(by=by, axis=axis_1, sort=sort, dropna=dropna)
result = grouped.size()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_size.py:33 | Complexity: Advanced | Last updated: 2026-06-02*