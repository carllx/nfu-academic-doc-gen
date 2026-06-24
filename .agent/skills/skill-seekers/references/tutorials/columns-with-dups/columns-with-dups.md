# How To: Columns With Dups

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test columns with dups

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2]], columns=['a', 'a'])
```

### Step 2: Assign df.columns = value

```python
df.columns = ['a', 'a.1']
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2]], columns=['a', 'a.1'])
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame([[1, 2, 3]], columns=['b', 'a', 'a'])
```

### Step 6: Assign df.columns = value

```python
df.columns = ['b', 'a', 'a.1']
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1, 2, 3]], columns=['b', 'a', 'a.1'])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1, 2]], columns=['a', 'a'])
df.columns = ['a', 'a.1']
expected = DataFrame([[1, 2]], columns=['a', 'a.1'])
tm.assert_frame_equal(df, expected)
df = DataFrame([[1, 2, 3]], columns=['b', 'a', 'a'])
df.columns = ['b', 'a', 'a.1']
expected = DataFrame([[1, 2, 3]], columns=['b', 'a', 'a.1'])
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_nonunique_indexes.py:248 | Complexity: Advanced | Last updated: 2026-06-02*