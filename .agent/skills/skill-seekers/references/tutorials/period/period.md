# How To: Period

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `re`
- `shutil`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas.io.formats`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign index = pd.period_range(...)

```python
index = pd.period_range('2013-01', periods=6, freq='M')
```

**Verification:**
```python
assert str(s) == exp
```

### Step 2: Assign s = Series(...)

```python
s = Series(np.arange(6, dtype='int64'), index=index)
```

**Verification:**
```python
assert str(s) == exp
```

### Step 3: Assign exp = '2013-01    0\n2013-02    1\n2013-03    2\n2013-04    3\n2013-05    4\n2013-06    5\nFreq: M, dtype: int64'

```python
exp = '2013-01    0\n2013-02    1\n2013-03    2\n2013-04    3\n2013-05    4\n2013-06    5\nFreq: M, dtype: int64'
```

**Verification:**
```python
assert str(s) == exp
```

### Step 4: Assign s = Series(...)

```python
s = Series(index)
```

### Step 5: Assign exp = '0    2013-01\n1    2013-02\n2    2013-03\n3    2013-04\n4    2013-05\n5    2013-06\ndtype: period[M]'

```python
exp = '0    2013-01\n1    2013-02\n2    2013-03\n3    2013-04\n4    2013-05\n5    2013-06\ndtype: period[M]'
```

**Verification:**
```python
assert str(s) == exp
```

### Step 6: Assign s = Series(...)

```python
s = Series([pd.Period('2011-01', freq='M'), pd.Period('2011-02-01', freq='D'), pd.Period('2011-03-01 09:00', freq='h')])
```

### Step 7: Assign exp = '0             2011-01\n1          2011-02-01\n2    2011-03-01 09:00\ndtype: object'

```python
exp = '0             2011-01\n1          2011-02-01\n2    2011-03-01 09:00\ndtype: object'
```

**Verification:**
```python
assert str(s) == exp
```


## Complete Example

```python
# Workflow
index = pd.period_range('2013-01', periods=6, freq='M')
s = Series(np.arange(6, dtype='int64'), index=index)
exp = '2013-01    0\n2013-02    1\n2013-03    2\n2013-04    3\n2013-05    4\n2013-06    5\nFreq: M, dtype: int64'
assert str(s) == exp
s = Series(index)
exp = '0    2013-01\n1    2013-02\n2    2013-03\n3    2013-04\n4    2013-05\n5    2013-06\ndtype: period[M]'
assert str(s) == exp
s = Series([pd.Period('2011-01', freq='M'), pd.Period('2011-02-01', freq='D'), pd.Period('2011-03-01 09:00', freq='h')])
exp = '0             2011-01\n1          2011-02-01\n2    2011-03-01 09:00\ndtype: object'
assert str(s) == exp
```

## Next Steps


---

*Source: test_format.py:1674 | Complexity: Intermediate | Last updated: 2026-06-02*