# How To: Representation

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test representation

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `datetime`
- `locale`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method
```

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

### Step 10: Assign idx10 = PeriodIndex(...)

```python
idx10 = PeriodIndex(['2011-01-01', '2011-02-01'], freq='3D')
```

### Step 11: Assign exp1 = "PeriodIndex([], dtype='period[D]')"

```python
exp1 = "PeriodIndex([], dtype='period[D]')"
```

### Step 12: Assign exp2 = "PeriodIndex(['2011-01-01'], dtype='period[D]')"

```python
exp2 = "PeriodIndex(['2011-01-01'], dtype='period[D]')"
```

### Step 13: Assign exp3 = "PeriodIndex(['2011-01-01', '2011-01-02'], dtype='period[D]')"

```python
exp3 = "PeriodIndex(['2011-01-01', '2011-01-02'], dtype='period[D]')"
```

### Step 14: Assign exp4 = "PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='period[D]')"

```python
exp4 = "PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='period[D]')"
```

### Step 15: Assign exp5 = "PeriodIndex(['2011', '2012', '2013'], dtype='period[Y-DEC]')"

```python
exp5 = "PeriodIndex(['2011', '2012', '2013'], dtype='period[Y-DEC]')"
```

### Step 16: Assign exp6 = "PeriodIndex(['2011-01-01 09:00', '2012-02-01 10:00', 'NaT'], dtype='period[h]')"

```python
exp6 = "PeriodIndex(['2011-01-01 09:00', '2012-02-01 10:00', 'NaT'], dtype='period[h]')"
```

### Step 17: Assign exp7 = "PeriodIndex(['2013Q1'], dtype='period[Q-DEC]')"

```python
exp7 = "PeriodIndex(['2013Q1'], dtype='period[Q-DEC]')"
```

### Step 18: Assign exp8 = "PeriodIndex(['2013Q1', '2013Q2'], dtype='period[Q-DEC]')"

```python
exp8 = "PeriodIndex(['2013Q1', '2013Q2'], dtype='period[Q-DEC]')"
```

### Step 19: Assign exp9 = "PeriodIndex(['2013Q1', '2013Q2', '2013Q3'], dtype='period[Q-DEC]')"

```python
exp9 = "PeriodIndex(['2013Q1', '2013Q2', '2013Q3'], dtype='period[Q-DEC]')"
```

### Step 20: Assign exp10 = "PeriodIndex(['2011-01-01', '2011-02-01'], dtype='period[3D]')"

```python
exp10 = "PeriodIndex(['2011-01-01', '2011-02-01'], dtype='period[3D]')"
```

### Step 21: Assign result = getattr(...)

```python
result = getattr(idx, method)()
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: method

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
idx10 = PeriodIndex(['2011-01-01', '2011-02-01'], freq='3D')
exp1 = "PeriodIndex([], dtype='period[D]')"
exp2 = "PeriodIndex(['2011-01-01'], dtype='period[D]')"
exp3 = "PeriodIndex(['2011-01-01', '2011-01-02'], dtype='period[D]')"
exp4 = "PeriodIndex(['2011-01-01', '2011-01-02', '2011-01-03'], dtype='period[D]')"
exp5 = "PeriodIndex(['2011', '2012', '2013'], dtype='period[Y-DEC]')"
exp6 = "PeriodIndex(['2011-01-01 09:00', '2012-02-01 10:00', 'NaT'], dtype='period[h]')"
exp7 = "PeriodIndex(['2013Q1'], dtype='period[Q-DEC]')"
exp8 = "PeriodIndex(['2013Q1', '2013Q2'], dtype='period[Q-DEC]')"
exp9 = "PeriodIndex(['2013Q1', '2013Q2', '2013Q3'], dtype='period[Q-DEC]')"
exp10 = "PeriodIndex(['2011-01-01', '2011-02-01'], dtype='period[3D]')"
for idx, expected in zip([idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9, idx10], [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10]):
    result = getattr(idx, method)()
    assert result == expected
```

## Next Steps


---

*Source: test_formats.py:69 | Complexity: Advanced | Last updated: 2026-06-02*