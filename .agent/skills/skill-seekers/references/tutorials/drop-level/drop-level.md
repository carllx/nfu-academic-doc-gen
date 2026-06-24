# How To: Drop Level

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: multiindex_dataframe_random_data
```

## Step-by-Step Guide

### Step 1: Assign frame = multiindex_dataframe_random_data

```python
frame = multiindex_dataframe_random_data
```

### Step 2: Assign result = frame.drop(...)

```python
result = frame.drop(['bar', 'qux'], level='first')
```

### Step 3: Assign expected = value

```python
expected = frame.iloc[[0, 1, 2, 5, 6]]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = frame.drop(...)

```python
result = frame.drop(['two'], level='second')
```

### Step 6: Assign expected = value

```python
expected = frame.iloc[[0, 2, 3, 6, 7, 9]]
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = frame.T.drop(...)

```python
result = frame.T.drop(['bar', 'qux'], axis=1, level='first')
```

### Step 9: Assign expected = value

```python
expected = frame.iloc[[0, 1, 2, 5, 6]].T
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = frame.T.drop(...)

```python
result = frame.T.drop(['two'], axis=1, level='second')
```

### Step 12: Assign expected = value

```python
expected = frame.iloc[[0, 2, 3, 6, 7, 9]].T
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
result = frame.drop(['bar', 'qux'], level='first')
expected = frame.iloc[[0, 1, 2, 5, 6]]
tm.assert_frame_equal(result, expected)
result = frame.drop(['two'], level='second')
expected = frame.iloc[[0, 2, 3, 6, 7, 9]]
tm.assert_frame_equal(result, expected)
result = frame.T.drop(['bar', 'qux'], axis=1, level='first')
expected = frame.iloc[[0, 1, 2, 5, 6]].T
tm.assert_frame_equal(result, expected)
result = frame.T.drop(['two'], axis=1, level='second')
expected = frame.iloc[[0, 2, 3, 6, 7, 9]].T
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_drop.py:382 | Complexity: Advanced | Last updated: 2026-06-02*