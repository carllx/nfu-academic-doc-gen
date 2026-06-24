# How To: Fillna Period

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna period

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01-01 09:00', NaT, '2011-01-01 11:00'], freq='h')
```

### Step 2: Assign exp = PeriodIndex(...)

```python
exp = PeriodIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='h')
```

### Step 3: Assign result = idx.fillna(...)

```python
result = idx.fillna(Period('2011-01-01 10:00', freq='h'))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

### Step 5: Assign exp = Index(...)

```python
exp = Index([Period('2011-01-01 09:00', freq='h'), 'x', Period('2011-01-01 11:00', freq='h')], dtype=object)
```

### Step 6: Assign result = idx.fillna(...)

```python
result = idx.fillna('x')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```

### Step 8: Assign exp = Index(...)

```python
exp = Index([Period('2011-01-01 09:00', freq='h'), Period('2011-01-01', freq='D'), Period('2011-01-01 11:00', freq='h')], dtype=object)
```

### Step 9: Assign result = idx.fillna(...)

```python
result = idx.fillna(Period('2011-01-01', freq='D'))
```

### Step 10: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, exp)
```


## Complete Example

```python
# Workflow
idx = PeriodIndex(['2011-01-01 09:00', NaT, '2011-01-01 11:00'], freq='h')
exp = PeriodIndex(['2011-01-01 09:00', '2011-01-01 10:00', '2011-01-01 11:00'], freq='h')
result = idx.fillna(Period('2011-01-01 10:00', freq='h'))
tm.assert_index_equal(result, exp)
exp = Index([Period('2011-01-01 09:00', freq='h'), 'x', Period('2011-01-01 11:00', freq='h')], dtype=object)
result = idx.fillna('x')
tm.assert_index_equal(result, exp)
exp = Index([Period('2011-01-01 09:00', freq='h'), Period('2011-01-01', freq='D'), Period('2011-01-01 11:00', freq='h')], dtype=object)
result = idx.fillna(Period('2011-01-01', freq='D'))
tm.assert_index_equal(result, exp)
```

## Next Steps


---

*Source: test_fillna.py:11 | Complexity: Advanced | Last updated: 2026-06-02*