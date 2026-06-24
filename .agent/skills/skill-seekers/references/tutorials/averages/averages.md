# How To: Averages

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test averages

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: df, method
```

## Step-by-Step Guide

### Step 1: Assign expected_columns_numeric = Index(...)

```python
expected_columns_numeric = Index(['int', 'float', 'category_int'])
```

### Step 2: Assign gb = df.groupby(...)

```python
gb = df.groupby('group')
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'category_int': [7.5, 9], 'float': [4.5, 6.0], 'timedelta': [pd.Timedelta('1.5s'), pd.Timedelta('3s')], 'int': [1.5, 3], 'datetime': [Timestamp('2013-01-01 12:00:00'), Timestamp('2013-01-03 00:00:00')], 'datetimetz': [Timestamp('2013-01-01 12:00:00', tz='US/Eastern'), Timestamp('2013-01-03 00:00:00', tz='US/Eastern')]}, index=Index([1, 2], name='group'), columns=['int', 'float', 'category_int'])
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(gb, method)(numeric_only=True)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result.reindex_like(expected), expected)
```

### Step 6: Assign expected_columns = value

```python
expected_columns = expected.columns
```

### Step 7: Call self._check()

```python
self._check(df, method, expected_columns, expected_columns_numeric)
```


## Complete Example

```python
# Setup
# Fixtures: df, method

# Workflow
expected_columns_numeric = Index(['int', 'float', 'category_int'])
gb = df.groupby('group')
expected = DataFrame({'category_int': [7.5, 9], 'float': [4.5, 6.0], 'timedelta': [pd.Timedelta('1.5s'), pd.Timedelta('3s')], 'int': [1.5, 3], 'datetime': [Timestamp('2013-01-01 12:00:00'), Timestamp('2013-01-03 00:00:00')], 'datetimetz': [Timestamp('2013-01-01 12:00:00', tz='US/Eastern'), Timestamp('2013-01-03 00:00:00', tz='US/Eastern')]}, index=Index([1, 2], name='group'), columns=['int', 'float', 'category_int'])
result = getattr(gb, method)(numeric_only=True)
tm.assert_frame_equal(result.reindex_like(expected), expected)
expected_columns = expected.columns
self._check(df, method, expected_columns, expected_columns_numeric)
```

## Next Steps


---

*Source: test_numeric_only.py:56 | Complexity: Intermediate | Last updated: 2026-06-02*