# How To: Rename Series With Multiindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename series with multiindex

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [['bar', 'baz', 'baz', 'foo', 'qux'], ['one', 'one', 'two', 'two', 'one']]
```

### Step 2: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays, names=['first', 'second'])
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(np.ones(5), index=index)
```

### Step 4: Assign result = ser.rename(...)

```python
result = ser.rename(index={'one': 'yes'}, level='second', errors='raise')
```

### Step 5: Assign arrays_expected = value

```python
arrays_expected = [['bar', 'baz', 'baz', 'foo', 'qux'], ['yes', 'yes', 'two', 'two', 'yes']]
```

### Step 6: Assign index_expected = MultiIndex.from_arrays(...)

```python
index_expected = MultiIndex.from_arrays(arrays_expected, names=['first', 'second'])
```

### Step 7: Assign series_expected = Series(...)

```python
series_expected = Series(np.ones(5), index=index_expected)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, series_expected)
```


## Complete Example

```python
# Workflow
arrays = [['bar', 'baz', 'baz', 'foo', 'qux'], ['one', 'one', 'two', 'two', 'one']]
index = MultiIndex.from_arrays(arrays, names=['first', 'second'])
ser = Series(np.ones(5), index=index)
result = ser.rename(index={'one': 'yes'}, level='second', errors='raise')
arrays_expected = [['bar', 'baz', 'baz', 'foo', 'qux'], ['yes', 'yes', 'two', 'two', 'yes']]
index_expected = MultiIndex.from_arrays(arrays_expected, names=['first', 'second'])
series_expected = Series(np.ones(5), index=index_expected)
tm.assert_series_equal(result, series_expected)
```

## Next Steps


---

*Source: test_rename.py:123 | Complexity: Advanced | Last updated: 2026-06-02*