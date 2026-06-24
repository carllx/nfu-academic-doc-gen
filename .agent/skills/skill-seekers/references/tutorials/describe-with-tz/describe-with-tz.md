# How To: Describe With Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test describe with tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

### Step 2: Assign name = str(...)

```python
name = str(tz_naive_fixture)
```

### Step 3: Assign start = Timestamp(...)

```python
start = Timestamp(2018, 1, 1)
```

### Step 4: Assign end = Timestamp(...)

```python
end = Timestamp(2018, 1, 5)
```

### Step 5: Assign s = Series(...)

```python
s = Series(date_range(start, end, tz=tz), name=name)
```

### Step 6: Assign result = s.describe(...)

```python
result = s.describe()
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([5, Timestamp(2018, 1, 3).tz_localize(tz), start.tz_localize(tz), s[1], s[2], s[3], end.tz_localize(tz)], name=name, index=['count', 'mean', 'min', '25%', '50%', '75%', 'max'])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = tz_naive_fixture
name = str(tz_naive_fixture)
start = Timestamp(2018, 1, 1)
end = Timestamp(2018, 1, 5)
s = Series(date_range(start, end, tz=tz), name=name)
result = s.describe()
expected = Series([5, Timestamp(2018, 1, 3).tz_localize(tz), start.tz_localize(tz), s[1], s[2], s[3], end.tz_localize(tz)], name=name, index=['count', 'mean', 'min', '25%', '50%', '75%', 'max'])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:98 | Complexity: Advanced | Last updated: 2026-06-02*