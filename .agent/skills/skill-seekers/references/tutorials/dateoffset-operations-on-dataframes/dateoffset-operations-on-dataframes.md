# How To: Dateoffset Operations On Dataframes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dateoffset operations on dataframes

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.offsets`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'T': [Timestamp('2019-04-30')], 'D': [DateOffset(months=1)]})
```

**Verification:**
```python
assert frameresult1[0] == expecteddate
```

### Step 2: Assign frameresult1 = value

```python
frameresult1 = df['T'] + 26 * df['D']
```

**Verification:**
```python
assert frameresult2[0] == expecteddate
```

### Step 3: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'T': [Timestamp('2019-04-30'), Timestamp('2019-04-30')], 'D': [DateOffset(months=1), DateOffset(months=1)]})
```

### Step 4: Assign expecteddate = Timestamp(...)

```python
expecteddate = Timestamp('2021-06-30')
```

**Verification:**
```python
assert frameresult1[0] == expecteddate
```

### Step 5: Assign frameresult2 = value

```python
frameresult2 = df2['T'] + 26 * df2['D']
```


## Complete Example

```python
# Workflow
df = DataFrame({'T': [Timestamp('2019-04-30')], 'D': [DateOffset(months=1)]})
frameresult1 = df['T'] + 26 * df['D']
df2 = DataFrame({'T': [Timestamp('2019-04-30'), Timestamp('2019-04-30')], 'D': [DateOffset(months=1), DateOffset(months=1)]})
expecteddate = Timestamp('2021-06-30')
with tm.assert_produces_warning(PerformanceWarning):
    frameresult2 = df2['T'] + 26 * df2['D']
assert frameresult1[0] == expecteddate
assert frameresult2[0] == expecteddate
```

## Next Steps


---

*Source: test_offsets.py:1122 | Complexity: Intermediate | Last updated: 2026-06-02*