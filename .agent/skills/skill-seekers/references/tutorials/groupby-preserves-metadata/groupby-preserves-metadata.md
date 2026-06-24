# How To: Groupby Preserves Metadata

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby preserves metadata

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`


## Step-by-Step Guide

### Step 1: Assign custom_df = tm.SubclassedDataFrame(...)

```python
custom_df = tm.SubclassedDataFrame({'a': [1, 2, 3], 'b': [1, 1, 2], 'c': [7, 8, 9]})
```

**Verification:**
```python
assert 'testattr' in custom_df._metadata
```

### Step 2: Assign custom_df.testattr = 'hello'

```python
custom_df.testattr = 'hello'
```

**Verification:**
```python
assert group_df.testattr == 'hello'
```

### Step 3: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

**Verification:**
```python
assert isinstance(group, tm.SubclassedDataFrame)
```

### Step 4: Assign expected = tm.SubclassedSeries(...)

```python
expected = tm.SubclassedSeries(['hello'] * 3, index=Index([7, 8, 9], name='c'))
```

**Verification:**
```python
assert hasattr(group, 'testattr')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert group.testattr == 'hello'
```

### Step 6: Assign result = custom_df.groupby.apply(...)

```python
result = custom_df.groupby('c').apply(func, include_groups=False)
```

**Verification:**
```python
assert isinstance(group, tm.SubclassedSeries)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert hasattr(group, 'testattr')
```

### Step 8: Assign result = unknown.apply(...)

```python
result = custom_df.groupby('c')[['a', 'b']].apply(func)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign custom_series = tm.SubclassedSeries(...)

```python
custom_series = tm.SubclassedSeries([1, 2, 3])
```

### Step 11: Assign custom_series.testattr = 'hello'

```python
custom_series.testattr = 'hello'
```

### Step 12: Assign result = custom_series.groupby.apply(...)

```python
result = custom_series.groupby(custom_df['c']).apply(func2)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Assign result = custom_series.groupby.agg(...)

```python
result = custom_series.groupby(custom_df['c']).agg(func2)
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert group_df.testattr == 'hello'
```

### Step 16: Assign result = custom_df.groupby.apply(...)

```python
result = custom_df.groupby('c').apply(func)
```

**Verification:**
```python
assert isinstance(group, tm.SubclassedSeries)
```


## Complete Example

```python
# Workflow
custom_df = tm.SubclassedDataFrame({'a': [1, 2, 3], 'b': [1, 1, 2], 'c': [7, 8, 9]})
assert 'testattr' in custom_df._metadata
custom_df.testattr = 'hello'
for _, group_df in custom_df.groupby('c'):
    assert group_df.testattr == 'hello'

def func(group):
    assert isinstance(group, tm.SubclassedDataFrame)
    assert hasattr(group, 'testattr')
    assert group.testattr == 'hello'
    return group.testattr
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg, raise_on_extra_warnings=False, check_stacklevel=False):
    result = custom_df.groupby('c').apply(func)
expected = tm.SubclassedSeries(['hello'] * 3, index=Index([7, 8, 9], name='c'))
tm.assert_series_equal(result, expected)
result = custom_df.groupby('c').apply(func, include_groups=False)
tm.assert_series_equal(result, expected)
result = custom_df.groupby('c')[['a', 'b']].apply(func)
tm.assert_series_equal(result, expected)

def func2(group):
    assert isinstance(group, tm.SubclassedSeries)
    assert hasattr(group, 'testattr')
    return group.testattr
custom_series = tm.SubclassedSeries([1, 2, 3])
custom_series.testattr = 'hello'
result = custom_series.groupby(custom_df['c']).apply(func2)
tm.assert_series_equal(result, expected)
result = custom_series.groupby(custom_df['c']).agg(func2)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby_subclass.py:60 | Complexity: Advanced | Last updated: 2026-06-02*