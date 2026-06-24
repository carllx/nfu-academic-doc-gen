# How To: Concat Empty Series Timelike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat empty series timelike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz, values
```

## Step-by-Step Guide

### Step 1: Assign first = Series.dt.tz_localize(...)

```python
first = Series([], dtype='M8[ns]').dt.tz_localize(tz)
```

### Step 2: Assign dtype = value

```python
dtype = None if values else np.float64
```

### Step 3: Assign second = Series(...)

```python
second = Series(values, dtype=dtype)
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: Series([pd.NaT] * len(values), dtype='M8[ns]').dt.tz_localize(tz), 1: values})
```

### Step 5: Assign result = concat(...)

```python
result = concat([first, second], axis=1)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz, values

# Workflow
first = Series([], dtype='M8[ns]').dt.tz_localize(tz)
dtype = None if values else np.float64
second = Series(values, dtype=dtype)
expected = DataFrame({0: Series([pd.NaT] * len(values), dtype='M8[ns]').dt.tz_localize(tz), 1: values})
result = concat([first, second], axis=1)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_empty.py:87 | Complexity: Intermediate | Last updated: 2026-06-02*