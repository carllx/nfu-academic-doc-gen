# How To: Cmp Series Period Series Mixed Freq

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cmp series period series mixed freq

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign base = Series(...)

```python
base = Series([Period('2011', freq='Y'), Period('2011-02', freq='M'), Period('2013', freq='Y'), Period('2011-04', freq='M')])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([Period('2012', freq='Y'), Period('2011-01', freq='M'), Period('2013', freq='Y'), Period('2011-05', freq='M')])
```

### Step 3: Assign exp = Series(...)

```python
exp = Series([False, False, True, False])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(base == ser, exp)
```

### Step 5: Assign exp = Series(...)

```python
exp = Series([True, True, False, True])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(base != ser, exp)
```

### Step 7: Assign exp = Series(...)

```python
exp = Series([False, True, False, False])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(base > ser, exp)
```

### Step 9: Assign exp = Series(...)

```python
exp = Series([True, False, False, True])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(base < ser, exp)
```

### Step 11: Assign exp = Series(...)

```python
exp = Series([False, True, True, False])
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(base >= ser, exp)
```

### Step 13: Assign exp = Series(...)

```python
exp = Series([True, False, True, True])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(base <= ser, exp)
```


## Complete Example

```python
# Workflow
base = Series([Period('2011', freq='Y'), Period('2011-02', freq='M'), Period('2013', freq='Y'), Period('2011-04', freq='M')])
ser = Series([Period('2012', freq='Y'), Period('2011-01', freq='M'), Period('2013', freq='Y'), Period('2011-05', freq='M')])
exp = Series([False, False, True, False])
tm.assert_series_equal(base == ser, exp)
exp = Series([True, True, False, True])
tm.assert_series_equal(base != ser, exp)
exp = Series([False, True, False, False])
tm.assert_series_equal(base > ser, exp)
exp = Series([True, False, False, True])
tm.assert_series_equal(base < ser, exp)
exp = Series([False, True, True, False])
tm.assert_series_equal(base >= ser, exp)
exp = Series([True, False, True, True])
tm.assert_series_equal(base <= ser, exp)
```

## Next Steps


---

*Source: test_period.py:443 | Complexity: Advanced | Last updated: 2026-06-02*