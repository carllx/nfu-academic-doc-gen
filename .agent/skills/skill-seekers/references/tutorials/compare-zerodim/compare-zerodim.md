# How To: Compare Zerodim

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare zerodim

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

### Step 3: Assign dti = date_range(...)

```python
dti = date_range('20130101', periods=3, tz=tz)
```

### Step 4: Assign other = np.array(...)

```python
other = np.array(dti.to_numpy()[0])
```

### Step 5: Assign dtarr = tm.box_expected(...)

```python
dtarr = tm.box_expected(dti, box)
```

### Step 6: Assign xbox = get_upcast_box(...)

```python
xbox = get_upcast_box(dtarr, other, True)
```

### Step 7: Assign result = value

```python
result = dtarr <= other
```

### Step 8: Assign expected = np.array(...)

```python
expected = np.array([True, False, False])
```

### Step 9: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
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
dti = date_range('20130101', periods=3, tz=tz)
other = np.array(dti.to_numpy()[0])
dtarr = tm.box_expected(dti, box)
xbox = get_upcast_box(dtarr, other, True)
result = dtarr <= other
expected = np.array([True, False, False])
expected = tm.box_expected(expected, xbox)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime64.py:53 | Complexity: Advanced | Last updated: 2026-06-02*