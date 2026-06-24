# How To: Return Type Doesnt Depend On Monotonicity Higher Reso

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test return type doesnt depend on monotonicity higher reso

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range(start='2015-5-13 23:59:00', freq='min', periods=3)
```

**Verification:**
```python
assert result == 1
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(range(3), index=dti)
```

**Verification:**
```python
assert result == 1
```

### Step 3: Assign ser2 = Series(...)

```python
ser2 = Series(range(3), index=[dti[1], dti[0], dti[2]])
```

**Verification:**
```python
assert result2 == 0
```

### Step 4: Assign key = '2015-5-14 00:00:00'

```python
key = '2015-5-14 00:00:00'
```

### Step 5: Assign result = value

```python
result = ser.loc[key]
```

**Verification:**
```python
assert result == 1
```

### Step 6: Assign result = value

```python
result = ser.iloc[::-1].loc[key]
```

**Verification:**
```python
assert result == 1
```

### Step 7: Assign result2 = value

```python
result2 = ser2.loc[key]
```

**Verification:**
```python
assert result2 == 0
```


## Complete Example

```python
# Workflow
dti = date_range(start='2015-5-13 23:59:00', freq='min', periods=3)
ser = Series(range(3), index=dti)
ser2 = Series(range(3), index=[dti[1], dti[0], dti[2]])
key = '2015-5-14 00:00:00'
result = ser.loc[key]
assert result == 1
result = ser.iloc[::-1].loc[key]
assert result == 1
result2 = ser2.loc[key]
assert result2 == 0
```

## Next Steps


---

*Source: test_partial_slicing.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*