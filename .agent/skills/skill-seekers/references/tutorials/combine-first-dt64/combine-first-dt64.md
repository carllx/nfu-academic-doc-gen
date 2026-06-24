# How To: Combine First Dt64

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first dt64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign s0 = to_datetime.dt.as_unit(...)

```python
s0 = to_datetime(Series(['2010', np.nan])).dt.as_unit(unit)
```

### Step 2: Assign s1 = to_datetime.dt.as_unit(...)

```python
s1 = to_datetime(Series([np.nan, '2011'])).dt.as_unit(unit)
```

### Step 3: Assign rs = s0.combine_first(...)

```python
rs = s0.combine_first(s1)
```

### Step 4: Assign xp = to_datetime.dt.as_unit(...)

```python
xp = to_datetime(Series(['2010', '2011'])).dt.as_unit(unit)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, xp)
```

### Step 6: Assign s0 = to_datetime.dt.as_unit(...)

```python
s0 = to_datetime(Series(['2010', np.nan])).dt.as_unit(unit)
```

### Step 7: Assign s1 = Series(...)

```python
s1 = Series([np.nan, '2011'])
```

### Step 8: Assign rs = s0.combine_first(...)

```python
rs = s0.combine_first(s1)
```

### Step 9: Assign xp = Series(...)

```python
xp = Series([datetime(2010, 1, 1), '2011'], dtype='datetime64[ns]')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, xp)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
s0 = to_datetime(Series(['2010', np.nan])).dt.as_unit(unit)
s1 = to_datetime(Series([np.nan, '2011'])).dt.as_unit(unit)
rs = s0.combine_first(s1)
xp = to_datetime(Series(['2010', '2011'])).dt.as_unit(unit)
tm.assert_series_equal(rs, xp)
s0 = to_datetime(Series(['2010', np.nan])).dt.as_unit(unit)
s1 = Series([np.nan, '2011'])
rs = s0.combine_first(s1)
xp = Series([datetime(2010, 1, 1), '2011'], dtype='datetime64[ns]')
tm.assert_series_equal(rs, xp)
```

## Next Steps


---

*Source: test_combine_first.py:73 | Complexity: Advanced | Last updated: 2026-06-02*