# How To: Dt64Arr Nat Comparison

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt64arr nat comparison

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.conversion`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture, box_with_array
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_naive_fixture

```python
tz = tz_naive_fixture
```

### Step 2: Assign box = box_with_array

```python
box = box_with_array
```

### Step 3: Assign ts = Timestamp(...)

```python
ts = Timestamp('2021-01-01', tz=tz)
```

### Step 4: Assign ser = Series(...)

```python
ser = Series([ts, NaT])
```

### Step 5: Assign obj = tm.box_expected(...)

```python
obj = tm.box_expected(ser, box)
```

### Step 6: Assign xbox = get_upcast_box(...)

```python
xbox = get_upcast_box(obj, ts, True)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([True, False], dtype=np.bool_)
```

### Step 8: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 9: Assign result = value

```python
result = obj == ts
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture, box_with_array

# Workflow
tz = tz_naive_fixture
box = box_with_array
ts = Timestamp('2021-01-01', tz=tz)
ser = Series([ts, NaT])
obj = tm.box_expected(ser, box)
xbox = get_upcast_box(obj, ts, True)
expected = Series([True, False], dtype=np.bool_)
expected = tm.box_expected(expected, xbox)
result = obj == ts
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime64.py:142 | Complexity: Advanced | Last updated: 2026-06-02*