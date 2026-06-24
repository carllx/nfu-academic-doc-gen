# How To: Series Equal Categorical Values Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series equal categorical values mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: rtol, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign dtype = value

```python
dtype = 'str' if using_infer_string else 'object'
```

### Step 2: Assign msg = value

```python
msg = f"Series are different\n\nSeries values are different \\(66\\.66667 %\\)\n\\[index\\]: \\[0, 1, 2\\]\n\\[left\\]:  \\['a', 'b', 'c'\\]\nCategories \\(3, {dtype}\\): \\['a', 'b', 'c'\\]\n\\[right\\]: \\['a', 'c', 'b'\\]\nCategories \\(3, {dtype}\\): \\['a', 'b', 'c'\\]"
```

### Step 3: Assign s1 = Series(...)

```python
s1 = Series(Categorical(['a', 'b', 'c']))
```

### Step 4: Assign s2 = Series(...)

```python
s2 = Series(Categorical(['a', 'c', 'b']))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1, s2, rtol=rtol)
```


## Complete Example

```python
# Setup
# Fixtures: rtol, using_infer_string

# Workflow
dtype = 'str' if using_infer_string else 'object'
msg = f"Series are different\n\nSeries values are different \\(66\\.66667 %\\)\n\\[index\\]: \\[0, 1, 2\\]\n\\[left\\]:  \\['a', 'b', 'c'\\]\nCategories \\(3, {dtype}\\): \\['a', 'b', 'c'\\]\n\\[right\\]: \\['a', 'c', 'b'\\]\nCategories \\(3, {dtype}\\): \\['a', 'b', 'c'\\]"
s1 = Series(Categorical(['a', 'b', 'c']))
s2 = Series(Categorical(['a', 'c', 'b']))
with pytest.raises(AssertionError, match=msg):
    tm.assert_series_equal(s1, s2, rtol=rtol)
```

## Next Steps


---

*Source: test_assert_series_equal.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*