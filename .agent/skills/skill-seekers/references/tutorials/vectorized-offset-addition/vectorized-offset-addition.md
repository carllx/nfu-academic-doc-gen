# How To: Vectorized Offset Addition

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test vectorized offset addition

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas.tests.tseries.offsets.common`

**Setup Required:**
```python
# Fixtures: klass
```

## Step-by-Step Guide

### Step 1: Assign shift = klass(...)

```python
shift = klass([Timestamp('2000-01-15 00:15:00', tz='US/Central'), Timestamp('2000-02-15', tz='US/Central')], name='a')
```

### Step 2: Assign exp = klass(...)

```python
exp = klass([Timestamp('2000-02-01 00:15:00', tz='US/Central'), Timestamp('2000-03-01', tz='US/Central')], name='a')
```

### Step 3: Call tm.assert_equal()

```python
tm.assert_equal(result, exp)
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(result2, exp)
```

### Step 5: Assign shift = klass(...)

```python
shift = klass([Timestamp('2000-01-01 00:15:00', tz='US/Central'), Timestamp('2000-02-01', tz='US/Central')], name='a')
```

### Step 6: Assign exp = klass(...)

```python
exp = klass([Timestamp('2000-01-15 00:15:00', tz='US/Central'), Timestamp('2000-02-15', tz='US/Central')], name='a')
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, exp)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result2, exp)
```

### Step 9: Assign result = value

```python
result = shift + SemiMonthBegin()
```

### Step 10: Assign result2 = value

```python
result2 = SemiMonthBegin() + shift
```

### Step 11: Assign result = value

```python
result = shift + SemiMonthBegin()
```

### Step 12: Assign result2 = value

```python
result2 = SemiMonthBegin() + shift
```


## Complete Example

```python
# Setup
# Fixtures: klass

# Workflow
shift = klass([Timestamp('2000-01-15 00:15:00', tz='US/Central'), Timestamp('2000-02-15', tz='US/Central')], name='a')
with tm.assert_produces_warning(None):
    result = shift + SemiMonthBegin()
    result2 = SemiMonthBegin() + shift
exp = klass([Timestamp('2000-02-01 00:15:00', tz='US/Central'), Timestamp('2000-03-01', tz='US/Central')], name='a')
tm.assert_equal(result, exp)
tm.assert_equal(result2, exp)
shift = klass([Timestamp('2000-01-01 00:15:00', tz='US/Central'), Timestamp('2000-02-01', tz='US/Central')], name='a')
with tm.assert_produces_warning(None):
    result = shift + SemiMonthBegin()
    result2 = SemiMonthBegin() + shift
exp = klass([Timestamp('2000-01-15 00:15:00', tz='US/Central'), Timestamp('2000-02-15', tz='US/Central')], name='a')
tm.assert_equal(result, exp)
tm.assert_equal(result2, exp)
```

## Next Steps


---

*Source: test_month.py:467 | Complexity: Advanced | Last updated: 2026-06-02*