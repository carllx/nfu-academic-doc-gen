# How To: Groupby Preserves Subclass

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test groupby preserves subclass

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: obj, groupby_func
```

## Step-by-Step Guide

### Step 1: Assign grouped = obj.groupby(...)

```python
grouped = obj.groupby(np.arange(0, 10))
```

**Verification:**
```python
assert isinstance(grouped.get_group(0), type(obj))
```

### Step 2: Assign args = get_groupby_method_args(...)

```python
args = get_groupby_method_args(groupby_func, obj)
```

**Verification:**
```python
assert isinstance(result1, tm.SubclassedSeries)
```

### Step 3: Assign warn = value

```python
warn = FutureWarning if groupby_func == 'fillna' else None
```

**Verification:**
```python
assert isinstance(result1, type(obj))
```

### Step 4: Assign msg = value

```python
msg = f'{type(grouped).__name__}.fillna is deprecated'
```

### Step 5: Assign slices = value

```python
slices = {'ngroup', 'cumcount', 'size'}
```

### Step 6: Call pytest.skip()

```python
pytest.skip(f'Not applicable for Series and {groupby_func}')
```

### Step 7: Assign result1 = getattr(...)

```python
result1 = getattr(grouped, groupby_func)(*args)
```

### Step 8: Assign result2 = grouped.agg(...)

```python
result2 = grouped.agg(groupby_func, *args)
```

**Verification:**
```python
assert isinstance(result1, tm.SubclassedSeries)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result1, result2)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result1, result2)
```


## Complete Example

```python
# Setup
# Fixtures: obj, groupby_func

# Workflow
if isinstance(obj, Series) and groupby_func in {'corrwith'}:
    pytest.skip(f'Not applicable for Series and {groupby_func}')
grouped = obj.groupby(np.arange(0, 10))
assert isinstance(grouped.get_group(0), type(obj))
args = get_groupby_method_args(groupby_func, obj)
warn = FutureWarning if groupby_func == 'fillna' else None
msg = f'{type(grouped).__name__}.fillna is deprecated'
with tm.assert_produces_warning(warn, match=msg, raise_on_extra_warnings=False):
    result1 = getattr(grouped, groupby_func)(*args)
with tm.assert_produces_warning(warn, match=msg, raise_on_extra_warnings=False):
    result2 = grouped.agg(groupby_func, *args)
slices = {'ngroup', 'cumcount', 'size'}
if isinstance(obj, DataFrame) and groupby_func in slices:
    assert isinstance(result1, tm.SubclassedSeries)
else:
    assert isinstance(result1, type(obj))
if isinstance(result1, DataFrame):
    tm.assert_frame_equal(result1, result2)
else:
    tm.assert_series_equal(result1, result2)
```

## Next Steps


---

*Source: test_groupby_subclass.py:26 | Complexity: Advanced | Last updated: 2026-06-02*