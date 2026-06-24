# How To: Detect Chained Assignment Implicit Take2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test detect chained assignment implicit take2

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `string`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = random_text(...)

```python
df = random_text(100000)
```

**Verification:**
```python
assert df._is_copy is not None
```

### Step 2: Assign indexer = df.letters.apply(...)

```python
indexer = df.letters.apply(lambda x: len(x) > 10)
```

**Verification:**
```python
assert df._is_copy is not None
```

### Step 3: Assign df = value

```python
df = df.loc[indexer]
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 4: Assign unknown = unknown.apply(...)

```python
df.loc[:, 'letters'] = df['letters'].apply(str.lower)
```

**Verification:**
```python
assert df._is_copy is not None
```

### Step 5: Assign unknown = unknown.apply(...)

```python
df['letters'] = df['letters'].apply(str.lower)
```

**Verification:**
```python
assert df._is_copy is None
```

### Step 6: Call pytest.skip()

```python
pytest.skip('_is_copy is not always set for CoW')
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
if using_copy_on_write or warn_copy_on_write:
    pytest.skip('_is_copy is not always set for CoW')
df = random_text(100000)
indexer = df.letters.apply(lambda x: len(x) > 10)
df = df.loc[indexer]
assert df._is_copy is not None
df.loc[:, 'letters'] = df['letters'].apply(str.lower)
assert df._is_copy is not None
df['letters'] = df['letters'].apply(str.lower)
assert df._is_copy is None
```

## Next Steps


---

*Source: test_chaining_and_caching.py:376 | Complexity: Intermediate | Last updated: 2026-06-02*