# How To: Categorical Index Upcast

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test categorical index upcast

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = DataFrame(...)

```python
a = DataFrame({'foo': [1, 2]}, index=Categorical(['foo', 'bar']))
```

### Step 2: Assign b = DataFrame(...)

```python
b = DataFrame({'foo': [4, 3]}, index=Categorical(['baz', 'bar']))
```

### Step 3: Assign res = pd.concat(...)

```python
res = pd.concat([a, b])
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame({'foo': [1, 2, 4, 3]}, index=['foo', 'bar', 'baz', 'bar'])
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(res, exp)
```

### Step 6: Assign a = Series(...)

```python
a = Series([1, 2], index=Categorical(['foo', 'bar']))
```

### Step 7: Assign b = Series(...)

```python
b = Series([4, 3], index=Categorical(['baz', 'bar']))
```

### Step 8: Assign res = pd.concat(...)

```python
res = pd.concat([a, b])
```

### Step 9: Assign exp = Series(...)

```python
exp = Series([1, 2, 4, 3], index=['foo', 'bar', 'baz', 'bar'])
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(res, exp)
```


## Complete Example

```python
# Workflow
a = DataFrame({'foo': [1, 2]}, index=Categorical(['foo', 'bar']))
b = DataFrame({'foo': [4, 3]}, index=Categorical(['baz', 'bar']))
res = pd.concat([a, b])
exp = DataFrame({'foo': [1, 2, 4, 3]}, index=['foo', 'bar', 'baz', 'bar'])
tm.assert_equal(res, exp)
a = Series([1, 2], index=Categorical(['foo', 'bar']))
b = Series([4, 3], index=Categorical(['baz', 'bar']))
res = pd.concat([a, b])
exp = Series([1, 2, 4, 3], index=['foo', 'bar', 'baz', 'bar'])
tm.assert_equal(res, exp)
```

## Next Steps


---

*Source: test_categorical.py:221 | Complexity: Advanced | Last updated: 2026-06-02*