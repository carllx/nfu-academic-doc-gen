# How To: Multiindex Slicers Datetimelike

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex slicers datetimelike

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign dates = value

```python
dates = [datetime(2012, 1, 1, 12, 12, 12) + timedelta(days=i) for i in range(6)]
```

### Step 2: Assign freq = value

```python
freq = [1, 2]
```

### Step 3: Assign index = MultiIndex.from_product(...)

```python
index = MultiIndex.from_product([dates, freq], names=['date', 'frequency'])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(6 * 2 * 4, dtype='int64').reshape(-1, 4), index=index, columns=list('ABCD'))
```

### Step 5: Assign idx = value

```python
idx = pd.IndexSlice
```

### Step 6: Assign expected = value

```python
expected = df.iloc[[0, 2, 4], [0, 1]]
```

### Step 7: Assign result = value

```python
result = df.loc[(slice(Timestamp('2012-01-01 12:12:12'), Timestamp('2012-01-03 12:12:12')), slice(1, 1)), slice('A', 'B')]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = df.loc[(idx[Timestamp('2012-01-01 12:12:12'):Timestamp('2012-01-03 12:12:12')], idx[1:1]), slice('A', 'B')]
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = value

```python
result = df.loc[(slice(Timestamp('2012-01-01 12:12:12'), Timestamp('2012-01-03 12:12:12')), 1), slice('A', 'B')]
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = value

```python
result = df.loc[(slice('2012-01-01 12:12:12', '2012-01-03 12:12:12'), slice(1, 1)), slice('A', 'B')]
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign result = value

```python
result = df.loc[(idx['2012-01-01 12:12:12':'2012-01-03 12:12:12'], 1), idx['A', 'B']]
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
dates = [datetime(2012, 1, 1, 12, 12, 12) + timedelta(days=i) for i in range(6)]
freq = [1, 2]
index = MultiIndex.from_product([dates, freq], names=['date', 'frequency'])
df = DataFrame(np.arange(6 * 2 * 4, dtype='int64').reshape(-1, 4), index=index, columns=list('ABCD'))
idx = pd.IndexSlice
expected = df.iloc[[0, 2, 4], [0, 1]]
result = df.loc[(slice(Timestamp('2012-01-01 12:12:12'), Timestamp('2012-01-03 12:12:12')), slice(1, 1)), slice('A', 'B')]
tm.assert_frame_equal(result, expected)
result = df.loc[(idx[Timestamp('2012-01-01 12:12:12'):Timestamp('2012-01-03 12:12:12')], idx[1:1]), slice('A', 'B')]
tm.assert_frame_equal(result, expected)
result = df.loc[(slice(Timestamp('2012-01-01 12:12:12'), Timestamp('2012-01-03 12:12:12')), 1), slice('A', 'B')]
tm.assert_frame_equal(result, expected)
result = df.loc[(slice('2012-01-01 12:12:12', '2012-01-03 12:12:12'), slice(1, 1)), slice('A', 'B')]
tm.assert_frame_equal(result, expected)
result = df.loc[(idx['2012-01-01 12:12:12':'2012-01-03 12:12:12'], 1), idx['A', 'B']]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_slice.py:250 | Complexity: Advanced | Last updated: 2026-06-02*