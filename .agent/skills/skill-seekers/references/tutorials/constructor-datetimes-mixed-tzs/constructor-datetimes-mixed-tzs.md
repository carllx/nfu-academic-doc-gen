# How To: Constructor Datetimes Mixed Tzs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor datetimes mixed tzs

## Prerequisites

**Required Modules:**
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign tz = maybe_get_tz(...)

```python
tz = maybe_get_tz('US/Central')
```

### Step 2: Assign dt1 = datetime(...)

```python
dt1 = datetime(2020, 1, 1, tzinfo=tz)
```

### Step 3: Assign dt2 = datetime(...)

```python
dt2 = datetime(2020, 1, 1, tzinfo=timezone.utc)
```

### Step 4: Assign result = Index(...)

```python
result = Index([dt1, dt2])
```

### Step 5: Assign expected = Index(...)

```python
expected = Index([dt1, dt2], dtype=object)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
tz = maybe_get_tz('US/Central')
dt1 = datetime(2020, 1, 1, tzinfo=tz)
dt2 = datetime(2020, 1, 1, tzinfo=timezone.utc)
result = Index([dt1, dt2])
expected = Index([dt1, dt2], dtype=object)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_index_new.py:189 | Complexity: Intermediate | Last updated: 2026-06-02*