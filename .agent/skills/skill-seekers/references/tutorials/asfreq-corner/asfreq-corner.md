# How To: Asfreq Corner

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq corner

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign val = Period(...)

```python
val = Period(freq='Y', year=2007)
```

**Verification:**
```python
assert result1.ordinal == expected.ordinal
```

### Step 2: Assign result1 = val.asfreq(...)

```python
result1 = val.asfreq('5min')
```

**Verification:**
```python
assert result1.freqstr == '5min'
```

### Step 3: Assign result2 = val.asfreq(...)

```python
result2 = val.asfreq('min')
```

**Verification:**
```python
assert result2.ordinal == expected.ordinal
```

### Step 4: Assign expected = Period(...)

```python
expected = Period('2007-12-31 23:59', freq='min')
```

**Verification:**
```python
assert result2.freqstr == 'min'
```


## Complete Example

```python
# Workflow
val = Period(freq='Y', year=2007)
result1 = val.asfreq('5min')
result2 = val.asfreq('min')
expected = Period('2007-12-31 23:59', freq='min')
assert result1.ordinal == expected.ordinal
assert result1.freqstr == '5min'
assert result2.ordinal == expected.ordinal
assert result2.freqstr == 'min'
```

## Next Steps


---

*Source: test_asfreq.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*