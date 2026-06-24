# How To: Timestamp Repr Pre1900

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timestamp repr pre1900

## Prerequisites

**Required Modules:**
- `datetime`
- `pprint`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign stamp = Timestamp(...)

```python
stamp = Timestamp('1850-01-01', tz='US/Eastern')
```

**Verification:**
```python
assert iso8601 in result
```

### Step 2: Call repr()

```python
repr(stamp)
```

### Step 3: Assign iso8601 = '1850-01-01 01:23:45.012345'

```python
iso8601 = '1850-01-01 01:23:45.012345'
```

### Step 4: Assign stamp = Timestamp(...)

```python
stamp = Timestamp(iso8601, tz='US/Eastern')
```

### Step 5: Assign result = repr(...)

```python
result = repr(stamp)
```

**Verification:**
```python
assert iso8601 in result
```


## Complete Example

```python
# Workflow
stamp = Timestamp('1850-01-01', tz='US/Eastern')
repr(stamp)
iso8601 = '1850-01-01 01:23:45.012345'
stamp = Timestamp(iso8601, tz='US/Eastern')
result = repr(stamp)
assert iso8601 in result
```

## Next Steps


---

*Source: test_formats.py:128 | Complexity: Intermediate | Last updated: 2026-06-02*