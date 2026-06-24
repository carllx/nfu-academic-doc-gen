# How To: Apply Differently Indexed

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply differently indexed

## Prerequisites

**Required Modules:**
- `datetime`
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`
- `pandas.util.version`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((20, 10)))
```

### Step 2: Assign result = df.apply(...)

```python
result = df.apply(Series.describe, axis=0)
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({i: v.describe() for i, v in df.items()}, columns=df.columns)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.apply(...)

```python
result = df.apply(Series.describe, axis=1)
```

### Step 6: Assign expected = value

```python
expected = DataFrame({i: v.describe() for i, v in df.T.items()}, columns=df.index).T
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(np.random.default_rng(2).standard_normal((20, 10)))
result = df.apply(Series.describe, axis=0)
expected = DataFrame({i: v.describe() for i, v in df.items()}, columns=df.columns)
tm.assert_frame_equal(result, expected)
result = df.apply(Series.describe, axis=1)
expected = DataFrame({i: v.describe() for i, v in df.T.items()}, columns=df.index).T
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:429 | Complexity: Intermediate | Last updated: 2026-06-02*