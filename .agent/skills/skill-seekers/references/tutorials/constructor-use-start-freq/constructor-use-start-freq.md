# How To: Constructor Use Start Freq

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor use start freq

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.period`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign msg1 = 'Period with BDay freq is deprecated'

```python
msg1 = 'Period with BDay freq is deprecated'
```

### Step 2: Assign msg2 = 'PeriodDtype\\[B\\] is deprecated'

```python
msg2 = 'PeriodDtype\\[B\\] is deprecated'
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(index, expected)
```

### Step 4: Assign p = Period(...)

```python
p = Period('4/2/2012', freq='B')
```

### Step 5: Assign expected = period_range(...)

```python
expected = period_range(start='4/2/2012', periods=10, freq='B')
```

### Step 6: Assign index = period_range(...)

```python
index = period_range(start=p, periods=10)
```


## Complete Example

```python
# Workflow
msg1 = 'Period with BDay freq is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg1):
    p = Period('4/2/2012', freq='B')
msg2 = 'PeriodDtype\\[B\\] is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg2):
    expected = period_range(start='4/2/2012', periods=10, freq='B')
with tm.assert_produces_warning(FutureWarning, match=msg2):
    index = period_range(start=p, periods=10)
tm.assert_index_equal(index, expected)
```

## Next Steps


---

*Source: test_constructors.py:142 | Complexity: Intermediate | Last updated: 2026-06-02*