# How To: Methods

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test methods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `IPython.core.completer`

**Setup Required:**
```python
# Fixtures: f, test_frame
```

## Step-by-Step Guide

### Step 1: Assign g = test_frame.groupby(...)

```python
g = test_frame.groupby('A')
```

### Step 2: Assign r = g.resample(...)

```python
r = g.resample('2s')
```

### Step 3: Assign msg = 'DataFrameGroupBy.resample operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
```

### Step 4: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(r, f)()
```

### Step 7: Assign expected = g.apply(...)

```python
expected = g.apply(lambda x: getattr(x.resample('2s'), f)())
```


## Complete Example

```python
# Setup
# Fixtures: f, test_frame

# Workflow
g = test_frame.groupby('A')
r = g.resample('2s')
msg = 'DataFrameGroupBy.resample operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = getattr(r, f)()
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = g.apply(lambda x: getattr(x.resample('2s'), f)())
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_resampler_grouper.py:233 | Complexity: Intermediate | Last updated: 2026-06-02*