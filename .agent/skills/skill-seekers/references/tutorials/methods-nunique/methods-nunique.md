# How To: Methods Nunique

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test methods nunique

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
# Fixtures: test_frame
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

### Step 3: Assign result = r.B.nunique(...)

```python
result = r.B.nunique()
```

### Step 4: Assign expected = g.B.apply(...)

```python
expected = g.B.apply(lambda x: x.resample('2s').nunique())
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: test_frame

# Workflow
g = test_frame.groupby('A')
r = g.resample('2s')
result = r.B.nunique()
expected = g.B.apply(lambda x: x.resample('2s').nunique())
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_resampler_grouper.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*