# How To: Concat Repeated Keys

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat repeated keys

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
# Fixtures: keys, integrity
```

## Step-by-Step Guide

### Step 1: Assign series_list = value

```python
series_list = [Series({'a': 1}), Series({'b': 2}), Series({'c': 3})]
```

### Step 2: Assign result = concat(...)

```python
result = concat(series_list, keys=keys, verify_integrity=integrity)
```

### Step 3: Assign tuples = list(...)

```python
tuples = list(zip(keys, ['a', 'b', 'c']))
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 2, 3], index=MultiIndex.from_tuples(tuples))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: keys, integrity

# Workflow
series_list = [Series({'a': 1}), Series({'b': 2}), Series({'c': 3})]
result = concat(series_list, keys=keys, verify_integrity=integrity)
tuples = list(zip(keys, ['a', 'b', 'c']))
expected = Series([1, 2, 3], index=MultiIndex.from_tuples(tuples))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_concat.py:695 | Complexity: Intermediate | Last updated: 2026-06-02*