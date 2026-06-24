# How To: Setitem Multiindex3

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem multiindex3

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([['A', 'B', 'C'], date_range('2015-01-01', '2015-04-01', freq='MS')])
```

### Step 2: Assign cols = MultiIndex.from_product(...)

```python
cols = MultiIndex.from_product([['foo', 'bar'], date_range('2016-01-01', '2016-02-01', freq='MS')])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((12, 4)), index=idx, columns=cols)
```

### Step 4: Assign subidx = MultiIndex.from_arrays(...)

```python
subidx = MultiIndex.from_arrays([['A', 'A'], date_range('2015-01-01', '2015-02-01', freq='MS')])
```

### Step 5: Assign subcols = MultiIndex.from_arrays(...)

```python
subcols = MultiIndex.from_arrays([['foo', 'foo'], date_range('2016-01-01', '2016-02-01', freq='MS')])
```

### Step 6: Assign vals = DataFrame(...)

```python
vals = DataFrame(np.random.default_rng(2).random((2, 2)), index=subidx, columns=subcols)
```

### Step 7: Call self.check()

```python
self.check(target=df, indexers=(subidx, subcols), value=vals, compare_fn=tm.assert_frame_equal)
```

### Step 8: Assign vals = DataFrame(...)

```python
vals = DataFrame(np.random.default_rng(2).random((2, 4)), index=subidx, columns=cols)
```

### Step 9: Call self.check()

```python
self.check(target=df, indexers=(subidx, slice(None, None, None)), value=vals, compare_fn=tm.assert_frame_equal)
```

### Step 10: Assign copy = df.copy(...)

```python
copy = df.copy()
```

### Step 11: Call self.check()

```python
self.check(target=df, indexers=(df.index, df.columns), value=df, compare_fn=tm.assert_frame_equal, expected=copy)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_product([['A', 'B', 'C'], date_range('2015-01-01', '2015-04-01', freq='MS')])
cols = MultiIndex.from_product([['foo', 'bar'], date_range('2016-01-01', '2016-02-01', freq='MS')])
df = DataFrame(np.random.default_rng(2).random((12, 4)), index=idx, columns=cols)
subidx = MultiIndex.from_arrays([['A', 'A'], date_range('2015-01-01', '2015-02-01', freq='MS')])
subcols = MultiIndex.from_arrays([['foo', 'foo'], date_range('2016-01-01', '2016-02-01', freq='MS')])
vals = DataFrame(np.random.default_rng(2).random((2, 2)), index=subidx, columns=subcols)
self.check(target=df, indexers=(subidx, subcols), value=vals, compare_fn=tm.assert_frame_equal)
vals = DataFrame(np.random.default_rng(2).random((2, 4)), index=subidx, columns=cols)
self.check(target=df, indexers=(subidx, slice(None, None, None)), value=vals, compare_fn=tm.assert_frame_equal)
copy = df.copy()
self.check(target=df, indexers=(df.index, df.columns), value=df, compare_fn=tm.assert_frame_equal, expected=copy)
```

## Next Steps


---

*Source: test_setitem.py:80 | Complexity: Advanced | Last updated: 2026-06-02*