# How To: Concat Bool Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat bool types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`

**Setup Required:**
```python
# Fixtures: dtype1, dtype2, expected_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser1 = Series(...)

```python
ser1 = Series([True, False], dtype=dtype1)
```

### Step 2: Assign ser2 = Series(...)

```python
ser2 = Series([False, True], dtype=dtype2)
```

### Step 3: Assign result = concat(...)

```python
result = concat([ser1, ser2], ignore_index=True)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([True, False, False, True], dtype=expected_dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype1, dtype2, expected_dtype

# Workflow
ser1 = Series([True, False], dtype=dtype1)
ser2 = Series([False, True], dtype=dtype2)
result = concat([ser1, ser2], ignore_index=True)
expected = Series([True, False, False, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:677 | Complexity: Intermediate | Last updated: 2026-06-02*