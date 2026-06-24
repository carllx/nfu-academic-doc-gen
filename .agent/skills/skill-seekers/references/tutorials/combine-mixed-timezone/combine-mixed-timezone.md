# How To: Combine Mixed Timezone

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine mixed timezone

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign uniform_tz = Series(...)

```python
uniform_tz = Series({pd.Timestamp('2019-05-01', tz='UTC'): 1.0})
```

### Step 2: Assign multi_tz = Series(...)

```python
multi_tz = Series({pd.Timestamp('2019-05-01 01:00:00+0100', tz='Europe/London'): 2.0, pd.Timestamp('2019-05-02', tz='UTC'): 3.0})
```

### Step 3: Assign result = uniform_tz.combine_first(...)

```python
result = uniform_tz.combine_first(multi_tz)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1.0, 3.0], index=pd.Index([pd.Timestamp('2019-05-01 00:00:00+00:00', tz='UTC'), pd.Timestamp('2019-05-02 00:00:00+00:00', tz='UTC')], dtype='object'))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
uniform_tz = Series({pd.Timestamp('2019-05-01', tz='UTC'): 1.0})
multi_tz = Series({pd.Timestamp('2019-05-01 01:00:00+0100', tz='Europe/London'): 2.0, pd.Timestamp('2019-05-02', tz='UTC'): 3.0})
result = uniform_tz.combine_first(multi_tz)
expected = Series([1.0, 3.0], index=pd.Index([pd.Timestamp('2019-05-01 00:00:00+00:00', tz='UTC'), pd.Timestamp('2019-05-02 00:00:00+00:00', tz='UTC')], dtype='object'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_first.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*