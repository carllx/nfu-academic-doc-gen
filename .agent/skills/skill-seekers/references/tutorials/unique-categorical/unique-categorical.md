# How To: Unique Categorical

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unique categorical

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical([])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(cat)
```

### Step 3: Assign result = ser.unique(...)

```python
result = ser.unique()
```

### Step 4: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, cat)
```

### Step 5: Assign cat = Categorical(...)

```python
cat = Categorical([np.nan])
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(cat)
```

### Step 7: Assign result = ser.unique(...)

```python
result = ser.unique()
```

### Step 8: Call tm.assert_categorical_equal()

```python
tm.assert_categorical_equal(result, cat)
```


## Complete Example

```python
# Workflow
cat = Categorical([])
ser = Series(cat)
result = ser.unique()
tm.assert_categorical_equal(result, cat)
cat = Categorical([np.nan])
ser = Series(cat)
result = ser.unique()
tm.assert_categorical_equal(result, cat)
```

## Next Steps


---

*Source: test_unique.py:50 | Complexity: Advanced | Last updated: 2026-06-02*