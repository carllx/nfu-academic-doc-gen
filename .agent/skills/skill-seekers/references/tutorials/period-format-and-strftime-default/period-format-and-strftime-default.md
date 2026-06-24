# How To: Period Format And Strftime Default

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test period format and strftime default

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

### Step 1: Assign per = PeriodIndex(...)

```python
per = PeriodIndex([datetime(2003, 1, 1, 12), None], freq='h')
```

**Verification:**
```python
assert formatted[0] == '2003-01-01 12:00'
```

### Step 2: Assign msg = 'PeriodIndex.format is deprecated'

```python
msg = 'PeriodIndex.format is deprecated'
```

**Verification:**
```python
assert formatted[1] == 'NaT'
```

### Step 3: Assign per = pd.period_range(...)

```python
per = pd.period_range('2003-01-01 12:01:01.123456789', periods=2, freq='ns')
```

**Verification:**
```python
assert formatted[0] == per.strftime(None)[0]
```

### Step 4: Assign formatted = per.format(...)

```python
formatted = per.format()
```

**Verification:**
```python
assert per.strftime(None)[1] is np.nan
```

### Step 5: Assign formatted = per.format(...)

```python
formatted = per.format()
```

**Verification:**
```python
assert (formatted == per.strftime(None)).all()
```


## Complete Example

```python
# Workflow
per = PeriodIndex([datetime(2003, 1, 1, 12), None], freq='h')
msg = 'PeriodIndex.format is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    formatted = per.format()
assert formatted[0] == '2003-01-01 12:00'
assert formatted[1] == 'NaT'
assert formatted[0] == per.strftime(None)[0]
assert per.strftime(None)[1] is np.nan
per = pd.period_range('2003-01-01 12:01:01.123456789', periods=2, freq='ns')
with tm.assert_produces_warning(FutureWarning, match=msg):
    formatted = per.format()
assert (formatted == per.strftime(None)).all()
assert formatted[0] == '2003-01-01 12:01:01.123456789'
assert formatted[1] == '2003-01-01 12:01:01.123456790'
```

## Next Steps


---

*Source: test_formats.py:221 | Complexity: Intermediate | Last updated: 2026-06-02*