# How To: Multiindex Complex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiindex complex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.index`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign complex_data = value

```python
complex_data = [1 + 2j, 4 - 3j, 10 - 1j]
```

### Step 2: Assign non_complex_data = value

```python
non_complex_data = [3, 4, 5]
```

### Step 3: Assign result = DataFrame(...)

```python
result = DataFrame({'x': complex_data, 'y': non_complex_data, 'z': non_complex_data})
```

### Step 4: Call result.set_index()

```python
result.set_index(['x', 'y'], inplace=True)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'z': non_complex_data}, index=MultiIndex.from_arrays([complex_data, non_complex_data], names=('x', 'y')))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
complex_data = [1 + 2j, 4 - 3j, 10 - 1j]
non_complex_data = [3, 4, 5]
result = DataFrame({'x': complex_data, 'y': non_complex_data, 'z': non_complex_data})
result.set_index(['x', 'y'], inplace=True)
expected = DataFrame({'z': non_complex_data}, index=MultiIndex.from_arrays([complex_data, non_complex_data], names=('x', 'y')))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multiindex.py:124 | Complexity: Intermediate | Last updated: 2026-06-02*