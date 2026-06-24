# How To: Transform Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test transform frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`

**Setup Required:**
```python
# Fixtures: on
```

## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range(datetime(2005, 1, 1), datetime(2005, 1, 10), freq='D')
```

### Step 2: Assign index.name = 'date'

```python
index.name = 'date'
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).random((10, 2)), columns=list('AB'), index=index)
```

### Step 4: Assign expected = df.groupby.transform(...)

```python
expected = df.groupby(pd.Grouper(freq='20min')).transform('mean')
```

### Step 5: Assign r = df.resample(...)

```python
r = df.resample('20min', on=on)
```

### Step 6: Assign result = r.transform(...)

```python
result = r.transform('mean')
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign expected = expected.reset_index(...)

```python
expected = expected.reset_index(drop=True)
```

### Step 9: Assign df = df.reset_index(...)

```python
df = df.reset_index()
```


## Complete Example

```python
# Setup
# Fixtures: on

# Workflow
index = date_range(datetime(2005, 1, 1), datetime(2005, 1, 10), freq='D')
index.name = 'date'
df = DataFrame(np.random.default_rng(2).random((10, 2)), columns=list('AB'), index=index)
expected = df.groupby(pd.Grouper(freq='20min')).transform('mean')
if on == 'date':
    expected = expected.reset_index(drop=True)
    df = df.reset_index()
r = df.resample('20min', on=on)
result = r.transform('mean')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_resample_api.py:284 | Complexity: Advanced | Last updated: 2026-06-02*