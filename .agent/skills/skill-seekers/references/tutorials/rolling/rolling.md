# How To: Rolling

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling

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
g = roll_frame.groupby('A', group_keys=False)
```

### Step 2: Assign r = g.rolling(...)

```python
r = g.rolling(window=4)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(r, f)()
```

### Step 4: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 5: Assign expected = expected.drop(...)

```python
expected = expected.drop('A', axis=1)
```

### Step 6: Assign expected_index = MultiIndex.from_arrays(...)

```python
expected_index = MultiIndex.from_arrays([roll_frame['A'], range(40)])
```

### Step 7: Assign expected.index = expected_index

```python
expected.index = expected_index
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign expected = g.apply(...)

```python
expected = g.apply(lambda x: getattr(x.rolling(4), f)())
```


## Complete Example

```python
# Setup
# Fixtures: f, roll_frame

# Workflow
g = roll_frame.groupby('A', group_keys=False)
r = g.rolling(window=4)
result = getattr(r, f)()
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = g.apply(lambda x: getattr(x.rolling(4), f)())
expected = expected.drop('A', axis=1)
expected_index = MultiIndex.from_arrays([roll_frame['A'], range(40)])
expected.index = expected_index
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby.py:98 | Complexity: Advanced | Last updated: 2026-06-02*