# How To: Join Empty Uncomparable Columns

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test join empty uncomparable columns

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame()
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame(columns=['test'])
```

### Step 3: Assign df3 = DataFrame(...)

```python
df3 = DataFrame(columns=['foo', ('bar', 'baz')])
```

### Step 4: Assign result = value

```python
result = df1 + df2
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=['test'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = df2 + df3
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=[('bar', 'baz'), 'foo', 'test'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = value

```python
result = df1 + df3
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame(columns=[('bar', 'baz'), 'foo'])
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df1 = DataFrame()
df2 = DataFrame(columns=['test'])
df3 = DataFrame(columns=['foo', ('bar', 'baz')])
result = df1 + df2
expected = DataFrame(columns=['test'])
tm.assert_frame_equal(result, expected)
result = df2 + df3
expected = DataFrame(columns=[('bar', 'baz'), 'foo', 'test'])
tm.assert_frame_equal(result, expected)
result = df1 + df3
expected = DataFrame(columns=[('bar', 'baz'), 'foo'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_join.py:1051 | Complexity: Advanced | Last updated: 2026-06-02*