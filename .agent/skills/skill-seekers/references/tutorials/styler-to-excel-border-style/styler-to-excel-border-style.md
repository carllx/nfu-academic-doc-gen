# How To: Styler To Excel Border Style

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test styler to excel border style

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `time`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.excel`
- `pandas.io.formats.excel`

**Setup Required:**
```python
# Fixtures: engine, border_style
```

## Step-by-Step Guide

### Step 1: Assign css = value

```python
css = f'border-left: {border_style} black thin'
```

**Verification:**
```python
assert u_cell is None or u_cell != expected[engine]
```

### Step 2: Assign attrs = value

```python
attrs = ['border', 'left', 'style']
```

**Verification:**
```python
assert s_cell == expected[engine]
```

### Step 3: Assign expected = border_style

```python
expected = border_style
```

**Verification:**
```python
assert u_cell is None or u_cell != expected
```

### Step 4: Call pytest.importorskip()

```python
pytest.importorskip(engine)
```

**Verification:**
```python
assert s_cell == expected
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((1, 1)))
```

### Step 6: Assign styler = df.style.map(...)

```python
styler = df.style.map(lambda x: css)
```

### Step 7: Assign openpyxl = pytest.importorskip(...)

```python
openpyxl = pytest.importorskip('openpyxl')
```

### Step 8: Call df.to_excel()

```python
df.to_excel(writer, sheet_name='dataframe')
```

### Step 9: Call styler.to_excel()

```python
styler.to_excel(writer, sheet_name='styled')
```

### Step 10: Assign unknown = value

```python
u_cell, s_cell = (wb['dataframe'].cell(2, 2), wb['styled'].cell(2, 2))
```

### Step 11: Assign unknown = value

```python
u_cell, s_cell = (getattr(u_cell, attr, None), getattr(s_cell, attr))
```

**Verification:**
```python
assert u_cell is None or u_cell != expected[engine]
```


## Complete Example

```python
# Setup
# Fixtures: engine, border_style

# Workflow
css = f'border-left: {border_style} black thin'
attrs = ['border', 'left', 'style']
expected = border_style
pytest.importorskip(engine)
df = DataFrame(np.random.default_rng(2).standard_normal((1, 1)))
styler = df.style.map(lambda x: css)
with tm.ensure_clean('.xlsx') as path:
    with ExcelWriter(path, engine=engine) as writer:
        df.to_excel(writer, sheet_name='dataframe')
        styler.to_excel(writer, sheet_name='styled')
    openpyxl = pytest.importorskip('openpyxl')
    with contextlib.closing(openpyxl.load_workbook(path)) as wb:
        u_cell, s_cell = (wb['dataframe'].cell(2, 2), wb['styled'].cell(2, 2))
    for attr in attrs:
        u_cell, s_cell = (getattr(u_cell, attr, None), getattr(s_cell, attr))
    if isinstance(expected, dict):
        assert u_cell is None or u_cell != expected[engine]
        assert s_cell == expected[engine]
    else:
        assert u_cell is None or u_cell != expected
        assert s_cell == expected
```

## Next Steps


---

*Source: test_style.py:231 | Complexity: Advanced | Last updated: 2026-06-02*