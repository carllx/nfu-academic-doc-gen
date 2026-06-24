# How To: Repr Round Days Non Nano

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr round days non nano

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign tdi = TimedeltaIndex.as_unit(...)

```python
tdi = TimedeltaIndex(['1 days'], freq='D').as_unit('s')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign result = repr(...)

```python
result = repr(tdi)
```

**Verification:**
```python
assert result2 == expected2
```

### Step 3: Assign expected = "TimedeltaIndex(['1 days'], dtype='timedelta64[s]', freq='D')"

```python
expected = "TimedeltaIndex(['1 days'], dtype='timedelta64[s]', freq='D')"
```

**Verification:**
```python
assert result == expected
```

### Step 4: Assign result2 = repr(...)

```python
result2 = repr(Series(tdi))
```

### Step 5: Assign expected2 = '0   1 days\ndtype: timedelta64[s]'

```python
expected2 = '0   1 days\ndtype: timedelta64[s]'
```

**Verification:**
```python
assert result2 == expected2
```


## Complete Example

```python
# Workflow
tdi = TimedeltaIndex(['1 days'], freq='D').as_unit('s')
result = repr(tdi)
expected = "TimedeltaIndex(['1 days'], dtype='timedelta64[s]', freq='D')"
assert result == expected
result2 = repr(Series(tdi))
expected2 = '0   1 days\ndtype: timedelta64[s]'
assert result2 == expected2
```

## Next Steps


---

*Source: test_formats.py:11 | Complexity: Intermediate | Last updated: 2026-06-02*