# How To: Set Index Dst

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set index dst

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign di = date_range(...)

```python
di = date_range('2006-10-29 00:00:00', periods=3, freq='h', tz='US/Pacific')
```

### Step 2: Assign df = DataFrame.reset_index(...)

```python
df = DataFrame(data={'a': [0, 1, 2], 'b': [3, 4, 5]}, index=di).reset_index()
```

### Step 3: Assign res = df.set_index(...)

```python
res = df.set_index('index')
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame(data={'a': [0, 1, 2], 'b': [3, 4, 5]}, index=Index(di, name='index'))
```

### Step 5: Assign exp.index = exp.index._with_freq(...)

```python
exp.index = exp.index._with_freq(None)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 7: Assign res = df.set_index(...)

```python
res = df.set_index(['index', 'a'])
```

### Step 8: Assign exp_index = MultiIndex.from_arrays(...)

```python
exp_index = MultiIndex.from_arrays([di, [0, 1, 2]], names=['index', 'a'])
```

### Step 9: Assign exp = DataFrame(...)

```python
exp = DataFrame({'b': [3, 4, 5]}, index=exp_index)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```


## Complete Example

```python
# Workflow
di = date_range('2006-10-29 00:00:00', periods=3, freq='h', tz='US/Pacific')
df = DataFrame(data={'a': [0, 1, 2], 'b': [3, 4, 5]}, index=di).reset_index()
res = df.set_index('index')
exp = DataFrame(data={'a': [0, 1, 2], 'b': [3, 4, 5]}, index=Index(di, name='index'))
exp.index = exp.index._with_freq(None)
tm.assert_frame_equal(res, exp)
res = df.set_index(['index', 'a'])
exp_index = MultiIndex.from_arrays([di, [0, 1, 2]], names=['index', 'a'])
exp = DataFrame({'b': [3, 4, 5]}, index=exp_index)
tm.assert_frame_equal(res, exp)
```

## Next Steps


---

*Source: test_set_index.py:130 | Complexity: Advanced | Last updated: 2026-06-02*