# How To: From Sequence Disallows I8

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from sequence disallows i8

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = period_array(...)

```python
arr = period_array(['2000', '2001'], freq='D')
```

### Step 2: Assign msg = str(...)

```python
msg = str(arr[0].ordinal)
```

### Step 3: Call PeriodArray._from_sequence()

```python
PeriodArray._from_sequence(arr.asi8, dtype=arr.dtype)
```

### Step 4: Call PeriodArray._from_sequence()

```python
PeriodArray._from_sequence(list(arr.asi8), dtype=arr.dtype)
```


## Complete Example

```python
# Workflow
arr = period_array(['2000', '2001'], freq='D')
msg = str(arr[0].ordinal)
with pytest.raises(TypeError, match=msg):
    PeriodArray._from_sequence(arr.asi8, dtype=arr.dtype)
with pytest.raises(TypeError, match=msg):
    PeriodArray._from_sequence(list(arr.asi8), dtype=arr.dtype)
```

## Next Steps


---

*Source: test_constructors.py:102 | Complexity: Intermediate | Last updated: 2026-06-02*