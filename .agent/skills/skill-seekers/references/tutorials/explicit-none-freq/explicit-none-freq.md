# How To: Explicit None Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test explicit none freq

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

### Step 1: Assign tdi = timedelta_range(...)

```python
tdi = timedelta_range(1, periods=5)
```

**Verification:**
```python
assert tdi.freq is not None
```

### Step 2: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex(tdi, freq=None)
```

**Verification:**
```python
assert result.freq is None
```

### Step 3: Assign result = TimedeltaIndex(...)

```python
result = TimedeltaIndex(tdi._data, freq=None)
```

**Verification:**
```python
assert result.freq is None
```

### Step 4: Assign msg = 'TimedeltaArray.__init__ is deprecated'

```python
msg = 'TimedeltaArray.__init__ is deprecated'
```

**Verification:**
```python
assert tda.freq is None
```

### Step 5: Assign tda = TimedeltaArray(...)

```python
tda = TimedeltaArray(tdi, freq=None)
```


## Complete Example

```python
# Workflow
tdi = timedelta_range(1, periods=5)
assert tdi.freq is not None
result = TimedeltaIndex(tdi, freq=None)
assert result.freq is None
result = TimedeltaIndex(tdi._data, freq=None)
assert result.freq is None
msg = 'TimedeltaArray.__init__ is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    tda = TimedeltaArray(tdi, freq=None)
assert tda.freq is None
```

## Next Steps


---

*Source: test_constructors.py:265 | Complexity: Intermediate | Last updated: 2026-06-02*