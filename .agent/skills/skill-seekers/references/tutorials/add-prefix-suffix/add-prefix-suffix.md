# How To: Add Prefix Suffix

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test add prefix suffix

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: string_series
```

## Step-by-Step Guide

### Step 1: Assign with_prefix = string_series.add_prefix(...)

```python
with_prefix = string_series.add_prefix('foo#')
```

### Step 2: Assign expected = Index(...)

```python
expected = Index([f'foo#{c}' for c in string_series.index])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(with_prefix.index, expected)
```

### Step 4: Assign with_suffix = string_series.add_suffix(...)

```python
with_suffix = string_series.add_suffix('#foo')
```

### Step 5: Assign expected = Index(...)

```python
expected = Index([f'{c}#foo' for c in string_series.index])
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(with_suffix.index, expected)
```

### Step 7: Assign with_pct_prefix = string_series.add_prefix(...)

```python
with_pct_prefix = string_series.add_prefix('%')
```

### Step 8: Assign expected = Index(...)

```python
expected = Index([f'%{c}' for c in string_series.index])
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(with_pct_prefix.index, expected)
```

### Step 10: Assign with_pct_suffix = string_series.add_suffix(...)

```python
with_pct_suffix = string_series.add_suffix('%')
```

### Step 11: Assign expected = Index(...)

```python
expected = Index([f'{c}%' for c in string_series.index])
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(with_pct_suffix.index, expected)
```


## Complete Example

```python
# Setup
# Fixtures: string_series

# Workflow
with_prefix = string_series.add_prefix('foo#')
expected = Index([f'foo#{c}' for c in string_series.index])
tm.assert_index_equal(with_prefix.index, expected)
with_suffix = string_series.add_suffix('#foo')
expected = Index([f'{c}#foo' for c in string_series.index])
tm.assert_index_equal(with_suffix.index, expected)
with_pct_prefix = string_series.add_prefix('%')
expected = Index([f'%{c}' for c in string_series.index])
tm.assert_index_equal(with_pct_prefix.index, expected)
with_pct_suffix = string_series.add_suffix('%')
expected = Index([f'{c}%' for c in string_series.index])
tm.assert_index_equal(with_pct_suffix.index, expected)
```

## Next Steps


---

*Source: test_add_prefix_suffix.py:7 | Complexity: Advanced | Last updated: 2026-06-02*