# How To: Float64 Ns Rounded

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float64 ns rounded

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.timedeltas`


## Step-by-Step Guide

### Step 1: Assign tdi = TimedeltaIndex(...)

```python
tdi = TimedeltaIndex([2.3, 9.7])
```

### Step 2: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex([2, 9])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(tdi, expected)
```

### Step 4: Assign tdi = TimedeltaIndex(...)

```python
tdi = TimedeltaIndex([2.0, 9.0])
```

### Step 5: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex([2, 9])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(tdi, expected)
```

### Step 7: Assign tdi = TimedeltaIndex(...)

```python
tdi = TimedeltaIndex([2.0, np.nan])
```

### Step 8: Assign expected = TimedeltaIndex(...)

```python
expected = TimedeltaIndex([Timedelta(nanoseconds=2), pd.NaT])
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(tdi, expected)
```


## Complete Example

```python
# Workflow
tdi = TimedeltaIndex([2.3, 9.7])
expected = TimedeltaIndex([2, 9])
tm.assert_index_equal(tdi, expected)
tdi = TimedeltaIndex([2.0, 9.0])
expected = TimedeltaIndex([2, 9])
tm.assert_index_equal(tdi, expected)
tdi = TimedeltaIndex([2.0, np.nan])
expected = TimedeltaIndex([Timedelta(nanoseconds=2), pd.NaT])
tm.assert_index_equal(tdi, expected)
```

## Next Steps


---

*Source: test_constructors.py:109 | Complexity: Advanced | Last updated: 2026-06-02*