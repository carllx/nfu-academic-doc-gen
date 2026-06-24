# How To: Transform Axis Ts

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform axis ts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: tsframe
```

## Step-by-Step Guide

### Step 1: Assign base = value

```python
base = tsframe.iloc[0:5]
```

### Step 2: Assign r = len(...)

```python
r = len(base.index)
```

### Step 3: Assign c = len(...)

```python
c = len(base.columns)
```

### Step 4: Assign tso = DataFrame(...)

```python
tso = DataFrame(np.random.default_rng(2).standard_normal((r, c)), index=base.index, columns=base.columns, dtype='float64')
```

### Step 5: Assign ts = tso

```python
ts = tso
```

### Step 6: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.weekday(), group_keys=False)
```

### Step 7: Assign result = value

```python
result = ts - grouped.transform('mean')
```

### Step 8: Assign expected = grouped.apply(...)

```python
expected = grouped.apply(lambda x: x - x.mean(axis=0))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign ts = value

```python
ts = ts.T
```

### Step 11: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 12: Assign result = value

```python
result = ts - grouped.transform('mean')
```

### Step 13: Assign expected = grouped.apply(...)

```python
expected = grouped.apply(lambda x: (x.T - x.mean(1)).T)
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign ts = value

```python
ts = tso.iloc[[1, 0] + list(range(2, len(base)))]
```

### Step 16: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.weekday(), group_keys=False)
```

### Step 17: Assign result = value

```python
result = ts - grouped.transform('mean')
```

### Step 18: Assign expected = grouped.apply(...)

```python
expected = grouped.apply(lambda x: x - x.mean(axis=0))
```

### Step 19: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 20: Assign ts = value

```python
ts = ts.T
```

### Step 21: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 22: Assign result = value

```python
result = ts - grouped.transform('mean')
```

### Step 23: Assign expected = grouped.apply(...)

```python
expected = grouped.apply(lambda x: (x.T - x.mean(1)).T)
```

### Step 24: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 25: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.weekday(), axis=1, group_keys=False)
```

### Step 26: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.weekday(), axis=1, group_keys=False)
```


## Complete Example

```python
# Setup
# Fixtures: tsframe

# Workflow
base = tsframe.iloc[0:5]
r = len(base.index)
c = len(base.columns)
tso = DataFrame(np.random.default_rng(2).standard_normal((r, c)), index=base.index, columns=base.columns, dtype='float64')
ts = tso
grouped = ts.groupby(lambda x: x.weekday(), group_keys=False)
result = ts - grouped.transform('mean')
expected = grouped.apply(lambda x: x - x.mean(axis=0))
tm.assert_frame_equal(result, expected)
ts = ts.T
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grouped = ts.groupby(lambda x: x.weekday(), axis=1, group_keys=False)
result = ts - grouped.transform('mean')
expected = grouped.apply(lambda x: (x.T - x.mean(1)).T)
tm.assert_frame_equal(result, expected)
ts = tso.iloc[[1, 0] + list(range(2, len(base)))]
grouped = ts.groupby(lambda x: x.weekday(), group_keys=False)
result = ts - grouped.transform('mean')
expected = grouped.apply(lambda x: x - x.mean(axis=0))
tm.assert_frame_equal(result, expected)
ts = ts.T
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    grouped = ts.groupby(lambda x: x.weekday(), axis=1, group_keys=False)
result = ts - grouped.transform('mean')
expected = grouped.apply(lambda x: (x.T - x.mean(1)).T)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_transform.py:233 | Complexity: Advanced | Last updated: 2026-06-02*