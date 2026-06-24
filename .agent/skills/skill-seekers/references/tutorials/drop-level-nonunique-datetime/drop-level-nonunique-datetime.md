# How To: Drop Level Nonunique Datetime

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop level nonunique datetime

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([2, 3, 4, 4, 5], name='id')
```

**Verification:**
```python
assert df.index.is_unique is False
```

### Step 2: Assign idxdt = pd.to_datetime(...)

```python
idxdt = pd.to_datetime(['2016-03-23 14:00', '2016-03-23 15:00', '2016-03-23 16:00', '2016-03-23 16:00', '2016-03-23 17:00'])
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.arange(10).reshape(5, 2), columns=list('ab'), index=idx)
```

### Step 4: Assign unknown = idxdt

```python
df['tstamp'] = idxdt
```

### Step 5: Assign df = df.set_index(...)

```python
df = df.set_index('tstamp', append=True)
```

### Step 6: Assign ts = Timestamp(...)

```python
ts = Timestamp('201603231600')
```

**Verification:**
```python
assert df.index.is_unique is False
```

### Step 7: Assign result = df.drop(...)

```python
result = df.drop(ts, level='tstamp')
```

### Step 8: Assign expected = value

```python
expected = df.loc[idx != 4]
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = Index([2, 3, 4, 4, 5], name='id')
idxdt = pd.to_datetime(['2016-03-23 14:00', '2016-03-23 15:00', '2016-03-23 16:00', '2016-03-23 16:00', '2016-03-23 17:00'])
df = DataFrame(np.arange(10).reshape(5, 2), columns=list('ab'), index=idx)
df['tstamp'] = idxdt
df = df.set_index('tstamp', append=True)
ts = Timestamp('201603231600')
assert df.index.is_unique is False
result = df.drop(ts, level='tstamp')
expected = df.loc[idx != 4]
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_drop.py:401 | Complexity: Advanced | Last updated: 2026-06-02*