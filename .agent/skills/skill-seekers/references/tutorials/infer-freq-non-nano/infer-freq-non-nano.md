# How To: Infer Freq Non Nano

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test infer freq non nano

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.tools.datetimes`
- `pandas.tseries`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.astype.view(...)

```python
arr = np.arange(10).astype(np.int64).view('M8[s]')
```

**Verification:**
```python
assert res == 's'
```

### Step 2: Assign dta = DatetimeArray._simple_new(...)

```python
dta = DatetimeArray._simple_new(arr, dtype=arr.dtype)
```

**Verification:**
```python
assert res2 == 'ms'
```

### Step 3: Assign res = frequencies.infer_freq(...)

```python
res = frequencies.infer_freq(dta)
```

**Verification:**
```python
assert res == 's'
```

### Step 4: Assign arr2 = arr.view(...)

```python
arr2 = arr.view('m8[ms]')
```

### Step 5: Assign tda = TimedeltaArray._simple_new(...)

```python
tda = TimedeltaArray._simple_new(arr2, dtype=arr2.dtype)
```

### Step 6: Assign res2 = frequencies.infer_freq(...)

```python
res2 = frequencies.infer_freq(tda)
```

**Verification:**
```python
assert res2 == 'ms'
```


## Complete Example

```python
# Workflow
arr = np.arange(10).astype(np.int64).view('M8[s]')
dta = DatetimeArray._simple_new(arr, dtype=arr.dtype)
res = frequencies.infer_freq(dta)
assert res == 's'
arr2 = arr.view('m8[ms]')
tda = TimedeltaArray._simple_new(arr2, dtype=arr2.dtype)
res2 = frequencies.infer_freq(tda)
assert res2 == 'ms'
```

## Next Steps


---

*Source: test_inference.py:539 | Complexity: Intermediate | Last updated: 2026-06-02*