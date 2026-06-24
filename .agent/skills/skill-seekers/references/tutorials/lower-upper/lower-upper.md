# How To: Lower Upper

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test lower upper

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['om', np.nan, 'nom', 'nom'], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.upper(...)

```python
result = s.str.upper()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['OM', np.nan, 'NOM', 'NOM'], dtype=any_string_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = result.str.lower(...)

```python
result = result.str.lower()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['om', np.nan, 'nom', 'nom'], dtype=any_string_dtype)
result = s.str.upper()
expected = Series(['OM', np.nan, 'NOM', 'NOM'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
result = result.str.lower()
tm.assert_series_equal(result, s)
```

## Next Steps


---

*Source: test_case_justify.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*