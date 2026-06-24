# How To: Period Ops Offset

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period ops offset

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign per = Period(...)

```python
per = Period('2011-04-01', freq='D')
```

**Verification:**
```python
assert result == exp
```

### Step 2: Assign result = value

```python
result = per + offsets.Day()
```

**Verification:**
```python
assert result == exp
```

### Step 3: Assign exp = Period(...)

```python
exp = Period('2011-04-02', freq='D')
```

**Verification:**
```python
assert result == exp
```

### Step 4: Assign result = value

```python
result = per - offsets.Day(2)
```

### Step 5: Assign exp = Period(...)

```python
exp = Period('2011-03-30', freq='D')
```

**Verification:**
```python
assert result == exp
```

### Step 6: Assign msg = 'Input cannot be converted to Period\\(freq=D\\)'

```python
msg = 'Input cannot be converted to Period\\(freq=D\\)'
```

### Step 7: per + offsets.Hour(2)

```python
per + offsets.Hour(2)
```

### Step 8: per - offsets.Hour(2)

```python
per - offsets.Hour(2)
```


## Complete Example

```python
# Workflow
per = Period('2011-04-01', freq='D')
result = per + offsets.Day()
exp = Period('2011-04-02', freq='D')
assert result == exp
result = per - offsets.Day(2)
exp = Period('2011-03-30', freq='D')
assert result == exp
msg = 'Input cannot be converted to Period\\(freq=D\\)'
with pytest.raises(IncompatibleFrequency, match=msg):
    per + offsets.Hour(2)
with pytest.raises(IncompatibleFrequency, match=msg):
    per - offsets.Hour(2)
```

## Next Steps


---

*Source: test_arithmetic.py:372 | Complexity: Advanced | Last updated: 2026-06-02*