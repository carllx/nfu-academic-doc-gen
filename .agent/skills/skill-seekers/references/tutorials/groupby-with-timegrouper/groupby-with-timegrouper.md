# How To: Groupby With Timegrouper

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test groupby with timegrouper

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.groupby.ops`

**Setup Required:**
```python
# Fixtures: using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df_original = DataFrame(...)

```python
df_original = DataFrame({'Buyer': 'Carl Carl Carl Carl Joe Carl'.split(), 'Quantity': [18, 3, 5, 1, 9, 3], 'Date': [datetime(2013, 9, 1, 13, 0), datetime(2013, 9, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 3, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 9, 2, 14, 0)]})
```

### Step 2: Assign df_reordered = df_original.sort_values(...)

```python
df_reordered = df_original.sort_values(by='Quantity')
```

### Step 3: Assign df = df.set_index(...)

```python
df = df.set_index(['Date'])
```

### Step 4: Assign exp_dti = date_range(...)

```python
exp_dti = date_range('20130901', '20131205', freq='5D', name='Date', inclusive='left', unit=df.index.unit)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'Buyer': '' if using_infer_string else 0, 'Quantity': 0}, index=exp_dti)
```

### Step 6: Assign expected = expected.astype(...)

```python
expected = expected.astype({'Buyer': object})
```

### Step 7: Assign unknown = 'CarlCarlCarl'

```python
expected.iloc[0, 0] = 'CarlCarlCarl'
```

### Step 8: Assign unknown = 'CarlCarl'

```python
expected.iloc[6, 0] = 'CarlCarl'
```

### Step 9: Assign unknown = 'Joe'

```python
expected.iloc[18, 0] = 'Joe'
```

### Step 10: Assign unknown = np.array(...)

```python
expected.iloc[[0, 6, 18], 1] = np.array([24, 6, 9], dtype='int64')
```

### Step 11: Assign result1 = df.resample.sum(...)

```python
result1 = df.resample('5D').sum()
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result1, expected)
```

### Step 13: Assign df_sorted = df.sort_index(...)

```python
df_sorted = df.sort_index()
```

### Step 14: Assign result2 = df_sorted.groupby.sum(...)

```python
result2 = df_sorted.groupby(Grouper(freq='5D')).sum()
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result2, expected)
```

### Step 16: Assign result3 = df.groupby.sum(...)

```python
result3 = df.groupby(Grouper(freq='5D')).sum()
```

### Step 17: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result3, expected)
```

### Step 18: Assign expected = expected.astype(...)

```python
expected = expected.astype({'Buyer': 'str'})
```


## Complete Example

```python
# Setup
# Fixtures: using_infer_string

# Workflow
df_original = DataFrame({'Buyer': 'Carl Carl Carl Carl Joe Carl'.split(), 'Quantity': [18, 3, 5, 1, 9, 3], 'Date': [datetime(2013, 9, 1, 13, 0), datetime(2013, 9, 1, 13, 5), datetime(2013, 10, 1, 20, 0), datetime(2013, 10, 3, 10, 0), datetime(2013, 12, 2, 12, 0), datetime(2013, 9, 2, 14, 0)]})
df_reordered = df_original.sort_values(by='Quantity')
for df in [df_original, df_reordered]:
    df = df.set_index(['Date'])
    exp_dti = date_range('20130901', '20131205', freq='5D', name='Date', inclusive='left', unit=df.index.unit)
    expected = DataFrame({'Buyer': '' if using_infer_string else 0, 'Quantity': 0}, index=exp_dti)
    expected = expected.astype({'Buyer': object})
    if using_infer_string:
        expected = expected.astype({'Buyer': 'str'})
    expected.iloc[0, 0] = 'CarlCarlCarl'
    expected.iloc[6, 0] = 'CarlCarl'
    expected.iloc[18, 0] = 'Joe'
    expected.iloc[[0, 6, 18], 1] = np.array([24, 6, 9], dtype='int64')
    result1 = df.resample('5D').sum()
    tm.assert_frame_equal(result1, expected)
    df_sorted = df.sort_index()
    result2 = df_sorted.groupby(Grouper(freq='5D')).sum()
    tm.assert_frame_equal(result2, expected)
    result3 = df.groupby(Grouper(freq='5D')).sum()
    tm.assert_frame_equal(result3, expected)
```

## Next Steps


---

*Source: test_timegrouper.py:76 | Complexity: Advanced | Last updated: 2026-06-02*