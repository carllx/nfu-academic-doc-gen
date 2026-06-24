# How To: Drop Duplicates Categorical Non Bool2 Keepfalse

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop duplicates categorical non bool2 keepfalse

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
# Fixtures: cat_series
```

## Step-by-Step Guide

### Step 1: Assign tc2 = cat_series

```python
tc2 = cat_series
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([False, True, True, False, True, True, False])
```

### Step 3: Assign result = tc2.duplicated(...)

```python
result = tc2.duplicated(keep=False)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = tc2.drop_duplicates(...)

```python
result = tc2.drop_duplicates(keep=False)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, tc2[~expected])
```

### Step 7: Assign sc = tc2.copy(...)

```python
sc = tc2.copy()
```

### Step 8: Assign return_value = sc.drop_duplicates(...)

```python
return_value = sc.drop_duplicates(keep=False, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sc, tc2[~expected])
```


## Complete Example

```python
# Setup
# Fixtures: cat_series

# Workflow
tc2 = cat_series
expected = Series([False, True, True, False, True, True, False])
result = tc2.duplicated(keep=False)
tm.assert_series_equal(result, expected)
result = tc2.drop_duplicates(keep=False)
tm.assert_series_equal(result, tc2[~expected])
sc = tc2.copy()
return_value = sc.drop_duplicates(keep=False, inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc2[~expected])
```

## Next Steps


---

*Source: test_drop_duplicates.py:184 | Complexity: Advanced | Last updated: 2026-06-02*