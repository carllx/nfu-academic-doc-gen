# How To: Parr Cmp Pi

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test parr cmp pi

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`

**Setup Required:**
```python
# Fixtures: freq, box_with_array
```

## Step-by-Step Guide

### Step 1: Assign base = PeriodIndex(...)

```python
base = PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq=freq)
```

### Step 2: Assign base = tm.box_expected(...)

```python
base = tm.box_expected(base, box_with_array)
```

### Step 3: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-02', '2011-01', '2011-03', '2011-05'], freq=freq)
```

### Step 4: Assign xbox = get_upcast_box(...)

```python
xbox = get_upcast_box(base, idx, True)
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([False, False, True, False])
```

### Step 6: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(base == idx, exp)
```

### Step 8: Assign exp = np.array(...)

```python
exp = np.array([True, True, False, True])
```

### Step 9: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(base != idx, exp)
```

### Step 11: Assign exp = np.array(...)

```python
exp = np.array([False, True, False, False])
```

### Step 12: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 13: Call tm.assert_equal()

```python
tm.assert_equal(base > idx, exp)
```

### Step 14: Assign exp = np.array(...)

```python
exp = np.array([True, False, False, True])
```

### Step 15: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 16: Call tm.assert_equal()

```python
tm.assert_equal(base < idx, exp)
```

### Step 17: Assign exp = np.array(...)

```python
exp = np.array([False, True, True, False])
```

### Step 18: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 19: Call tm.assert_equal()

```python
tm.assert_equal(base >= idx, exp)
```

### Step 20: Assign exp = np.array(...)

```python
exp = np.array([True, False, True, True])
```

### Step 21: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 22: Call tm.assert_equal()

```python
tm.assert_equal(base <= idx, exp)
```


## Complete Example

```python
# Setup
# Fixtures: freq, box_with_array

# Workflow
base = PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq=freq)
base = tm.box_expected(base, box_with_array)
idx = PeriodIndex(['2011-02', '2011-01', '2011-03', '2011-05'], freq=freq)
xbox = get_upcast_box(base, idx, True)
exp = np.array([False, False, True, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base == idx, exp)
exp = np.array([True, True, False, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base != idx, exp)
exp = np.array([False, True, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base > idx, exp)
exp = np.array([True, False, False, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base < idx, exp)
exp = np.array([False, True, True, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base >= idx, exp)
exp = np.array([True, False, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base <= idx, exp)
```

## Next Steps


---

*Source: test_period.py:285 | Complexity: Advanced | Last updated: 2026-06-02*