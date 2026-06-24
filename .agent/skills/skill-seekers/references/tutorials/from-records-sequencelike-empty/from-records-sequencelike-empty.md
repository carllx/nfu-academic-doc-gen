# How To: From Records Sequencelike Empty

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from records sequencelike empty

## Prerequisites

**Required Modules:**
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pytz`
- `pandas._config`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign result = DataFrame.from_records(...)

```python
result = DataFrame.from_records([], columns=['foo', 'bar', 'baz'])
```

**Verification:**
```python
assert len(result) == 0
```

### Step 2: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.columns, Index(['foo', 'bar', 'baz']))
```

**Verification:**
```python
assert len(result) == 0
```

### Step 3: Assign result = DataFrame.from_records(...)

```python
result = DataFrame.from_records([])
```

**Verification:**
```python
assert len(result.columns) == 0
```


## Complete Example

```python
# Workflow
result = DataFrame.from_records([], columns=['foo', 'bar', 'baz'])
assert len(result) == 0
tm.assert_index_equal(result.columns, Index(['foo', 'bar', 'baz']))
result = DataFrame.from_records([])
assert len(result) == 0
assert len(result.columns) == 0
```

## Next Steps


---

*Source: test_from_records.py:140 | Complexity: Beginner | Last updated: 2026-06-02*