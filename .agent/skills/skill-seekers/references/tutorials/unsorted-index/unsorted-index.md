# How To: Unsorted Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unsorted index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `gc`
- `itertools`
- `re`
- `string`
- `weakref`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.api`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.plotting.common`
- `pandas.util.version`
- `pandas.io.formats.printing`
- `matplotlib.pyplot`
- `matplotlib.patches`
- `matplotlib.patches`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.pyplot`
- `matplotlib`
- `matplotlib.pyplot`
- `mpl_toolkits.axes_grid1`
- `mpl_toolkits.axes_grid1.inset_locator`

**Setup Required:**
```python
# Fixtures: index_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'y': np.arange(100)}, index=Index(np.arange(99, -1, -1), dtype=index_dtype), dtype=np.int64)
```

### Step 2: Assign ax = df.plot(...)

```python
ax = df.plot()
```

### Step 3: Assign lines = value

```python
lines = ax.get_lines()[0]
```

### Step 4: Assign rs = lines.get_xydata(...)

```python
rs = lines.get_xydata()
```

### Step 5: Assign rs = Series(...)

```python
rs = Series(rs[:, 1], rs[:, 0], dtype=np.int64, name='y')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, df.y, check_index_type=False)
```


## Complete Example

```python
# Setup
# Fixtures: index_dtype

# Workflow
df = DataFrame({'y': np.arange(100)}, index=Index(np.arange(99, -1, -1), dtype=index_dtype), dtype=np.int64)
ax = df.plot()
lines = ax.get_lines()[0]
rs = lines.get_xydata()
rs = Series(rs[:, 1], rs[:, 0], dtype=np.int64, name='y')
tm.assert_series_equal(rs, df.y, check_index_type=False)
```

## Next Steps


---

*Source: test_frame.py:455 | Complexity: Intermediate | Last updated: 2026-06-02*