# How To: To Records Datetimeindex With Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to records datetimeindex with tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `email`
- `email.parser`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz
```

## Step-by-Step Guide

### Step 1: Assign dr = date_range(...)

```python
dr = date_range('2016-01-01', periods=10, freq='s', tz=tz)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'datetime': dr}, index=dr)
```

### Step 3: Assign expected = df.to_records(...)

```python
expected = df.to_records()
```

### Step 4: Assign result = df.tz_convert.to_records(...)

```python
result = df.tz_convert('UTC').to_records()
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz

# Workflow
dr = date_range('2016-01-01', periods=10, freq='s', tz=tz)
df = DataFrame({'datetime': dr}, index=dr)
expected = df.to_records()
result = df.tz_convert('UTC').to_records()
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_to_records.py:513 | Complexity: Intermediate | Last updated: 2026-06-02*