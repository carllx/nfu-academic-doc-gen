# How To: Series Equal Exact For Nonnumeric

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series equal exact for nonnumeric

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s1 = Series(...)

```python
s1 = Series(['a', 'b'])
```

### Step 2: Assign s2 = Series(...)

```python
s2 = Series(['a', 'b'])
```

### Step 3: Assign s3 = Series(...)

```python
s3 = Series(['b', 'a'])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1, s2, check_exact=True)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s2, s1, check_exact=True)
```

### Step 6: Assign msg = 'Series are different\n\nSeries values are different \\(100\\.0 %\\)\n\\[index\\]: \\[0, 1\\]\n\\[left\\]:  \\[a, b\\]\n\\[right\\]: \\[b, a\\]'

```python
msg = 'Series are different\n\nSeries values are different \\(100\\.0 %\\)\n\\[index\\]: \\[0, 1\\]\n\\[left\\]:  \\[a, b\\]\n\\[right\\]: \\[b, a\\]'
```

### Step 7: Assign msg = 'Series are different\n\nSeries values are different \\(100\\.0 %\\)\n\\[index\\]: \\[0, 1\\]\n\\[left\\]:  \\[b, a\\]\n\\[right\\]: \\[a, b\\]'

```python
msg = 'Series are different\n\nSeries values are different \\(100\\.0 %\\)\n\\[index\\]: \\[0, 1\\]\n\\[left\\]:  \\[b, a\\]\n\\[right\\]: \\[a, b\\]'
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s1, s3, check_exact=True)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s3, s1, check_exact=True)
```


## Complete Example

```python
# Workflow
s1 = Series(['a', 'b'])
s2 = Series(['a', 'b'])
s3 = Series(['b', 'a'])
tm.assert_series_equal(s1, s2, check_exact=True)
tm.assert_series_equal(s2, s1, check_exact=True)
msg = 'Series are different\n\nSeries values are different \\(100\\.0 %\\)\n\\[index\\]: \\[0, 1\\]\n\\[left\\]:  \\[a, b\\]\n\\[right\\]: \\[b, a\\]'
with pytest.raises(AssertionError, match=msg):
    tm.assert_series_equal(s1, s3, check_exact=True)
msg = 'Series are different\n\nSeries values are different \\(100\\.0 %\\)\n\\[index\\]: \\[0, 1\\]\n\\[left\\]:  \\[b, a\\]\n\\[right\\]: \\[a, b\\]'
with pytest.raises(AssertionError, match=msg):
    tm.assert_series_equal(s3, s1, check_exact=True)
```

## Next Steps


---

*Source: test_assert_series_equal.py:328 | Complexity: Advanced | Last updated: 2026-06-02*