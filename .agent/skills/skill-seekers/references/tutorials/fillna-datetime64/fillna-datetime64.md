# How To: Fillna Datetime64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test fillna datetime64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign idx = pd.DatetimeIndex(...)

```python
idx = pd.DatetimeIndex(['2011-01-01 09:00', pd.NaT, '2011-01-01 11:00'])
```

### Step 2: Assign exp = pd.DatetimeIndex(...)

```python
exp = pd.DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00')), exp)
```

### Step 4: Assign exp = pd.Index(...)

```python
exp = pd.Index([pd.Timestamp('2011-01-01 09:00'), pd.Timestamp('2011-01-01 10:00', tz=tz), pd.Timestamp('2011-01-01 11:00')], dtype=object)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00', tz=tz)), exp)
```

### Step 6: Assign exp = pd.Index(...)

```python
exp = pd.Index([pd.Timestamp('2011-01-01 09:00'), 'x', pd.Timestamp('2011-01-01 11:00')], dtype=object)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna('x'), exp)
```

### Step 8: Assign idx = pd.DatetimeIndex(...)

```python
idx = pd.DatetimeIndex(['2011-01-01 09:00', pd.NaT, '2011-01-01 11:00'], tz=tz)
```

### Step 9: Assign exp = pd.DatetimeIndex(...)

```python
exp = pd.DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], tz=tz)
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00', tz=tz)), exp)
```

### Step 11: Assign exp = pd.Index(...)

```python
exp = pd.Index([pd.Timestamp('2011-01-01 09:00', tz=tz), pd.Timestamp('2011-01-01 10:00'), pd.Timestamp('2011-01-01 11:00', tz=tz)], dtype=object)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00')), exp)
```

### Step 13: Assign exp = pd.Index(...)

```python
exp = pd.Index([pd.Timestamp('2011-01-01 09:00', tz=tz), 'x', pd.Timestamp('2011-01-01 11:00', tz=tz)], dtype=object)
```

### Step 14: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna('x'), exp)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
idx = pd.DatetimeIndex(['2011-01-01 09:00', pd.NaT, '2011-01-01 11:00'])
exp = pd.DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'])
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00')), exp)
exp = pd.Index([pd.Timestamp('2011-01-01 09:00'), pd.Timestamp('2011-01-01 10:00', tz=tz), pd.Timestamp('2011-01-01 11:00')], dtype=object)
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00', tz=tz)), exp)
exp = pd.Index([pd.Timestamp('2011-01-01 09:00'), 'x', pd.Timestamp('2011-01-01 11:00')], dtype=object)
tm.assert_index_equal(idx.fillna('x'), exp)
idx = pd.DatetimeIndex(['2011-01-01 09:00', pd.NaT, '2011-01-01 11:00'], tz=tz)
exp = pd.DatetimeIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], tz=tz)
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00', tz=tz)), exp)
exp = pd.Index([pd.Timestamp('2011-01-01 09:00', tz=tz), pd.Timestamp('2011-01-01 10:00'), pd.Timestamp('2011-01-01 11:00', tz=tz)], dtype=object)
tm.assert_index_equal(idx.fillna(pd.Timestamp('2011-01-01 10:00')), exp)
exp = pd.Index([pd.Timestamp('2011-01-01 09:00', tz=tz), 'x', pd.Timestamp('2011-01-01 11:00', tz=tz)], dtype=object)
tm.assert_index_equal(idx.fillna('x'), exp)
```

## Next Steps


---

*Source: test_fillna.py:9 | Complexity: Advanced | Last updated: 2026-06-02*