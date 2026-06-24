# How To: Drop Duplicates Categorical Bool

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop duplicates categorical bool

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
# Fixtures: ordered
```

## Step-by-Step Guide

### Step 1: Assign tc = Series(...)

```python
tc = Series(Categorical([True, False, True, False], categories=[True, False], ordered=ordered))
```

**Verification:**
```python
assert return_value is None
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([False, False, True, True])
```

**Verification:**
```python
assert return_value is None
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(tc.duplicated(), expected)
```

**Verification:**
```python
assert return_value is None
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(tc.drop_duplicates(), tc[~expected])
```

### Step 5: Assign sc = tc.copy(...)

```python
sc = tc.copy()
```

### Step 6: Assign return_value = sc.drop_duplicates(...)

```python
return_value = sc.drop_duplicates(inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sc, tc[~expected])
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([True, True, False, False])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(tc.duplicated(keep='last'), expected)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(tc.drop_duplicates(keep='last'), tc[~expected])
```

### Step 11: Assign sc = tc.copy(...)

```python
sc = tc.copy()
```

### Step 12: Assign return_value = sc.drop_duplicates(...)

```python
return_value = sc.drop_duplicates(keep='last', inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sc, tc[~expected])
```

### Step 14: Assign expected = Series(...)

```python
expected = Series([True, True, True, True])
```

### Step 15: Call tm.assert_series_equal()

```python
tm.assert_series_equal(tc.duplicated(keep=False), expected)
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(tc.drop_duplicates(keep=False), tc[~expected])
```

### Step 17: Assign sc = tc.copy(...)

```python
sc = tc.copy()
```

### Step 18: Assign return_value = sc.drop_duplicates(...)

```python
return_value = sc.drop_duplicates(keep=False, inplace=True)
```

**Verification:**
```python
assert return_value is None
```

### Step 19: Call tm.assert_series_equal()

```python
tm.assert_series_equal(sc, tc[~expected])
```


## Complete Example

```python
# Setup
# Fixtures: ordered

# Workflow
tc = Series(Categorical([True, False, True, False], categories=[True, False], ordered=ordered))
expected = Series([False, False, True, True])
tm.assert_series_equal(tc.duplicated(), expected)
tm.assert_series_equal(tc.drop_duplicates(), tc[~expected])
sc = tc.copy()
return_value = sc.drop_duplicates(inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc[~expected])
expected = Series([True, True, False, False])
tm.assert_series_equal(tc.duplicated(keep='last'), expected)
tm.assert_series_equal(tc.drop_duplicates(keep='last'), tc[~expected])
sc = tc.copy()
return_value = sc.drop_duplicates(keep='last', inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc[~expected])
expected = Series([True, True, True, True])
tm.assert_series_equal(tc.duplicated(keep=False), expected)
tm.assert_series_equal(tc.drop_duplicates(keep=False), tc[~expected])
sc = tc.copy()
return_value = sc.drop_duplicates(keep=False, inplace=True)
assert return_value is None
tm.assert_series_equal(sc, tc[~expected])
```

## Next Steps


---

*Source: test_drop_duplicates.py:200 | Complexity: Advanced | Last updated: 2026-06-02*