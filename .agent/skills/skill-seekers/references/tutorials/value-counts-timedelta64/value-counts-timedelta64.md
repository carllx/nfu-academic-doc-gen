# How To: Value Counts Timedelta64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts timedelta64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.base.common`

**Setup Required:**
```python
# Fixtures: index_or_series, unit
```

## Step-by-Step Guide

### Step 1: Assign klass = index_or_series

```python
klass = index_or_series
```

### Step 2: Assign day = Timedelta.as_unit(...)

```python
day = Timedelta(timedelta(1)).as_unit(unit)
```

### Step 3: Assign tdi = TimedeltaIndex.as_unit(...)

```python
tdi = TimedeltaIndex([day], name='dt').as_unit(unit)
```

### Step 4: Assign tdvals = value

```python
tdvals = np.zeros(6, dtype=f'm8[{unit}]') + day
```

### Step 5: Assign td = klass(...)

```python
td = klass(tdvals, name='dt')
```

### Step 6: Assign result = td.value_counts(...)

```python
result = td.value_counts()
```

### Step 7: Assign expected_s = Series(...)

```python
expected_s = Series([6], index=tdi, name='count')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected_s)
```

### Step 9: Assign expected = tdi

```python
expected = tdi
```

### Step 10: Assign result = td.unique(...)

```python
result = td.unique()
```

### Step 11: Assign td2 = value

```python
td2 = day + np.zeros(6, dtype=f'm8[{unit}]')
```

### Step 12: Assign td2 = klass(...)

```python
td2 = klass(td2, name='dt')
```

### Step 13: Assign result2 = td2.value_counts(...)

```python
result2 = td2.value_counts()
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result2, expected_s)
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 16: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected._values)
```


## Complete Example

```python
# Setup
# Fixtures: index_or_series, unit

# Workflow
klass = index_or_series
day = Timedelta(timedelta(1)).as_unit(unit)
tdi = TimedeltaIndex([day], name='dt').as_unit(unit)
tdvals = np.zeros(6, dtype=f'm8[{unit}]') + day
td = klass(tdvals, name='dt')
result = td.value_counts()
expected_s = Series([6], index=tdi, name='count')
tm.assert_series_equal(result, expected_s)
expected = tdi
result = td.unique()
if isinstance(td, Index):
    tm.assert_index_equal(result, expected)
else:
    tm.assert_extension_array_equal(result, expected._values)
td2 = day + np.zeros(6, dtype=f'm8[{unit}]')
td2 = klass(td2, name='dt')
result2 = td2.value_counts()
tm.assert_series_equal(result2, expected_s)
```

## Next Steps


---

*Source: test_value_counts.py:305 | Complexity: Advanced | Last updated: 2026-06-02*