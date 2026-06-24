# How To: Constructor Interval Values Mismatched Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor interval values mismatched dtype

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

### Step 2: Assign ii = IntervalIndex.from_breaks(...)

```python
ii = IntervalIndex.from_breaks(dti)
```

### Step 3: Assign result = Index(...)

```python
result = Index(ii, dtype='category')
```

### Step 4: Assign expected = CategoricalIndex(...)

```python
expected = CategoricalIndex(ii)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
ii = IntervalIndex.from_breaks(dti)
result = Index(ii, dtype='category')
expected = CategoricalIndex(ii)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_index_new.py:266 | Complexity: Intermediate | Last updated: 2026-06-02*