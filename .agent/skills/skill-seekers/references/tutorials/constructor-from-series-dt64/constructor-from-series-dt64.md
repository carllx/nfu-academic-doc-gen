# How To: Constructor From Series Dt64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor from series dt64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: klass
```

## Step-by-Step Guide

### Step 1: Assign stamps = value

```python
stamps = [Timestamp('20110101'), Timestamp('20120101'), Timestamp('20130101')]
```

### Step 2: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(stamps)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(stamps)
```

### Step 4: Assign result = klass(...)

```python
result = klass(ser)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: klass

# Workflow
stamps = [Timestamp('20110101'), Timestamp('20120101'), Timestamp('20130101')]
expected = DatetimeIndex(stamps)
ser = Series(stamps)
result = klass(ser)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_index_new.py:387 | Complexity: Intermediate | Last updated: 2026-06-02*