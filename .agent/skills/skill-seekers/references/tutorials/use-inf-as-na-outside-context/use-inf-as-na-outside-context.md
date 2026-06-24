# How To: Use Inf As Na Outside Context

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test use inf as na outside context

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: values, expected
```

## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(values)
```

### Step 2: Assign msg = 'use_inf_as_na option is deprecated'

```python
msg = 'use_inf_as_na option is deprecated'
```

### Step 3: Assign result = isna(...)

```python
result = isna(cat)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = isna(...)

```python
result = isna(Series(cat))
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(expected)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = isna(...)

```python
result = isna(DataFrame(cat))
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame(expected)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: values, expected

# Workflow
cat = Categorical(values)
msg = 'use_inf_as_na option is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    with pd.option_context('mode.use_inf_as_na', True):
        result = isna(cat)
        tm.assert_numpy_array_equal(result, expected)
        result = isna(Series(cat))
        expected = Series(expected)
        tm.assert_series_equal(result, expected)
        result = isna(DataFrame(cat))
        expected = DataFrame(expected)
        tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_missing.py:164 | Complexity: Advanced | Last updated: 2026-06-02*