# How To: Operators Na Handling

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test operators na handling

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `operator`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['foo', 'bar', 'baz', np.nan])
```

### Step 2: Assign result = value

```python
result = 'prefix_' + ser
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['prefix_foo', 'prefix_bar', 'prefix_baz', np.nan])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = value

```python
result = ser + '_suffix'
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['foo_suffix', 'bar_suffix', 'baz_suffix', np.nan])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(['foo', 'bar', 'baz', np.nan])
result = 'prefix_' + ser
expected = Series(['prefix_foo', 'prefix_bar', 'prefix_baz', np.nan])
tm.assert_series_equal(result, expected)
result = ser + '_suffix'
expected = Series(['foo_suffix', 'bar_suffix', 'baz_suffix', np.nan])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_object.py:198 | Complexity: Intermediate | Last updated: 2026-06-02*