# How To: Styler To Excel Basic Indexes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test styler to excel basic indexes

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
# Fixtures: engine, css, attrs, expected
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip(engine)
```

**Verification:**
```python
assert ui_cell is None or ui_cell != expected[engine]
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.random.default_rng(2).standard_normal((1, 1)))
```

**Verification:**
```python
assert si_cell == expected[engine]
```

### Step 3: Assign styler = value

```python
styler = df.style
```

**Verification:**
```python
assert uc_cell is None or uc_cell != expected[engine]
```

### Step 4: Call styler.map_index()

```python
styler.map_index(lambda x: css, axis=0)
```

**Verification:**
```python
assert sc_cell == expected[engine]
```

### Step 5: Call styler.map_index()

```python
styler.map_index(lambda x: css, axis=1)
```

**Verification:**
```python
assert ui_cell is None or ui_cell != expected
```

### Step 6: Assign null_styler = value

```python
null_styler = df.style
```

**Verification:**
```python
assert si_cell == expected
```

### Step 7: Call null_styler.map()

```python
null_styler.map(lambda x: 'null: css;')
```

**Verification:**
```python
assert uc_cell is None or uc_cell != expected
```

### Step 8: Call null_styler.map_index()

```python
null_styler.map_index(lambda x: 'null: css;', axis=0)
```

**Verification:**
```python
assert sc_cell == expected
```

### Step 9: Call null_styler.map_index()

```python
null_styler.map_index(lambda x: 'null: css;', axis=1)
```

### Step 10: Assign openpyxl = pytest.importorskip(...)

```python
openpyxl = pytest.importorskip('openpyxl')
```

### Step 11: Call null_styler.to_excel()

```python
null_styler.to_excel(writer, sheet_name='null_styled')
```

### Step 12: Call styler.to_excel()

```python
styler.to_excel(writer, sheet_name='styled')
```

### Step 13: Assign unknown = value

```python
ui_cell, si_cell = (wb['null_styled'].cell(2, 1), wb['styled'].cell(2, 1))
```

### Step 14: Assign unknown = value

```python
uc_cell, sc_cell = (wb['null_styled'].cell(1, 2), wb['styled'].cell(1, 2))
```

### Step 15: Assign unknown = value

```python
ui_cell, si_cell = (getattr(ui_cell, attr, None), getattr(si_cell, attr))
```

### Step 16: Assign unknown = value

```python
uc_cell, sc_cell = (getattr(uc_cell, attr, None), getattr(sc_cell, attr))
```

**Verification:**
```python
assert ui_cell is None or ui_cell != expected[engine]
```


## Complete Example

```python
# Setup
# Fixtures: engine, css, attrs, expected

# Workflow
pytest.importorskip(engine)
df = DataFrame(np.random.default_rng(2).standard_normal((1, 1)))
styler = df.style
styler.map_index(lambda x: css, axis=0)
styler.map_index(lambda x: css, axis=1)
null_styler = df.style
null_styler.map(lambda x: 'null: css;')
null_styler.map_index(lambda x: 'null: css;', axis=0)
null_styler.map_index(lambda x: 'null: css;', axis=1)
with tm.ensure_clean('.xlsx') as path:
    with ExcelWriter(path, engine=engine) as writer:
        null_styler.to_excel(writer, sheet_name='null_styled')
        styler.to_excel(writer, sheet_name='styled')
    openpyxl = pytest.importorskip('openpyxl')
    with contextlib.closing(openpyxl.load_workbook(path)) as wb:
        ui_cell, si_cell = (wb['null_styled'].cell(2, 1), wb['styled'].cell(2, 1))
        uc_cell, sc_cell = (wb['null_styled'].cell(1, 2), wb['styled'].cell(1, 2))
    for attr in attrs:
        ui_cell, si_cell = (getattr(ui_cell, attr, None), getattr(si_cell, attr))
        uc_cell, sc_cell = (getattr(uc_cell, attr, None), getattr(sc_cell, attr))
    if isinstance(expected, dict):
        assert ui_cell is None or ui_cell != expected[engine]
        assert si_cell == expected[engine]
        assert uc_cell is None or uc_cell != expected[engine]
        assert sc_cell == expected[engine]
    else:
        assert ui_cell is None or ui_cell != expected
        assert si_cell == expected
        assert uc_cell is None or uc_cell != expected
        assert sc_cell == expected
```

## Next Steps


---

*Source: test_style.py:166 | Complexity: Advanced | Last updated: 2026-06-02*