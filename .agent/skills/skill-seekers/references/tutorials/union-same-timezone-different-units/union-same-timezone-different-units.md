# How To: Union Same Timezone Different Units

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union same timezone different units

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`
- `pandas`
- `pandas`
- `pandas._libs.tslibs.timezones`


## Step-by-Step Guide

### Step 1: Assign idx1 = date_range.as_unit(...)

```python
idx1 = date_range('2000-01-01', periods=3, tz='UTC').as_unit('ms')
```

### Step 2: Assign idx2 = date_range.as_unit(...)

```python
idx2 = date_range('2000-01-01', periods=3, tz='UTC').as_unit('us')
```

### Step 3: Assign result = idx1.union(...)

```python
result = idx1.union(idx2)
```

### Step 4: Assign expected = date_range.as_unit(...)

```python
expected = date_range('2000-01-01', periods=3, tz='UTC').as_unit('us')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx1 = date_range('2000-01-01', periods=3, tz='UTC').as_unit('ms')
idx2 = date_range('2000-01-01', periods=3, tz='UTC').as_unit('us')
result = idx1.union(idx2)
expected = date_range('2000-01-01', periods=3, tz='UTC').as_unit('us')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:196 | Complexity: Intermediate | Last updated: 2026-06-02*