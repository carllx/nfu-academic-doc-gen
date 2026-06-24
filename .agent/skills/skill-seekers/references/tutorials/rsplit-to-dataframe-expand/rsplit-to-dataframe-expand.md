# How To: Rsplit To Dataframe Expand

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rsplit to dataframe expand

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas.tests.strings`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['some_equal_splits', 'with_no_nans'], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.rsplit(...)

```python
result = s.str.rsplit('_', expand=True)
```

### Step 3: Assign exp = DataFrame(...)

```python
exp = DataFrame({0: ['some', 'with'], 1: ['equal', 'no'], 2: ['splits', 'nans']}, dtype=any_string_dtype)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```

### Step 5: Assign result = s.str.rsplit(...)

```python
result = s.str.rsplit('_', expand=True, n=2)
```

### Step 6: Assign exp = DataFrame(...)

```python
exp = DataFrame({0: ['some', 'with'], 1: ['equal', 'no'], 2: ['splits', 'nans']}, dtype=any_string_dtype)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```

### Step 8: Assign result = s.str.rsplit(...)

```python
result = s.str.rsplit('_', expand=True, n=1)
```

### Step 9: Assign exp = DataFrame(...)

```python
exp = DataFrame({0: ['some_equal', 'with_no'], 1: ['splits', 'nans']}, dtype=any_string_dtype)
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, exp)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['some_equal_splits', 'with_no_nans'], dtype=any_string_dtype)
result = s.str.rsplit('_', expand=True)
exp = DataFrame({0: ['some', 'with'], 1: ['equal', 'no'], 2: ['splits', 'nans']}, dtype=any_string_dtype)
tm.assert_frame_equal(result, exp)
result = s.str.rsplit('_', expand=True, n=2)
exp = DataFrame({0: ['some', 'with'], 1: ['equal', 'no'], 2: ['splits', 'nans']}, dtype=any_string_dtype)
tm.assert_frame_equal(result, exp)
result = s.str.rsplit('_', expand=True, n=1)
exp = DataFrame({0: ['some_equal', 'with_no'], 1: ['splits', 'nans']}, dtype=any_string_dtype)
tm.assert_frame_equal(result, exp)
```

## Next Steps


---

*Source: test_split_partition.py:315 | Complexity: Advanced | Last updated: 2026-06-02*