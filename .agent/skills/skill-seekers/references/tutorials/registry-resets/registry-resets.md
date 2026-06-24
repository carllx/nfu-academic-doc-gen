# How To: Registry Resets

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test registry resets

## Prerequisites

**Required Modules:**
- `datetime`
- `subprocess`
- `sys`
- `numpy`
- `pytest`
- `pandas._config.config`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`
- `pandas.plotting`
- `pandas.tseries.offsets`
- `pandas.plotting._matplotlib`


## Step-by-Step Guide

### Step 1: Assign units = pytest.importorskip(...)

```python
units = pytest.importorskip('matplotlib.units')
```

**Verification:**
```python
assert units.registry[date] is not date_converter
```

### Step 2: Assign dates = pytest.importorskip(...)

```python
dates = pytest.importorskip('matplotlib.dates')
```

**Verification:**
```python
assert units.registry[date] is date_converter
```

### Step 3: Assign original = dict(...)

```python
original = dict(units.registry)
```

### Step 4: Call units.registry.clear()

```python
units.registry.clear()
```

### Step 5: Assign date_converter = dates.DateConverter(...)

```python
date_converter = dates.DateConverter()
```

### Step 6: Assign unknown = date_converter

```python
units.registry[datetime] = date_converter
```

### Step 7: Assign unknown = date_converter

```python
units.registry[date] = date_converter
```

### Step 8: Call register_matplotlib_converters()

```python
register_matplotlib_converters()
```

**Verification:**
```python
assert units.registry[date] is not date_converter
```

### Step 9: Call deregister_matplotlib_converters()

```python
deregister_matplotlib_converters()
```

**Verification:**
```python
assert units.registry[date] is date_converter
```

### Step 10: Call units.registry.clear()

```python
units.registry.clear()
```

### Step 11: Assign unknown = v

```python
units.registry[k] = v
```


## Complete Example

```python
# Workflow
units = pytest.importorskip('matplotlib.units')
dates = pytest.importorskip('matplotlib.dates')
original = dict(units.registry)
try:
    units.registry.clear()
    date_converter = dates.DateConverter()
    units.registry[datetime] = date_converter
    units.registry[date] = date_converter
    register_matplotlib_converters()
    assert units.registry[date] is not date_converter
    deregister_matplotlib_converters()
    assert units.registry[date] is date_converter
finally:
    units.registry.clear()
    for k, v in original.items():
        units.registry[k] = v
```

## Next Steps


---

*Source: test_converter.py:132 | Complexity: Advanced | Last updated: 2026-06-02*