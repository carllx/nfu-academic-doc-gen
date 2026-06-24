# How To: Fillna Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna timedelta

## Prerequisites

**Required Modules:**
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = TimedeltaIndex(...)

```python
idx = TimedeltaIndex(['1 day', NaT, '3 day'])
```

### Step 2: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(['1 day', '2 day', '3 day'])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna(Timedelta('2 day')), exp)
```

### Step 4: Assign exp = TimedeltaIndex(...)

```python
exp = TimedeltaIndex(['1 day', '3 hour', '3 day'])
```

### Step 5: Call idx.fillna()

```python
idx.fillna(Timedelta('3 hour'))
```

### Step 6: Assign exp = Index(...)

```python
exp = Index([Timedelta('1 day'), 'x', Timedelta('3 day')], dtype=object)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.fillna('x'), exp)
```


## Complete Example

```python
# Workflow
idx = TimedeltaIndex(['1 day', NaT, '3 day'])
exp = TimedeltaIndex(['1 day', '2 day', '3 day'])
tm.assert_index_equal(idx.fillna(Timedelta('2 day')), exp)
exp = TimedeltaIndex(['1 day', '3 hour', '3 day'])
idx.fillna(Timedelta('3 hour'))
exp = Index([Timedelta('1 day'), 'x', Timedelta('3 day')], dtype=object)
tm.assert_index_equal(idx.fillna('x'), exp)
```

## Next Steps


---

*Source: test_fillna.py:11 | Complexity: Intermediate | Last updated: 2026-06-02*