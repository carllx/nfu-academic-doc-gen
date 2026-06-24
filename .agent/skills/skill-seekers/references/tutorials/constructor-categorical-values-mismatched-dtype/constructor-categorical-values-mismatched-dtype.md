# How To: Constructor Categorical Values Mismatched Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor categorical values mismatched dtype

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

### Step 2: Assign cat = Categorical(...)

```python
cat = Categorical(dti)
```

### Step 3: Assign result = Index(...)

```python
result = Index(cat, dti.dtype)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, dti)
```

### Step 5: Assign dti2 = dti.tz_localize(...)

```python
dti2 = dti.tz_localize('Asia/Tokyo')
```

### Step 6: Assign cat2 = Categorical(...)

```python
cat2 = Categorical(dti2)
```

### Step 7: Assign result = Index(...)

```python
result = Index(cat2, dti2.dtype)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, dti2)
```

### Step 9: Assign ii = IntervalIndex.from_breaks(...)

```python
ii = IntervalIndex.from_breaks(range(5))
```

### Step 10: Assign cat3 = Categorical(...)

```python
cat3 = Categorical(ii)
```

### Step 11: Assign result = Index(...)

```python
result = Index(cat3, dtype=ii.dtype)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, ii)
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3)
cat = Categorical(dti)
result = Index(cat, dti.dtype)
tm.assert_index_equal(result, dti)
dti2 = dti.tz_localize('Asia/Tokyo')
cat2 = Categorical(dti2)
result = Index(cat2, dti2.dtype)
tm.assert_index_equal(result, dti2)
ii = IntervalIndex.from_breaks(range(5))
cat3 = Categorical(ii)
result = Index(cat3, dtype=ii.dtype)
tm.assert_index_equal(result, ii)
```

## Next Steps


---

*Source: test_index_new.py:226 | Complexity: Advanced | Last updated: 2026-06-02*