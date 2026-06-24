# How To: Apply Np Reducer

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test apply np reducer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`

**Setup Required:**
```python
# Fixtures: op, how
```

## Step-by-Step Guide

### Step 1: Assign float_frame = DataFrame(...)

```python
float_frame = DataFrame({'a': [1, 2], 'b': [3, 4]})
```

### Step 2: Assign result = getattr(...)

```python
result = getattr(float_frame, how)(op)
```

### Step 3: Assign kwargs = value

```python
kwargs = {'ddof': 1} if op in ('std', 'var') else {}
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(getattr(np, op)(float_frame, axis=0, **kwargs), index=float_frame.columns)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: op, how

# Workflow
float_frame = DataFrame({'a': [1, 2], 'b': [3, 4]})
result = getattr(float_frame, how)(op)
kwargs = {'ddof': 1} if op in ('std', 'var') else {}
expected = Series(getattr(np, op)(float_frame, axis=0, **kwargs), index=float_frame.columns)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_str.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*