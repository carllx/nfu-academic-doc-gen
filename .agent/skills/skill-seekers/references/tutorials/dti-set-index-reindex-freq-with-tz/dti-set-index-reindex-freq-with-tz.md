# How To: Dti Set Index Reindex Freq With Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti set index reindex freq with tz

## Prerequisites

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range(datetime(2015, 10, 1), datetime(2015, 10, 1, 23), freq='h', tz='US/Eastern')
```

**Verification:**
```python
assert result.index.freq == index.freq
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((24, 1)), columns=['a'], index=index)
```

### Step 3: Assign new_index = date_range(...)

```python
new_index = date_range(datetime(2015, 10, 2), datetime(2015, 10, 2, 23), freq='h', tz='US/Eastern')
```

### Step 4: Assign result = df.set_index(...)

```python
result = df.set_index(new_index)
```

**Verification:**
```python
assert result.index.freq == index.freq
```


## Complete Example

```python
# Workflow
index = date_range(datetime(2015, 10, 1), datetime(2015, 10, 1, 23), freq='h', tz='US/Eastern')
df = DataFrame(np.random.default_rng(2).standard_normal((24, 1)), columns=['a'], index=index)
new_index = date_range(datetime(2015, 10, 2), datetime(2015, 10, 2, 23), freq='h', tz='US/Eastern')
result = df.set_index(new_index)
assert result.index.freq == index.freq
```

## Next Steps


---

*Source: test_reindex.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*