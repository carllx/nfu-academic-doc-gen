# How To: Astype Conversion

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype conversion

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2016-05-16', 'NaT', NaT, np.nan], freq='D', name='idx')
```

### Step 2: Assign result = idx.astype(...)

```python
result = idx.astype(object)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([Period('2016-05-16', freq='D')] + [Period(NaT, freq='D')] * 3, dtype='object', name='idx')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = idx.astype(...)

```python
result = idx.astype(np.int64)
```

### Step 6: Assign expected = Index(...)

```python
expected = Index([16937] + [-9223372036854775808] * 3, dtype=np.int64, name='idx')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign result = idx.astype(...)

```python
result = idx.astype(str)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 10: Assign idx = period_range(...)

```python
idx = period_range('1990', '2009', freq='Y', name='idx')
```

### Step 11: Assign result = idx.astype(...)

```python
result = idx.astype('i8')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, Index(idx.asi8, name='idx'))
```

### Step 13: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result.values, idx.asi8)
```

### Step 14: Assign expected = Index(...)

```python
expected = Index([str(x) if x is not NaT else None for x in idx], name='idx', dtype='str')
```

### Step 15: Assign expected = Index(...)

```python
expected = Index([str(x) for x in idx], name='idx', dtype=object)
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
idx = PeriodIndex(['2016-05-16', 'NaT', NaT, np.nan], freq='D', name='idx')
result = idx.astype(object)
expected = Index([Period('2016-05-16', freq='D')] + [Period(NaT, freq='D')] * 3, dtype='object', name='idx')
tm.assert_index_equal(result, expected)
result = idx.astype(np.int64)
expected = Index([16937] + [-9223372036854775808] * 3, dtype=np.int64, name='idx')
tm.assert_index_equal(result, expected)
result = idx.astype(str)
if using_infer_string:
    expected = Index([str(x) if x is not NaT else None for x in idx], name='idx', dtype='str')
else:
    expected = Index([str(x) for x in idx], name='idx', dtype=object)
tm.assert_index_equal(result, expected)
idx = period_range('1990', '2009', freq='Y', name='idx')
result = idx.astype('i8')
tm.assert_index_equal(result, Index(idx.asi8, name='idx'))
tm.assert_numpy_array_equal(result.values, idx.asi8)
```

## Next Steps


---

*Source: test_astype.py:25 | Complexity: Advanced | Last updated: 2026-06-02*