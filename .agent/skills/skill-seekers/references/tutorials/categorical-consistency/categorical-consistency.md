# How To: Categorical Consistency

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test categorical consistency

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.util.hashing`
- `pandas.util`

**Setup Required:**
```python
# Fixtures: s1, categorize
```

## Step-by-Step Guide

### Step 1: Assign s2 = s1.astype.cat.set_categories(...)

```python
s2 = s1.astype('category').cat.set_categories(s1)
```

### Step 2: Assign s3 = s2.cat.set_categories(...)

```python
s3 = s2.cat.set_categories(list(reversed(s1)))
```

### Step 3: Assign h1 = hash_pandas_object(...)

```python
h1 = hash_pandas_object(s1, categorize=categorize)
```

### Step 4: Assign h2 = hash_pandas_object(...)

```python
h2 = hash_pandas_object(s2, categorize=categorize)
```

### Step 5: Assign h3 = hash_pandas_object(...)

```python
h3 = hash_pandas_object(s3, categorize=categorize)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(h1, h2)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(h1, h3)
```


## Complete Example

```python
# Setup
# Fixtures: s1, categorize

# Workflow
s2 = s1.astype('category').cat.set_categories(s1)
s3 = s2.cat.set_categories(list(reversed(s1)))
h1 = hash_pandas_object(s1, categorize=categorize)
h2 = hash_pandas_object(s2, categorize=categorize)
h3 = hash_pandas_object(s3, categorize=categorize)
tm.assert_series_equal(h1, h2)
tm.assert_series_equal(h1, h3)
```

## Next Steps


---

*Source: test_hashing.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*