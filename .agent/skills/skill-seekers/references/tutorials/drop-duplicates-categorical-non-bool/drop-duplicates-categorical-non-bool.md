# How To: Drop Duplicates Categorical Non Bool

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop duplicates categorical non bool

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: cat_series_unused_category
```

## Step-by-Step Guide

### Step 1: Assign tc1 = cat_series_unused_category

```python
tc1 = cat_series_unused_category
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([False, False, False, True])
```

### Step 3: Assign result = tc1.duplicated(...)

```python
result = tc1.duplicated()
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = tc1.drop_duplicates(...)

```python
result = tc1.drop_duplicates()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, tc1[~expected])
```

### Step 7: Assign sc = tc1.copy(...)

```python
sc = tc1.copy()
```

### Step 8: Assign return_value = sc.drop_duplicates(...)

```python
return_value = sc.drop_duplicates(inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sc, tc1[~expected])
```


## Complete Example

```python
# Setup
# Fixtures: cat_series_unused_category

# Workflow
tc1 = cat_series_unused_category
expected = Series([False, False, False, True])
result = tc1.duplicated()
tm.assert_series_equal(result, expected)
result = tc1.drop_duplicates()
tm.assert_series_equal(result, tc1[~expected])
sc = tc1.copy()
return_value = sc.drop_duplicates(inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc1[~expected])
```

## Next Steps


---

*Source: test_drop_duplicates.py:90 | Complexity: Advanced | Last updated: 2026-06-02*