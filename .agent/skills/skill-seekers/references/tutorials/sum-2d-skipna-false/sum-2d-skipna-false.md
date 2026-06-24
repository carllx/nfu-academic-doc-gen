# How To: Sum 2D Skipna False

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sum 2d skipna false

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.astype.view.astype.reshape(...)

```python
arr = np.arange(8).astype(np.int64).view('m8[s]').astype('m8[ns]').reshape(4, 2)
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 2: Assign unknown = 'Nat'

```python
arr[-1, -1] = 'Nat'
```

### Step 3: Assign tda = TimedeltaArray._from_sequence(...)

```python
tda = TimedeltaArray._from_sequence(arr)
```

### Step 4: Assign result = tda.sum(...)

```python
result = tda.sum(skipna=False)
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 5: Assign result = tda.sum(...)

```python
result = tda.sum(axis=0, skipna=False)
```

### Step 6: Assign expected = value

```python
expected = pd.TimedeltaIndex([Timedelta(seconds=12), pd.NaT])._values
```

### Step 7: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result, expected)
```

### Step 8: Assign result = tda.sum(...)

```python
result = tda.sum(axis=1, skipna=False)
```

### Step 9: Assign expected = value

```python
expected = pd.TimedeltaIndex([Timedelta(seconds=1), Timedelta(seconds=5), Timedelta(seconds=9), pd.NaT])._values
```

### Step 10: Call tm.assert_timedelta_array_equal()

```python
tm.assert_timedelta_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.arange(8).astype(np.int64).view('m8[s]').astype('m8[ns]').reshape(4, 2)
arr[-1, -1] = 'Nat'
tda = TimedeltaArray._from_sequence(arr)
result = tda.sum(skipna=False)
assert result is pd.NaT
result = tda.sum(axis=0, skipna=False)
expected = pd.TimedeltaIndex([Timedelta(seconds=12), pd.NaT])._values
tm.assert_timedelta_array_equal(result, expected)
result = tda.sum(axis=1, skipna=False)
expected = pd.TimedeltaIndex([Timedelta(seconds=1), Timedelta(seconds=5), Timedelta(seconds=9), pd.NaT])._values
tm.assert_timedelta_array_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:104 | Complexity: Advanced | Last updated: 2026-06-02*