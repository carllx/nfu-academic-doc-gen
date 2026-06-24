# How To: Compare Timedelta64 Zerodim

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test compare timedelta64 zerodim

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: box_with_array
```

## Step-by-Step Guide

### Step 1: Assign box = box_with_array

```python
box = box_with_array
```

### Step 2: Assign xbox = value

```python
xbox = box_with_array if box_with_array not in [Index, pd.array] else np.ndarray
```

### Step 3: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range('2h', periods=4)
```

### Step 4: Assign other = np.array(...)

```python
other = np.array(tdi.to_numpy()[0])
```

### Step 5: Assign tdi = tm.box_expected(...)

```python
tdi = tm.box_expected(tdi, box)
```

### Step 6: Assign res = value

```python
res = tdi <= other
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False])
```

### Step 8: Assign expected = tm.box_expected(...)

```python
expected = tm.box_expected(expected, xbox)
```

### Step 9: Call tm.assert_equal()

```python
tm.assert_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: box_with_array

# Workflow
box = box_with_array
xbox = box_with_array if box_with_array not in [Index, pd.array] else np.ndarray
tdi = timedelta_range('2h', periods=4)
other = np.array(tdi.to_numpy()[0])
tdi = tm.box_expected(tdi, box)
res = tdi <= other
expected = np.array([True, False, False, False])
expected = tm.box_expected(expected, xbox)
tm.assert_equal(res, expected)
```

## Next Steps


---

*Source: test_timedelta64.py:68 | Complexity: Advanced | Last updated: 2026-06-02*