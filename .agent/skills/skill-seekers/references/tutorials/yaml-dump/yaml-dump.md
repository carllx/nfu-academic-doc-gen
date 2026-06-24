# How To: Yaml Dump

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test yaml dump

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `array`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.util.version`
- `sklearn`
- `dask.array`
- `xarray`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign yaml = pytest.importorskip(...)

```python
yaml = pytest.importorskip('yaml')
```

### Step 2: Assign dumped = yaml.dump(...)

```python
dumped = yaml.dump(df)
```

### Step 3: Assign loaded = yaml.load(...)

```python
loaded = yaml.load(dumped, Loader=yaml.Loader)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, loaded)
```

### Step 5: Assign loaded2 = yaml.load(...)

```python
loaded2 = yaml.load(dumped, Loader=yaml.UnsafeLoader)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, loaded2)
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
yaml = pytest.importorskip('yaml')
dumped = yaml.dump(df)
loaded = yaml.load(dumped, Loader=yaml.Loader)
tm.assert_frame_equal(df, loaded)
loaded2 = yaml.load(dumped, Loader=yaml.UnsafeLoader)
tm.assert_frame_equal(df, loaded2)
```

## Next Steps


---

*Source: test_downstream.py:177 | Complexity: Intermediate | Last updated: 2026-06-02*