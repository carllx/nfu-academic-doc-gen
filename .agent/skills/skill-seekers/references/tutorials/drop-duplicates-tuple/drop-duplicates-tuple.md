# How To: Drop Duplicates Tuple

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop duplicates tuple

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({('AA', 'AB'): ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'bar', 'foo'], 'B': ['one', 'one', 'two', 'two', 'two', 'two', 'one', 'two'], 'C': [1, 1, 2, 2, 2, 2, 1, 2], 'D': range(8)})
```

**Verification:**
```python
assert len(result) == 0
```

### Step 2: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates(('AA', 'AB'))
```

### Step 3: Assign expected = value

```python
expected = df[:2]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates(('AA', 'AB'), keep='last')
```

### Step 6: Assign expected = value

```python
expected = df.loc[[6, 7]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates(('AA', 'AB'), keep=False)
```

### Step 9: Assign expected = value

```python
expected = df.loc[[]]
```

**Verification:**
```python
assert len(result) == 0
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign expected = value

```python
expected = df.loc[[0, 1, 2, 3]]
```

### Step 12: Assign result = df.drop_duplicates(...)

```python
result = df.drop_duplicates((('AA', 'AB'), 'B'))
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({('AA', 'AB'): ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'bar', 'foo'], 'B': ['one', 'one', 'two', 'two', 'two', 'two', 'one', 'two'], 'C': [1, 1, 2, 2, 2, 2, 1, 2], 'D': range(8)})
result = df.drop_duplicates(('AA', 'AB'))
expected = df[:2]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates(('AA', 'AB'), keep='last')
expected = df.loc[[6, 7]]
tm.assert_frame_equal(result, expected)
result = df.drop_duplicates(('AA', 'AB'), keep=False)
expected = df.loc[[]]
assert len(result) == 0
tm.assert_frame_equal(result, expected)
expected = df.loc[[0, 1, 2, 3]]
result = df.drop_duplicates((('AA', 'AB'), 'B'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_drop_duplicates.py:169 | Complexity: Advanced | Last updated: 2026-06-02*