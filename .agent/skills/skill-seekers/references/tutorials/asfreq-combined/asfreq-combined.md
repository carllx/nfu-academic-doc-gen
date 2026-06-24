# How To: Asfreq Combined

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq combined

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign p = Period(...)

```python
p = Period('2007', freq='h')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign expected = Period(...)

```python
expected = Period('2007', freq='25h')
```

**Verification:**
```python
assert result.ordinal == expected.ordinal
```

### Step 3: Assign p1 = Period(...)

```python
p1 = Period(freq='1D1h', year=2007)
```

**Verification:**
```python
assert result.freq == expected.freq
```

### Step 4: Assign p2 = Period(...)

```python
p2 = Period(freq='1h1D', year=2007)
```

**Verification:**
```python
assert result1 == expected
```

### Step 5: Assign result1 = p1.asfreq(...)

```python
result1 = p1.asfreq('h')
```

**Verification:**
```python
assert result1.ordinal == expected.ordinal
```

### Step 6: Assign result2 = p2.asfreq(...)

```python
result2 = p2.asfreq('h')
```

**Verification:**
```python
assert result1.freq == expected.freq
```

### Step 7: Assign expected = Period(...)

```python
expected = Period('2007-01-02', freq='h')
```

**Verification:**
```python
assert result2 == expected
```

### Step 8: Assign result1 = p1.asfreq(...)

```python
result1 = p1.asfreq('h', how='S')
```

**Verification:**
```python
assert result2.ordinal == expected.ordinal
```

### Step 9: Assign result2 = p2.asfreq(...)

```python
result2 = p2.asfreq('h', how='S')
```

**Verification:**
```python
assert result2.freq == expected.freq
```

### Step 10: Assign expected = Period(...)

```python
expected = Period('2007-01-01', freq='h')
```

**Verification:**
```python
assert result1 == expected
```

### Step 11: Assign result = p.asfreq(...)

```python
result = p.asfreq(freq, how=how)
```

**Verification:**
```python
assert result1.ordinal == expected.ordinal
```


## Complete Example

```python
# Workflow
p = Period('2007', freq='h')
expected = Period('2007', freq='25h')
for freq, how in zip(['1D1h', '1h1D'], ['E', 'S']):
    result = p.asfreq(freq, how=how)
    assert result == expected
    assert result.ordinal == expected.ordinal
    assert result.freq == expected.freq
p1 = Period(freq='1D1h', year=2007)
p2 = Period(freq='1h1D', year=2007)
result1 = p1.asfreq('h')
result2 = p2.asfreq('h')
expected = Period('2007-01-02', freq='h')
assert result1 == expected
assert result1.ordinal == expected.ordinal
assert result1.freq == expected.freq
assert result2 == expected
assert result2.ordinal == expected.ordinal
assert result2.freq == expected.freq
result1 = p1.asfreq('h', how='S')
result2 = p2.asfreq('h', how='S')
expected = Period('2007-01-01', freq='h')
assert result1 == expected
assert result1.ordinal == expected.ordinal
assert result1.freq == expected.freq
assert result2 == expected
assert result2.ordinal == expected.ordinal
assert result2.freq == expected.freq
```

## Next Steps


---

*Source: test_asfreq.py:780 | Complexity: Advanced | Last updated: 2026-06-02*