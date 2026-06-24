# How To: Parr Cmp Period Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test parr cmp period scalar

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

### Step 3: Assign per = Period(...)

```python
per = Period('2011-02', freq=freq)
```

### Step 4: Assign xbox = get_upcast_box(...)

```python
xbox = get_upcast_box(base, per, True)
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([False, True, False, False])
```

### Step 6: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(base == per, exp)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(per == base, exp)
```

### Step 9: Assign exp = np.array(...)

```python
exp = np.array([True, False, True, True])
```

### Step 10: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 11: Call tm.assert_equal()

```python
tm.assert_equal(base != per, exp)
```

### Step 12: Call tm.assert_equal()

```python
tm.assert_equal(per != base, exp)
```

### Step 13: Assign exp = np.array(...)

```python
exp = np.array([False, False, True, True])
```

### Step 14: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 15: Call tm.assert_equal()

```python
tm.assert_equal(base > per, exp)
```

### Step 16: Call tm.assert_equal()

```python
tm.assert_equal(per < base, exp)
```

### Step 17: Assign exp = np.array(...)

```python
exp = np.array([True, False, False, False])
```

### Step 18: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 19: Call tm.assert_equal()

```python
tm.assert_equal(base < per, exp)
```

### Step 20: Call tm.assert_equal()

```python
tm.assert_equal(per > base, exp)
```

### Step 21: Assign exp = np.array(...)

```python
exp = np.array([False, True, True, True])
```

### Step 22: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 23: Call tm.assert_equal()

```python
tm.assert_equal(base >= per, exp)
```

### Step 24: Call tm.assert_equal()

```python
tm.assert_equal(per <= base, exp)
```

### Step 25: Assign exp = np.array(...)

```python
exp = np.array([True, True, False, False])
```

### Step 26: Assign exp = tm.box_expected(...)

```python
exp = tm.box_expected(exp, xbox)
```

### Step 27: Call tm.assert_equal()

```python
tm.assert_equal(base <= per, exp)
```

### Step 28: Call tm.assert_equal()

```python
tm.assert_equal(per >= base, exp)
```


## Complete Example

```python
# Setup
# Fixtures: freq, box_with_array

# Workflow
base = PeriodIndex(['2011-01', '2011-02', '2011-03', '2011-04'], freq=freq)
base = tm.box_expected(base, box_with_array)
per = Period('2011-02', freq=freq)
xbox = get_upcast_box(base, per, True)
exp = np.array([False, True, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base == per, exp)
tm.assert_equal(per == base, exp)
exp = np.array([True, False, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base != per, exp)
tm.assert_equal(per != base, exp)
exp = np.array([False, False, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base > per, exp)
tm.assert_equal(per < base, exp)
exp = np.array([True, False, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base < per, exp)
tm.assert_equal(per > base, exp)
exp = np.array([False, True, True, True])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base >= per, exp)
tm.assert_equal(per <= base, exp)
exp = np.array([True, True, False, False])
exp = tm.box_expected(exp, xbox)
tm.assert_equal(base <= per, exp)
tm.assert_equal(per >= base, exp)
```

## Next Steps


---

*Source: test_period.py:247 | Complexity: Advanced | Last updated: 2026-06-02*