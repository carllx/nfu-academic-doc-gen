# How To: Tz Unique

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz unique

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti1 = date_range(...)

```python
dti1 = date_range('2016-01-01', periods=3)
```

**Verification:**
```python
assert uni1.dtype != uni2.dtype
```

### Step 2: Assign ii1 = IntervalIndex.from_breaks(...)

```python
ii1 = IntervalIndex.from_breaks(dti1)
```

### Step 3: Assign ser1 = Series(...)

```python
ser1 = Series(ii1)
```

### Step 4: Assign uni1 = ser1.unique(...)

```python
uni1 = ser1.unique()
```

### Step 5: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(ser1.array, uni1)
```

### Step 6: Assign dti2 = date_range(...)

```python
dti2 = date_range('2016-01-01', periods=3, tz='US/Eastern')
```

### Step 7: Assign ii2 = IntervalIndex.from_breaks(...)

```python
ii2 = IntervalIndex.from_breaks(dti2)
```

### Step 8: Assign ser2 = Series(...)

```python
ser2 = Series(ii2)
```

### Step 9: Assign uni2 = ser2.unique(...)

```python
uni2 = ser2.unique()
```

### Step 10: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(ser2.array, uni2)
```

**Verification:**
```python
assert uni1.dtype != uni2.dtype
```


## Complete Example

```python
# Workflow
dti1 = date_range('2016-01-01', periods=3)
ii1 = IntervalIndex.from_breaks(dti1)
ser1 = Series(ii1)
uni1 = ser1.unique()
tm.assert_interval_array_equal(ser1.array, uni1)
dti2 = date_range('2016-01-01', periods=3, tz='US/Eastern')
ii2 = IntervalIndex.from_breaks(dti2)
ser2 = Series(ii2)
uni2 = ser2.unique()
tm.assert_interval_array_equal(ser2.array, uni2)
assert uni1.dtype != uni2.dtype
```

## Next Steps


---

*Source: test_unique.py:62 | Complexity: Advanced | Last updated: 2026-06-02*