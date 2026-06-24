# How To: Constructor From Frame Series Freq

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor from frame series freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `functools`
- `math`
- `operator`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`
- `pyarrow`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign dts = value

```python
dts = ['1-1-1990', '2-1-1990', '3-1-1990', '4-1-1990', '5-1-1990']
```

**Verification:**
```python
assert df['date'].dtype == dtype
```

### Step 2: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(dts, freq='MS')
```

**Verification:**
```python
assert freq == 'MS'
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((5, 3)))
```

### Step 4: Assign unknown = dts

```python
df['date'] = dts
```

### Step 5: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex(df['date'], freq='MS')
```

### Step 6: Assign dtype = value

```python
dtype = object if not using_infer_string else 'str'
```

**Verification:**
```python
assert df['date'].dtype == dtype
```

### Step 7: Assign expected.name = 'date'

```python
expected.name = 'date'
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series(dts, name='date')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(df['date'], expected)
```

### Step 11: Assign freq = pd.infer_freq(...)

```python
freq = pd.infer_freq(df['date'])
```

**Verification:**
```python
assert freq == 'MS'
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
dts = ['1-1-1990', '2-1-1990', '3-1-1990', '4-1-1990', '5-1-1990']
expected = DatetimeIndex(dts, freq='MS')
df = DataFrame(np.random.default_rng(2).random((5, 3)))
df['date'] = dts
result = DatetimeIndex(df['date'], freq='MS')
dtype = object if not using_infer_string else 'str'
assert df['date'].dtype == dtype
expected.name = 'date'
tm.assert_index_equal(result, expected)
expected = Series(dts, name='date')
tm.assert_series_equal(df['date'], expected)
if not using_infer_string:
    freq = pd.infer_freq(df['date'])
    assert freq == 'MS'
```

## Next Steps


---

*Source: test_base.py:154 | Complexity: Advanced | Last updated: 2026-06-02*