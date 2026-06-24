# How To: Grouper Multilevel Freq

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test grouper multilevel freq

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`


## Step-by-Step Guide

### Step 1: Assign d0 = value

```python
d0 = date.today() - timedelta(days=14)
```

### Step 2: Assign dates = date_range(...)

```python
dates = date_range(d0, date.today())
```

### Step 3: Assign date_index = MultiIndex.from_product(...)

```python
date_index = MultiIndex.from_product([dates, dates], names=['foo', 'bar'])
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).integers(0, 100, 225), index=date_index)
```

### Step 5: Assign expected = df.reset_index.groupby.sum(...)

```python
expected = df.reset_index().groupby([Grouper(key='foo', freq='W'), Grouper(key='bar', freq='W')]).sum()
```

### Step 6: Assign expected.columns = Index(...)

```python
expected.columns = Index([0], dtype='int64')
```

### Step 7: Assign result = df.groupby.sum(...)

```python
result = df.groupby([Grouper(level='foo', freq='W'), Grouper(level='bar', freq='W')]).sum()
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df.groupby.sum(...)

```python
result = df.groupby([Grouper(level=0, freq='W'), Grouper(level=1, freq='W')]).sum()
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
d0 = date.today() - timedelta(days=14)
dates = date_range(d0, date.today())
date_index = MultiIndex.from_product([dates, dates], names=['foo', 'bar'])
df = DataFrame(np.random.default_rng(2).integers(0, 100, 225), index=date_index)
expected = df.reset_index().groupby([Grouper(key='foo', freq='W'), Grouper(key='bar', freq='W')]).sum()
expected.columns = Index([0], dtype='int64')
result = df.groupby([Grouper(level='foo', freq='W'), Grouper(level='bar', freq='W')]).sum()
tm.assert_frame_equal(result, expected)
result = df.groupby([Grouper(level=0, freq='W'), Grouper(level=1, freq='W')]).sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_grouping.py:195 | Complexity: Advanced | Last updated: 2026-06-02*