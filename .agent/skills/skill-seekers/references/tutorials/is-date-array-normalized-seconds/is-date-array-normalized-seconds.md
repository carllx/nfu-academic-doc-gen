# How To: Is Date Array Normalized Seconds

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test is date array normalized seconds

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.vectorized`


## Step-by-Step Guide

### Step 1: Assign abbrev = 's'

```python
abbrev = 's'
```

**Verification:**
```python
assert result is True
```

### Step 2: Assign arr = day_arr.astype(...)

```python
arr = day_arr.astype(f'M8[{abbrev}]')
```

**Verification:**
```python
assert result2 is False
```

### Step 3: Assign unit = abbrev_to_npy_unit(...)

```python
unit = abbrev_to_npy_unit(abbrev)
```

### Step 4: Assign result = is_date_array_normalized(...)

```python
result = is_date_array_normalized(arr.view('i8'), None, unit)
```

**Verification:**
```python
assert result is True
```

### Step 5: Assign result2 = is_date_array_normalized(...)

```python
result2 = is_date_array_normalized(arr.view('i8'), None, unit)
```

**Verification:**
```python
assert result2 is False
```


## Complete Example

```python
# Workflow
abbrev = 's'
arr = day_arr.astype(f'M8[{abbrev}]')
unit = abbrev_to_npy_unit(abbrev)
result = is_date_array_normalized(arr.view('i8'), None, unit)
assert result is True
arr[0] += np.timedelta64(1, abbrev)
result2 = is_date_array_normalized(arr.view('i8'), None, unit)
assert result2 is False
```

## Next Steps


---

*Source: test_npy_units.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*