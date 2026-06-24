# How To: Repr Max Columns Max Rows

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr max columns max rows

## Prerequisites

**Required Modules:**
- `datetime`
- `io`
- `pathlib`
- `re`
- `shutil`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas`
- `pandas`
- `pandas.io.formats`
- `pandas.io.formats.format`


## Step-by-Step Guide

### Step 1: Assign unknown = get_terminal_size(...)

```python
term_width, term_height = get_terminal_size()
```

**Verification:**
```python
assert not has_expanded_repr(mkframe(4))
```

### Step 2: Assign df6 = mkframe(...)

```python
df6 = mkframe(6)
```

**Verification:**
```python
assert not has_expanded_repr(mkframe(5))
```

### Step 3: Assign df10 = mkframe(...)

```python
df10 = mkframe(10)
```

**Verification:**
```python
assert not has_expanded_repr(df6)
```

### Step 4: Call pytest.skip()

```python
pytest.skip(f'terminal size too small, {term_width} x {term_height}')
```

**Verification:**
```python
assert has_doubly_truncated_repr(df6)
```

### Step 5: Assign index = value

```python
index = [f'{i:05d}' for i in range(n)]
```

**Verification:**
```python
assert not has_expanded_repr(df6)
```

### Step 6: Assign df = mkframe(...)

```python
df = mkframe(term_width // 7 - 2)
```

**Verification:**
```python
assert not has_truncated_repr(df6)
```

### Step 7: Assign df = mkframe(...)

```python
df = mkframe(term_width // 7 + 2)
```

**Verification:**
```python
assert not has_expanded_repr(df10)
```

### Step 8: Call printing.pprint_thing()

```python
printing.pprint_thing(df._repr_fits_horizontal_())
```

**Verification:**
```python
assert has_vertically_truncated_repr(df10)
```


## Complete Example

```python
# Workflow
term_width, term_height = get_terminal_size()
if term_width < 10 or term_height < 10:
    pytest.skip(f'terminal size too small, {term_width} x {term_height}')

def mkframe(n):
    index = [f'{i:05d}' for i in range(n)]
    return DataFrame(0, index, index)
df6 = mkframe(6)
df10 = mkframe(10)
with option_context('mode.sim_interactive', True):
    with option_context('display.width', term_width * 2):
        with option_context('display.max_rows', 5, 'display.max_columns', 5):
            assert not has_expanded_repr(mkframe(4))
            assert not has_expanded_repr(mkframe(5))
            assert not has_expanded_repr(df6)
            assert has_doubly_truncated_repr(df6)
        with option_context('display.max_rows', 20, 'display.max_columns', 10):
            assert not has_expanded_repr(df6)
            assert not has_truncated_repr(df6)
        with option_context('display.max_rows', 9, 'display.max_columns', 10):
            assert not has_expanded_repr(df10)
            assert has_vertically_truncated_repr(df10)
    with option_context('display.max_columns', 100, 'display.max_rows', term_width * 20, 'display.width', None):
        df = mkframe(term_width // 7 - 2)
        assert not has_expanded_repr(df)
        df = mkframe(term_width // 7 + 2)
        printing.pprint_thing(df._repr_fits_horizontal_())
        assert has_expanded_repr(df)
```

## Next Steps


---

*Source: test_format.py:340 | Complexity: Advanced | Last updated: 2026-06-02*