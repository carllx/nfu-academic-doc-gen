# How To: Median

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test median

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

### Step 1: Assign tdi = pd.TimedeltaIndex(...)

```python
tdi = pd.TimedeltaIndex(['0h', '3h', 'NaT', '5h06m', '0h', '2h'])
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 2: Assign arr = value

```python
arr = tdi.array
```

**Verification:**
```python
assert result == expected
```

### Step 3: Assign result = arr.median(...)

```python
result = arr.median(skipna=True)
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 4: Assign expected = Timedelta(...)

```python
expected = Timedelta(hours=2)
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = tdi.median(...)

```python
result = tdi.median(skipna=True)
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 6: Assign result = arr.median(...)

```python
result = arr.median(skipna=False)
```

**Verification:**
```python
assert result is pd.NaT
```

### Step 7: Assign result = tdi.median(...)

```python
result = tdi.median(skipna=False)
```

**Verification:**
```python
assert result is pd.NaT
```


## Complete Example

```python
# Workflow
tdi = pd.TimedeltaIndex(['0h', '3h', 'NaT', '5h06m', '0h', '2h'])
arr = tdi.array
result = arr.median(skipna=True)
expected = Timedelta(hours=2)
assert isinstance(result, Timedelta)
assert result == expected
result = tdi.median(skipna=True)
assert isinstance(result, Timedelta)
assert result == expected
result = arr.median(skipna=False)
assert result is pd.NaT
result = tdi.median(skipna=False)
assert result is pd.NaT
```

## Next Steps


---

*Source: test_reductions.py:167 | Complexity: Intermediate | Last updated: 2026-06-02*