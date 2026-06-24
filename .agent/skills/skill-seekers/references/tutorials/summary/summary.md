# How To: Summary

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test summary

## Prerequisites

**Required Modules:**
- `contextlib`
- `datetime`
- `locale`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx1 = PeriodIndex(...)

```python
idx1 = PeriodIndex([], freq='D')
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign idx2 = PeriodIndex(...)

```python
idx2 = PeriodIndex(['2011-01-01'], freq='D')
```

### Step 3: Assign idx3 = PeriodIndex(...)

```python
idx3 = PeriodIndex(['2011-01-01', '2011-01-02'], freq='D')
```

### Step 4: Assign idx4 = PeriodIndex(...)

```python
idx4 = PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D')
```

### Step 5: Assign idx5 = PeriodIndex(...)

```python
idx5 = PeriodIndex(['2011', '2012', '2013'], freq='Y')
```

### Step 6: Assign idx6 = PeriodIndex(...)

```python
idx6 = PeriodIndex(['2011-01-01 09:00', '2012-02-01 10:00', 'NaT'], freq='h')
```

### Step 7: Assign idx7 = pd.period_range(...)

```python
idx7 = pd.period_range('2013Q1', periods=1, freq='Q')
```

### Step 8: Assign idx8 = pd.period_range(...)

```python
idx8 = pd.period_range('2013Q1', periods=2, freq='Q')
```

### Step 9: Assign idx9 = pd.period_range(...)

```python
idx9 = pd.period_range('2013Q1', periods=3, freq='Q')
```

### Step 10: Assign exp1 = 'PeriodIndex: 0 entries\nFreq: D'

```python
exp1 = 'PeriodIndex: 0 entries\nFreq: D'
```

### Step 11: Assign exp2 = 'PeriodIndex: 1 entries, 2011-01-01 to 2011-01-01\nFreq: D'

```python
exp2 = 'PeriodIndex: 1 entries, 2011-01-01 to 2011-01-01\nFreq: D'
```

### Step 12: Assign exp3 = 'PeriodIndex: 2 entries, 2011-01-01 to 2011-01-02\nFreq: D'

```python
exp3 = 'PeriodIndex: 2 entries, 2011-01-01 to 2011-01-02\nFreq: D'
```

### Step 13: Assign exp4 = 'PeriodIndex: 3 entries, 2011-01-01 to 2011-01-03\nFreq: D'

```python
exp4 = 'PeriodIndex: 3 entries, 2011-01-01 to 2011-01-03\nFreq: D'
```

### Step 14: Assign exp5 = 'PeriodIndex: 3 entries, 2011 to 2013\nFreq: Y-DEC'

```python
exp5 = 'PeriodIndex: 3 entries, 2011 to 2013\nFreq: Y-DEC'
```

### Step 15: Assign exp6 = 'PeriodIndex: 3 entries, 2011-01-01 09:00 to NaT\nFreq: h'

```python
exp6 = 'PeriodIndex: 3 entries, 2011-01-01 09:00 to NaT\nFreq: h'
```

### Step 16: Assign exp7 = 'PeriodIndex: 1 entries, 2013Q1 to 2013Q1\nFreq: Q-DEC'

```python
exp7 = 'PeriodIndex: 1 entries, 2013Q1 to 2013Q1\nFreq: Q-DEC'
```

### Step 17: Assign exp8 = 'PeriodIndex: 2 entries, 2013Q1 to 2013Q2\nFreq: Q-DEC'

```python
exp8 = 'PeriodIndex: 2 entries, 2013Q1 to 2013Q2\nFreq: Q-DEC'
```

### Step 18: Assign exp9 = 'PeriodIndex: 3 entries, 2013Q1 to 2013Q3\nFreq: Q-DEC'

```python
exp9 = 'PeriodIndex: 3 entries, 2013Q1 to 2013Q3\nFreq: Q-DEC'
```

### Step 19: Assign result = idx._summary(...)

```python
result = idx._summary()
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
idx1 = PeriodIndex([], freq='D')
idx2 = PeriodIndex(['2011-01-01'], freq='D')
idx3 = PeriodIndex(['2011-01-01', '2011-01-02'], freq='D')
idx4 = PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03'], freq='D')
idx5 = PeriodIndex(['2011', '2012', '2013'], freq='Y')
idx6 = PeriodIndex(['2011-01-01 09:00', '2012-02-01 10:00', 'NaT'], freq='h')
idx7 = pd.period_range('2013Q1', periods=1, freq='Q')
idx8 = pd.period_range('2013Q1', periods=2, freq='Q')
idx9 = pd.period_range('2013Q1', periods=3, freq='Q')
exp1 = 'PeriodIndex: 0 entries\nFreq: D'
exp2 = 'PeriodIndex: 1 entries, 2011-01-01 to 2011-01-01\nFreq: D'
exp3 = 'PeriodIndex: 2 entries, 2011-01-01 to 2011-01-02\nFreq: D'
exp4 = 'PeriodIndex: 3 entries, 2011-01-01 to 2011-01-03\nFreq: D'
exp5 = 'PeriodIndex: 3 entries, 2011 to 2013\nFreq: Y-DEC'
exp6 = 'PeriodIndex: 3 entries, 2011-01-01 09:00 to NaT\nFreq: h'
exp7 = 'PeriodIndex: 1 entries, 2013Q1 to 2013Q1\nFreq: Q-DEC'
exp8 = 'PeriodIndex: 2 entries, 2013Q1 to 2013Q2\nFreq: Q-DEC'
exp9 = 'PeriodIndex: 3 entries, 2013Q1 to 2013Q3\nFreq: Q-DEC'
for idx, expected in zip([idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9], [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9]):
    result = idx._summary()
    assert result == expected
```

## Next Steps


---

*Source: test_formats.py:172 | Complexity: Advanced | Last updated: 2026-06-02*