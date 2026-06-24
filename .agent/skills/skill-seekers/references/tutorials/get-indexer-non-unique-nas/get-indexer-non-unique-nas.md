# How To: Get Indexer Non Unique Nas

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get indexer non unique nas

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nulls_fixture
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index(['a', 'b', nulls_fixture], dtype=object)
```

### Step 2: Assign unknown = index.get_indexer_non_unique(...)

```python
indexer, missing = index.get_indexer_non_unique([nulls_fixture])
```

### Step 3: Assign expected_indexer = np.array(...)

```python
expected_indexer = np.array([2], dtype=np.intp)
```

### Step 4: Assign expected_missing = np.array(...)

```python
expected_missing = np.array([], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected_indexer)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(missing, expected_missing)
```

### Step 7: Assign index = Index(...)

```python
index = Index(['a', nulls_fixture, 'b', nulls_fixture], dtype=object)
```

### Step 8: Assign unknown = index.get_indexer_non_unique(...)

```python
indexer, missing = index.get_indexer_non_unique([nulls_fixture])
```

### Step 9: Assign expected_indexer = np.array(...)

```python
expected_indexer = np.array([1, 3], dtype=np.intp)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected_indexer)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(missing, expected_missing)
```

### Step 12: Assign index = Index(...)

```python
index = Index(['a', float('NaN'), 'b', float('NaN')], dtype=object)
```

### Step 13: Assign match_but_not_identical = True

```python
match_but_not_identical = True
```

### Step 14: Assign unknown = index.get_indexer_non_unique(...)

```python
indexer, missing = index.get_indexer_non_unique([nulls_fixture])
```

### Step 15: Assign expected_indexer = np.array(...)

```python
expected_indexer = np.array([1, 3], dtype=np.intp)
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(indexer, expected_indexer)
```

### Step 17: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(missing, expected_missing)
```

### Step 18: Assign index = Index(...)

```python
index = Index(['a', Decimal('NaN'), 'b', Decimal('NaN')], dtype=object)
```

### Step 19: Assign match_but_not_identical = True

```python
match_but_not_identical = True
```

### Step 20: Assign match_but_not_identical = False

```python
match_but_not_identical = False
```


## Complete Example

```python
# Setup
# Fixtures: nulls_fixture

# Workflow
index = Index(['a', 'b', nulls_fixture], dtype=object)
indexer, missing = index.get_indexer_non_unique([nulls_fixture])
expected_indexer = np.array([2], dtype=np.intp)
expected_missing = np.array([], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected_indexer)
tm.assert_numpy_array_equal(missing, expected_missing)
index = Index(['a', nulls_fixture, 'b', nulls_fixture], dtype=object)
indexer, missing = index.get_indexer_non_unique([nulls_fixture])
expected_indexer = np.array([1, 3], dtype=np.intp)
tm.assert_numpy_array_equal(indexer, expected_indexer)
tm.assert_numpy_array_equal(missing, expected_missing)
if is_matching_na(nulls_fixture, float('NaN')):
    index = Index(['a', float('NaN'), 'b', float('NaN')], dtype=object)
    match_but_not_identical = True
elif is_matching_na(nulls_fixture, Decimal('NaN')):
    index = Index(['a', Decimal('NaN'), 'b', Decimal('NaN')], dtype=object)
    match_but_not_identical = True
else:
    match_but_not_identical = False
if match_but_not_identical:
    indexer, missing = index.get_indexer_non_unique([nulls_fixture])
    expected_indexer = np.array([1, 3], dtype=np.intp)
    tm.assert_numpy_array_equal(indexer, expected_indexer)
    tm.assert_numpy_array_equal(missing, expected_missing)
```

## Next Steps


---

*Source: test_indexing.py:76 | Complexity: Advanced | Last updated: 2026-06-02*