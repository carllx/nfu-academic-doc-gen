# How To: Reindex Level Partial Selection

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex level partial selection

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
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

### Step 2: Assign result = frame.reindex(...)

```python
result = frame.reindex(['foo', 'qux'], level=0)
```

### Step 3: Assign expected = value

```python
expected = frame.iloc[[0, 1, 2, 7, 8, 9]]
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = frame.T.reindex(...)

```python
result = frame.T.reindex(['foo', 'qux'], axis=1, level=0)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected.T)
```

### Step 7: Assign result = value

```python
result = frame.loc[['foo', 'qux']]
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = value

```python
result = frame['A'].loc[['foo', 'qux']]
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected['A'])
```

### Step 11: Assign result = value

```python
result = frame.T.loc[:, ['foo', 'qux']]
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected.T)
```


## Complete Example

```python
# Setup
# Fixtures: multiindex_dataframe_random_data

# Workflow
frame = multiindex_dataframe_random_data
result = frame.reindex(['foo', 'qux'], level=0)
expected = frame.iloc[[0, 1, 2, 7, 8, 9]]
tm.assert_frame_equal(result, expected)
result = frame.T.reindex(['foo', 'qux'], axis=1, level=0)
tm.assert_frame_equal(result, expected.T)
result = frame.loc[['foo', 'qux']]
tm.assert_frame_equal(result, expected)
result = frame['A'].loc[['foo', 'qux']]
tm.assert_series_equal(result, expected['A'])
result = frame.T.loc[:, ['foo', 'qux']]
tm.assert_frame_equal(result, expected.T)
```

## Next Steps


---

*Source: test_multilevel.py:226 | Complexity: Advanced | Last updated: 2026-06-02*