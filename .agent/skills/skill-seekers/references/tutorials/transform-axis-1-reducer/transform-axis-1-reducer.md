# How To: Transform Axis 1 Reducer

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test transform axis 1 reducer

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`

**Setup Required:**
```python
# Fixtures: request, reduction_func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}, index=['x', 'y'])
```

### Step 2: Assign msg = 'DataFrame.groupby with axis=1 is deprecated'

```python
msg = 'DataFrame.groupby with axis=1 is deprecated'
```

### Step 3: Assign result = gb.transform(...)

```python
result = gb.transform(reduction_func)
```

### Step 4: Assign expected = value

```python
expected = df.T.groupby([0, 0, 1]).transform(reduction_func).T
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign marker = pytest.mark.xfail(...)

```python
marker = pytest.mark.xfail(reason='transform incorrectly fails - GH#45986')
```

### Step 7: Call request.applymarker()

```python
request.applymarker(marker)
```

### Step 8: Assign gb = df.groupby(...)

```python
gb = df.groupby([0, 0, 1], axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: request, reduction_func

# Workflow
if reduction_func in ('corrwith', 'ngroup', 'nth'):
    marker = pytest.mark.xfail(reason='transform incorrectly fails - GH#45986')
    request.applymarker(marker)
df = DataFrame({'a': [1, 2], 'b': [3, 4], 'c': [5, 6]}, index=['x', 'y'])
msg = 'DataFrame.groupby with axis=1 is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    gb = df.groupby([0, 0, 1], axis=1)
result = gb.transform(reduction_func)
expected = df.T.groupby([0, 0, 1]).transform(reduction_func).T
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_transform.py:213 | Complexity: Advanced | Last updated: 2026-06-02*