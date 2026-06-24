# How To: First Last Tz Multi Column

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test first last tz multi column

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: method, ts, alpha, unit
```

## Step-by-Step Guide

### Step 1: Assign category_string = Series.astype(...)

```python
category_string = Series(list('abc')).astype('category')
```

### Step 2: Assign dti = pd.date_range(...)

```python
dti = pd.date_range('20130101', periods=3, tz='US/Eastern', unit=unit)
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'group': [1, 1, 2], 'category_string': category_string, 'datetimetz': dti})
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(df.groupby('group'), method)()
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'category_string': pd.Categorical([alpha, 'c'], dtype=category_string.dtype), 'datetimetz': [ts, Timestamp('2013-01-03', tz='US/Eastern')]}, index=Index([1, 2], name='group'))
```

### Step 6: Assign unknown = unknown.dt.as_unit(...)

```python
expected['datetimetz'] = expected['datetimetz'].dt.as_unit(unit)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, ts, alpha, unit

# Workflow
category_string = Series(list('abc')).astype('category')
dti = pd.date_range('20130101', periods=3, tz='US/Eastern', unit=unit)
df = DataFrame({'group': [1, 1, 2], 'category_string': category_string, 'datetimetz': dti})
result = getattr(df.groupby('group'), method)()
expected = DataFrame({'category_string': pd.Categorical([alpha, 'c'], dtype=category_string.dtype), 'datetimetz': [ts, Timestamp('2013-01-03', tz='US/Eastern')]}, index=Index([1, 2], name='group'))
expected['datetimetz'] = expected['datetimetz'].dt.as_unit(unit)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nth.py:415 | Complexity: Intermediate | Last updated: 2026-06-02*