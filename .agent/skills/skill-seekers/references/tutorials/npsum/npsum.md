# How To: Npsum

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test npsum

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
tdi = pd.TimedeltaIndex(['3h', '3h', '2h', '5h', '4h'])
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

### Step 3: Assign result = np.sum(...)

```python
result = np.sum(tdi)
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 4: Assign expected = Timedelta(...)

```python
expected = Timedelta(hours=17)
```

**Verification:**
```python
assert result == expected
```

### Step 5: Assign result = np.sum(...)

```python
result = np.sum(arr)
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```


## Complete Example

```python
# Workflow
tdi = pd.TimedeltaIndex(['3h', '3h', '2h', '5h', '4h'])
arr = tdi.array
result = np.sum(tdi)
expected = Timedelta(hours=17)
assert isinstance(result, Timedelta)
assert result == expected
result = np.sum(arr)
assert isinstance(result, Timedelta)
assert result == expected
```

## Next Steps


---

*Source: test_reductions.py:90 | Complexity: Intermediate | Last updated: 2026-06-02*