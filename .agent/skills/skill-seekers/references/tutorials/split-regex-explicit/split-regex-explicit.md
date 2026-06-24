# How To: Split Regex Explicit

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test split regex explicit

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

### Step 1: Assign regex_pat = re.compile(...)

```python
regex_pat = re.compile('.jpg')
```

### Step 2: Assign values = Series(...)

```python
values = Series('xxxjpgzzz.jpg', dtype=any_string_dtype)
```

### Step 3: Assign result = values.str.split(...)

```python
result = values.str.split(regex_pat)
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([['xx', 'zzz', '']])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 6: Assign result = values.str.split(...)

```python
result = values.str.split('\\.jpg', regex=False)
```

### Step 7: Assign exp = Series(...)

```python
exp = Series([['xxxjpgzzz.jpg']])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 9: Assign result = values.str.split(...)

```python
result = values.str.split('.')
```

### Step 10: Assign exp = Series(...)

```python
exp = Series([['xxxjpgzzz', 'jpg']])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 12: Assign result = values.str.split(...)

```python
result = values.str.split('.jpg')
```

### Step 13: Assign exp = Series(...)

```python
exp = Series([['xx', 'zzz', '']])
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 15: Call values.str.split()

```python
values.str.split(regex_pat, regex=False)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
regex_pat = re.compile('.jpg')
values = Series('xxxjpgzzz.jpg', dtype=any_string_dtype)
result = values.str.split(regex_pat)
exp = Series([['xx', 'zzz', '']])
tm.assert_series_equal(result, exp)
result = values.str.split('\\.jpg', regex=False)
exp = Series([['xxxjpgzzz.jpg']])
tm.assert_series_equal(result, exp)
result = values.str.split('.')
exp = Series([['xxxjpgzzz', 'jpg']])
tm.assert_series_equal(result, exp)
result = values.str.split('.jpg')
exp = Series([['xx', 'zzz', '']])
tm.assert_series_equal(result, exp)
with pytest.raises(ValueError, match='Cannot use a compiled regex as replacement pattern with regex=False'):
    values.str.split(regex_pat, regex=False)
```

## Next Steps


---

*Source: test_split_partition.py:62 | Complexity: Advanced | Last updated: 2026-06-02*