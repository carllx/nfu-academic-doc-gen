# How To: Resample With Timedelta Yields No Empty Groups

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample with timedelta yields no empty groups

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.timedeltas`

**Setup Required:**
```python
# Fixtures: duplicates
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).normal(size=(10000, 4)), index=timedelta_range(start='0s', periods=10000, freq='3906250ns'))
```

### Step 2: Assign result = unknown.resample.apply(...)

```python
result = df.loc['1s':, :].resample('3s').apply(lambda x: len(x))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[768] * 4] * 12 + [[528] * 4], index=timedelta_range(start='1s', periods=13, freq='3s'))
```

### Step 4: Assign expected.columns = value

```python
expected.columns = df.columns
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign df.columns = value

```python
df.columns = ['A', 'B', 'A', 'C']
```


## Complete Example

```python
# Setup
# Fixtures: duplicates

# Workflow
df = DataFrame(np.random.default_rng(2).normal(size=(10000, 4)), index=timedelta_range(start='0s', periods=10000, freq='3906250ns'))
if duplicates:
    df.columns = ['A', 'B', 'A', 'C']
result = df.loc['1s':, :].resample('3s').apply(lambda x: len(x))
expected = DataFrame([[768] * 4] * 12 + [[528] * 4], index=timedelta_range(start='1s', periods=13, freq='3s'))
expected.columns = df.columns
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timedelta.py:159 | Complexity: Intermediate | Last updated: 2026-06-02*