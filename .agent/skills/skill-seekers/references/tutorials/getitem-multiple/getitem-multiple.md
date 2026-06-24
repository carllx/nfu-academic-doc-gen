# How To: Getitem Multiple

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem multiple

## Prerequisites

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `IPython.core.completer`


## Step-by-Step Guide

### Step 1: Assign data = value

```python
data = [{'id': 1, 'buyer': 'A'}, {'id': 2, 'buyer': 'B'}]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(data, index=date_range('2016-01-01', periods=2))
```

### Step 3: Assign r = df.groupby.resample(...)

```python
r = df.groupby('id').resample('1D')
```

### Step 4: Assign result = unknown.count(...)

```python
result = r['buyer'].count()
```

### Step 5: Assign exp_mi = pd.MultiIndex.from_arrays(...)

```python
exp_mi = pd.MultiIndex.from_arrays([[1, 2], df.index], names=('id', None))
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, 1], index=exp_mi, name='buyer')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = unknown.count(...)

```python
result = r['buyer'].count()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
data = [{'id': 1, 'buyer': 'A'}, {'id': 2, 'buyer': 'B'}]
df = DataFrame(data, index=date_range('2016-01-01', periods=2))
r = df.groupby('id').resample('1D')
result = r['buyer'].count()
exp_mi = pd.MultiIndex.from_arrays([[1, 2], df.index], names=('id', None))
expected = Series([1, 1], index=exp_mi, name='buyer')
tm.assert_series_equal(result, expected)
result = r['buyer'].count()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_resampler_grouper.py:117 | Complexity: Advanced | Last updated: 2026-06-02*