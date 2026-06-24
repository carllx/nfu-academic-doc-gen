# How To: Arith Series With Scalar

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arith series with scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays.numpy_`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: data, all_arithmetic_operators, request
```

## Step-by-Step Guide

### Step 1: Assign opname = all_arithmetic_operators

```python
opname = all_arithmetic_operators
```

### Step 2: Assign series_scalar_exc = None

```python
series_scalar_exc = None
```

### Step 3: Assign self.series_scalar_exc = series_scalar_exc

```python
self.series_scalar_exc = series_scalar_exc
```

### Step 4: Call super.test_arith_series_with_scalar()

```python
super().test_arith_series_with_scalar(data, all_arithmetic_operators)
```

### Step 5: Assign series_scalar_exc = TypeError

```python
series_scalar_exc = TypeError
```

### Step 6: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason='the Series.combine step raises but not the Series method.')
```

### Step 7: Call request.node.add_marker()

```python
request.node.add_marker(mark)
```


## Complete Example

```python
# Setup
# Fixtures: data, all_arithmetic_operators, request

# Workflow
opname = all_arithmetic_operators
series_scalar_exc = None
if data.dtype.numpy_dtype == object:
    if opname in ['__mul__', '__rmul__']:
        mark = pytest.mark.xfail(reason='the Series.combine step raises but not the Series method.')
        request.node.add_marker(mark)
    series_scalar_exc = TypeError
self.series_scalar_exc = series_scalar_exc
super().test_arith_series_with_scalar(data, all_arithmetic_operators)
```

## Next Steps


---

*Source: test_numpy.py:260 | Complexity: Intermediate | Last updated: 2026-06-02*