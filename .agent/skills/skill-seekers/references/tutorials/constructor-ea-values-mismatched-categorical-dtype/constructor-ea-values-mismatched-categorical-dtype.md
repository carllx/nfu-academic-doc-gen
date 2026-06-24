# How To: Constructor Ea Values Mismatched Categorical Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor ea values mismatched categorical dtype

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

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3)
```

### Step 2: Assign result = Index(...)

```python
result = Index(dti, dtype='category')
```

### Step 3: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(dti)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign dti2 = date_range(...)

```python
dti2 = date_range('2016-01-01', periods=3, tz='US/Pacific')
```

### Step 6: Assign result = Index(...)

```python
result = Index(dti2, dtype='category')
```

### Step 7: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(dti2)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
result = Index(dti, dtype='category')
expected = CategoricalIndex(dti)
tm.assert_index_equal(result, expected)
dti2 = date_range('2016-01-01', periods=3, tz='US/Pacific')
result = Index(dti2, dtype='category')
expected = CategoricalIndex(dti2)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_index_new.py:242 | Complexity: Advanced | Last updated: 2026-06-02*