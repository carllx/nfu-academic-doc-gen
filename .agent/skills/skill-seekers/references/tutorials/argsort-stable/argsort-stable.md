# How To: Argsort Stable

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test argsort stable

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(np.random.default_rng(2).integers(0, 100, size=10000))
```

### Step 2: Assign mindexer = ser.argsort(...)

```python
mindexer = ser.argsort(kind='mergesort')
```

### Step 3: Assign qindexer = ser.argsort(...)

```python
qindexer = ser.argsort()
```

### Step 4: Assign mexpected = np.argsort(...)

```python
mexpected = np.argsort(ser.values, kind='mergesort')
```

### Step 5: Assign qexpected = np.argsort(...)

```python
qexpected = np.argsort(ser.values, kind='quicksort')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(mindexer.astype(np.intp), Series(mexpected))
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(qindexer.astype(np.intp), Series(qexpected))
```

### Step 8: Assign msg = "ndarray Expected type <class 'numpy\\.ndarray'>, found <class 'pandas\\.core\\.series\\.Series'> instead"

```python
msg = "ndarray Expected type <class 'numpy\\.ndarray'>, found <class 'pandas\\.core\\.series\\.Series'> instead"
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(qindexer, mindexer)
```


## Complete Example

```python
# Workflow
ser = Series(np.random.default_rng(2).integers(0, 100, size=10000))
mindexer = ser.argsort(kind='mergesort')
qindexer = ser.argsort()
mexpected = np.argsort(ser.values, kind='mergesort')
qexpected = np.argsort(ser.values, kind='quicksort')
tm.assert_series_equal(mindexer.astype(np.intp), Series(mexpected))
tm.assert_series_equal(qindexer.astype(np.intp), Series(qexpected))
msg = "ndarray Expected type <class 'numpy\\.ndarray'>, found <class 'pandas\\.core\\.series\\.Series'> instead"
with pytest.raises(AssertionError, match=msg):
    tm.assert_numpy_array_equal(qindexer, mindexer)
```

## Next Steps


---

*Source: test_argsort.py:65 | Complexity: Advanced | Last updated: 2026-06-02*