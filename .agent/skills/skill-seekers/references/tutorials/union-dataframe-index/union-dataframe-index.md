# How To: Union Dataframe Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union dataframe index

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

### Step 1: Assign rng1 = date_range(...)

```python
rng1 = date_range('1/1/1999', '1/1/2012', freq='MS')
```

### Step 2: Assign s1 = Series(...)

```python
s1 = Series(np.random.default_rng(2).standard_normal(len(rng1)), rng1)
```

### Step 3: Assign rng2 = date_range(...)

```python
rng2 = date_range('1/1/1980', '12/1/2001', freq='MS')
```

### Step 4: Assign s2 = Series(...)

```python
s2 = Series(np.random.default_rng(2).standard_normal(len(rng2)), rng2)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'s1': s1, 's2': s2})
```

### Step 6: Assign exp = date_range(...)

```python
exp = date_range('1/1/1980', '1/1/2012', freq='MS')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(df.index, exp)
```


## Complete Example

```python
# Workflow
rng1 = date_range('1/1/1999', '1/1/2012', freq='MS')
s1 = Series(np.random.default_rng(2).standard_normal(len(rng1)), rng1)
rng2 = date_range('1/1/1980', '12/1/2001', freq='MS')
s2 = Series(np.random.default_rng(2).standard_normal(len(rng2)), rng2)
df = DataFrame({'s1': s1, 's2': s2})
exp = date_range('1/1/1980', '1/1/2012', freq='MS')
tm.assert_index_equal(df.index, exp)
```

## Next Steps


---

*Source: test_setops.py:177 | Complexity: Intermediate | Last updated: 2026-06-02*