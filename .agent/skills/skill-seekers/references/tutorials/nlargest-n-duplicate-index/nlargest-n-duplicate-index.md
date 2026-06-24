# How To: Nlargest N Duplicate Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nlargest n duplicate index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: df_duplicates, n, order, request
```

## Step-by-Step Guide

### Step 1: Assign df = df_duplicates

```python
df = df_duplicates
```

### Step 2: Assign result = df.nsmallest(...)

```python
result = df.nsmallest(n, order)
```

### Step 3: Assign expected = df.sort_values.head(...)

```python
expected = df.sort_values(order).head(n)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = df.nlargest(...)

```python
result = df.nlargest(n, order)
```

### Step 6: Assign expected = df.sort_values.head(...)

```python
expected = df.sort_values(order, ascending=False).head(n)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='pandas default unstable sorting of duplicatesissue with numpy>=1.25 with AVX instructions', strict=False))
```


## Complete Example

```python
# Setup
# Fixtures: df_duplicates, n, order, request

# Workflow
df = df_duplicates
result = df.nsmallest(n, order)
expected = df.sort_values(order).head(n)
tm.assert_frame_equal(result, expected)
result = df.nlargest(n, order)
expected = df.sort_values(order, ascending=False).head(n)
if Version(np.__version__) >= Version('1.25') and (order == ['a'] and n in (1, 2, 3, 4) or (order == ['a', 'b'] and n == 5)):
    request.applymarker(pytest.mark.xfail(reason='pandas default unstable sorting of duplicatesissue with numpy>=1.25 with AVX instructions', strict=False))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_nlargest.py:159 | Complexity: Advanced | Last updated: 2026-06-02*