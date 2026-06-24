# How To: Update From Non Df

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test update from non df

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign d = value

```python
d = {'a': Series([1, 2, 3, 4]), 'b': Series([5, 6, 7, 8])}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(d)
```

### Step 3: Assign unknown = Series(...)

```python
d['a'] = Series([5, 6, 7, 8])
```

### Step 4: Call df.update()

```python
df.update(d)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(d)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 7: Assign d = value

```python
d = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]}
```

### Step 8: Assign df = DataFrame(...)

```python
df = DataFrame(d)
```

### Step 9: Assign unknown = value

```python
d['a'] = [5, 6, 7, 8]
```

### Step 10: Call df.update()

```python
df.update(d)
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame(d)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```


## Complete Example

```python
# Workflow
d = {'a': Series([1, 2, 3, 4]), 'b': Series([5, 6, 7, 8])}
df = DataFrame(d)
d['a'] = Series([5, 6, 7, 8])
df.update(d)
expected = DataFrame(d)
tm.assert_frame_equal(df, expected)
d = {'a': [1, 2, 3, 4], 'b': [5, 6, 7, 8]}
df = DataFrame(d)
d['a'] = [5, 6, 7, 8]
df.update(d)
expected = DataFrame(d)
tm.assert_frame_equal(df, expected)
```

## Next Steps


---

*Source: test_update.py:116 | Complexity: Advanced | Last updated: 2026-06-02*