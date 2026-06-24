# How To: Representation To Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test representation to series

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

### Step 10: Assign exp1 = 'Series([], dtype: period[D])'

```python
exp1 = 'Series([], dtype: period[D])'
```

### Step 11: Assign exp2 = '0    2011-01-01\ndtype: period[D]'

```python
exp2 = '0    2011-01-01\ndtype: period[D]'
```

### Step 12: Assign exp3 = '0    2011-01-01\n1    2011-01-02\ndtype: period[D]'

```python
exp3 = '0    2011-01-01\n1    2011-01-02\ndtype: period[D]'
```

### Step 13: Assign exp4 = '0    2011-01-01\n1    2011-01-02\n2    2011-01-03\ndtype: period[D]'

```python
exp4 = '0    2011-01-01\n1    2011-01-02\n2    2011-01-03\ndtype: period[D]'
```

### Step 14: Assign exp5 = '0    2011\n1    2012\n2    2013\ndtype: period[Y-DEC]'

```python
exp5 = '0    2011\n1    2012\n2    2013\ndtype: period[Y-DEC]'
```

### Step 15: Assign exp6 = '0    2011-01-01 09:00\n1    2012-02-01 10:00\n2                 NaT\ndtype: period[h]'

```python
exp6 = '0    2011-01-01 09:00\n1    2012-02-01 10:00\n2                 NaT\ndtype: period[h]'
```

### Step 16: Assign exp7 = '0    2013Q1\ndtype: period[Q-DEC]'

```python
exp7 = '0    2013Q1\ndtype: period[Q-DEC]'
```

### Step 17: Assign exp8 = '0    2013Q1\n1    2013Q2\ndtype: period[Q-DEC]'

```python
exp8 = '0    2013Q1\n1    2013Q2\ndtype: period[Q-DEC]'
```

### Step 18: Assign exp9 = '0    2013Q1\n1    2013Q2\n2    2013Q3\ndtype: period[Q-DEC]'

```python
exp9 = '0    2013Q1\n1    2013Q2\n2    2013Q3\ndtype: period[Q-DEC]'
```

### Step 19: Assign result = repr(...)

```python
result = repr(Series(idx))
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
exp1 = 'Series([], dtype: period[D])'
exp2 = '0    2011-01-01\ndtype: period[D]'
exp3 = '0    2011-01-01\n1    2011-01-02\ndtype: period[D]'
exp4 = '0    2011-01-01\n1    2011-01-02\n2    2011-01-03\ndtype: period[D]'
exp5 = '0    2011\n1    2012\n2    2013\ndtype: period[Y-DEC]'
exp6 = '0    2011-01-01 09:00\n1    2012-02-01 10:00\n2                 NaT\ndtype: period[h]'
exp7 = '0    2013Q1\ndtype: period[Q-DEC]'
exp8 = '0    2013Q1\n1    2013Q2\ndtype: period[Q-DEC]'
exp9 = '0    2013Q1\n1    2013Q2\n2    2013Q3\ndtype: period[Q-DEC]'
for idx, expected in zip([idx1, idx2, idx3, idx4, idx5, idx6, idx7, idx8, idx9], [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9]):
    result = repr(Series(idx))
    assert result == expected
```

## Next Steps


---

*Source: test_formats.py:116 | Complexity: Advanced | Last updated: 2026-06-02*