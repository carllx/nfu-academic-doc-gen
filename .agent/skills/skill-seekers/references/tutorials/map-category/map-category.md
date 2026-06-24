# How To: Map Category

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map category

## Prerequisites

**Required Modules:**
- `collections`
- `decimal`
- `math`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = Series(...)

```python
a = Series([1, 2, 3, 4])
```

### Step 2: Assign b = Series(...)

```python
b = Series(['even', 'odd', 'even', 'odd'], dtype='category')
```

### Step 3: Assign c = Series(...)

```python
c = Series(['even', 'odd', 'even', 'odd'])
```

### Step 4: Assign exp = Series(...)

```python
exp = Series(['odd', 'even', 'odd', np.nan], dtype='category')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(a.map(b), exp)
```

### Step 6: Assign exp = Series(...)

```python
exp = Series(['odd', 'even', 'odd', np.nan])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(a.map(c), exp)
```


## Complete Example

```python
# Workflow
a = Series([1, 2, 3, 4])
b = Series(['even', 'odd', 'even', 'odd'], dtype='category')
c = Series(['even', 'odd', 'even', 'odd'])
exp = Series(['odd', 'even', 'odd', np.nan], dtype='category')
tm.assert_series_equal(a.map(b), exp)
exp = Series(['odd', 'even', 'odd', np.nan])
tm.assert_series_equal(a.map(c), exp)
```

## Next Steps


---

*Source: test_map.py:184 | Complexity: Intermediate | Last updated: 2026-06-02*