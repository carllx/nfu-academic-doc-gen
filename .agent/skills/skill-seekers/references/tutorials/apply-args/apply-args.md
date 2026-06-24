# How To: Apply Args

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test apply args

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `warnings`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.frame.common`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: float_frame, axis, raw, engine, request
```

## Step-by-Step Guide

### Step 1: Assign result = float_frame.apply(...)

```python
result = float_frame.apply(lambda x, y: x + y, axis, args=(1,), raw=raw, engine=engine)
```

### Step 2: Assign expected = value

```python
expected = float_frame + 1
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 4: Assign numba = pytest.importorskip(...)

```python
numba = pytest.importorskip('numba')
```

### Step 5: Assign mark = pytest.mark.xfail(...)

```python
mark = pytest.mark.xfail(reason="numba engine doesn't support args")
```

### Step 6: Call request.node.add_marker()

```python
request.node.add_marker(mark)
```

### Step 7: Call pytest.skip()

```python
pytest.skip(f'Segfaults on ARM platforms with numba {numba.__version__}')
```


## Complete Example

```python
# Setup
# Fixtures: float_frame, axis, raw, engine, request

# Workflow
if engine == 'numba':
    numba = pytest.importorskip('numba')
    if Version(numba.__version__) == Version('0.61') and is_platform_arm():
        pytest.skip(f'Segfaults on ARM platforms with numba {numba.__version__}')
    mark = pytest.mark.xfail(reason="numba engine doesn't support args")
    request.node.add_marker(mark)
result = float_frame.apply(lambda x, y: x + y, axis, args=(1,), raw=raw, engine=engine)
expected = float_frame + 1
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_frame_apply.py:69 | Complexity: Intermediate | Last updated: 2026-06-02*