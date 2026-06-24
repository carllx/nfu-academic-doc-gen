# How To: Maybe Convert I8 Nat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test maybe convert i8 nat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`

**Setup Required:**
```python
# Fixtures: breaks
```

## Step-by-Step Guide

### Step 1: Assign index = IntervalIndex.from_breaks(...)

```python
index = IntervalIndex.from_breaks(breaks)
```

### Step 2: Assign to_convert = breaks._constructor.as_unit(...)

```python
to_convert = breaks._constructor([pd.NaT] * 3).as_unit('ns')
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([np.nan] * 3, dtype=np.float64)
```

### Step 4: Assign result = index._maybe_convert_i8(...)

```python
result = index._maybe_convert_i8(to_convert)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign to_convert = to_convert.insert(...)

```python
to_convert = to_convert.insert(0, breaks[0])
```

### Step 7: Assign expected = expected.insert(...)

```python
expected = expected.insert(0, float(breaks[0]._value))
```

### Step 8: Assign result = index._maybe_convert_i8(...)

```python
result = index._maybe_convert_i8(to_convert)
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: breaks

# Workflow
index = IntervalIndex.from_breaks(breaks)
to_convert = breaks._constructor([pd.NaT] * 3).as_unit('ns')
expected = Index([np.nan] * 3, dtype=np.float64)
result = index._maybe_convert_i8(to_convert)
tm.assert_index_equal(result, expected)
to_convert = to_convert.insert(0, breaks[0])
expected = expected.insert(0, float(breaks[0]._value))
result = index._maybe_convert_i8(to_convert)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_interval.py:387 | Complexity: Advanced | Last updated: 2026-06-02*