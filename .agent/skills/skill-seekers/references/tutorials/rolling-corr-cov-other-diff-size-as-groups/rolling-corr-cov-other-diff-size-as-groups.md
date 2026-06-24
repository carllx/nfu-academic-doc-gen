# How To: Rolling Corr Cov Other Diff Size As Groups

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling corr cov other diff size as groups

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.groupby.groupby`

**Setup Required:**
```python
# Fixtures: f, roll_frame
```

## Step-by-Step Guide

### Step 1: Assign g = roll_frame.groupby(...)

```python
g = roll_frame.groupby('A')
```

### Step 2: Assign r = g.rolling(...)

```python
r = g.rolling(window=4)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(r, f)(roll_frame)
```

### Step 4: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 5: Assign unknown = value

```python
expected['A'] = np.nan
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign expected = g.apply(...)

```python
expected = g.apply(func)
```


## Complete Example

```python
# Setup
# Fixtures: f, roll_frame

# Workflow
g = roll_frame.groupby('A')
r = g.rolling(window=4)
result = getattr(r, f)(roll_frame)

def func(x):
    return getattr(x.rolling(4), f)(roll_frame)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = g.apply(func)
expected['A'] = np.nan
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby.py:175 | Complexity: Intermediate | Last updated: 2026-06-02*