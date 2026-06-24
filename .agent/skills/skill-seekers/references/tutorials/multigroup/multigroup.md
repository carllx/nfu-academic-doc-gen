# How To: Multigroup

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multigroup

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: left, right
```

## Step-by-Step Guide

### Step 1: Assign left = pd.concat(...)

```python
left = pd.concat([left, left], ignore_index=True)
```

**Verification:**
```python
assert result['group'].notna().all()
```

### Step 2: Assign unknown = value

```python
left['group'] = ['a'] * 3 + ['b'] * 3
```

### Step 3: Assign result = merge_ordered(...)

```python
result = merge_ordered(left, right, on='key', left_by='group', fill_method='ffill')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'key': ['a', 'b', 'c', 'd', 'e', 'f'] * 2, 'lvalue': [1.0, 1, 2, 2, 3, 3.0] * 2, 'rvalue': [np.nan, 1, 2, 3, 3, 4] * 2})
```

### Step 5: Assign unknown = value

```python
expected['group'] = ['a'] * 6 + ['b'] * 6
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected.loc[:, result.columns])
```

### Step 7: Assign result2 = merge_ordered(...)

```python
result2 = merge_ordered(right, left, on='key', right_by='group', fill_method='ffill')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, result2.loc[:, result.columns])
```

### Step 9: Assign result = merge_ordered(...)

```python
result = merge_ordered(left, right, on='key', left_by='group')
```

**Verification:**
```python
assert result['group'].notna().all()
```


## Complete Example

```python
# Setup
# Fixtures: left, right

# Workflow
left = pd.concat([left, left], ignore_index=True)
left['group'] = ['a'] * 3 + ['b'] * 3
result = merge_ordered(left, right, on='key', left_by='group', fill_method='ffill')
expected = DataFrame({'key': ['a', 'b', 'c', 'd', 'e', 'f'] * 2, 'lvalue': [1.0, 1, 2, 2, 3, 3.0] * 2, 'rvalue': [np.nan, 1, 2, 3, 3, 4] * 2})
expected['group'] = ['a'] * 6 + ['b'] * 6
tm.assert_frame_equal(result, expected.loc[:, result.columns])
result2 = merge_ordered(right, left, on='key', right_by='group', fill_method='ffill')
tm.assert_frame_equal(result, result2.loc[:, result.columns])
result = merge_ordered(left, right, on='key', left_by='group')
assert result['group'].notna().all()
```

## Next Steps


---

*Source: test_merge_ordered.py:48 | Complexity: Advanced | Last updated: 2026-06-02*