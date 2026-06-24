# How To: Repr Truncates Terminal Size

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: mock, workflow, integration

## Overview

Workflow: test repr truncates terminal size

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: monkeypatch
```

## Step-by-Step Guide

### Step 1: Assign terminal_size = value

```python
terminal_size = (118, 96)
```

**Verification:**
```python
assert 'long' in h1
```

### Step 2: Call monkeypatch.setattr()

```python
monkeypatch.setattr('pandas.io.formats.format.get_terminal_size', lambda: terminal_size)
```

**Verification:**
```python
assert 'loooooonger' in h1
```

### Step 3: Assign index = range(...)

```python
index = range(5)
```

**Verification:**
```python
assert 'cat' in h2
```

### Step 4: Assign columns = MultiIndex.from_tuples(...)

```python
columns = MultiIndex.from_tuples([('This is a long title with > 37 chars.', 'cat'), ('This is a loooooonger title with > 43 chars.', 'dog')])
```

**Verification:**
```python
assert 'dog' in h2
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(1, index=index, columns=columns)
```

**Verification:**
```python
assert df2.columns[0] in result.split('\n')[0]
```

### Step 6: Assign result = repr(...)

```python
result = repr(df)
```

### Step 7: Assign unknown = value

```python
h1, h2 = result.split('\n')[:2]
```

**Verification:**
```python
assert 'long' in h1
```

### Step 8: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'A' * 41: [1, 2], 'B' * 41: [1, 2]})
```

### Step 9: Assign result = repr(...)

```python
result = repr(df2)
```

**Verification:**
```python
assert df2.columns[0] in result.split('\n')[0]
```


## Complete Example

```python
# Setup
# Fixtures: monkeypatch

# Workflow
terminal_size = (118, 96)
monkeypatch.setattr('pandas.io.formats.format.get_terminal_size', lambda: terminal_size)
index = range(5)
columns = MultiIndex.from_tuples([('This is a long title with > 37 chars.', 'cat'), ('This is a loooooonger title with > 43 chars.', 'dog')])
df = DataFrame(1, index=index, columns=columns)
result = repr(df)
h1, h2 = result.split('\n')[:2]
assert 'long' in h1
assert 'loooooonger' in h1
assert 'cat' in h2
assert 'dog' in h2
df2 = DataFrame({'A' * 41: [1, 2], 'B' * 41: [1, 2]})
result = repr(df2)
assert df2.columns[0] in result.split('\n')[0]
```

## Next Steps


---

*Source: test_format.py:284 | Complexity: Advanced | Last updated: 2026-06-02*