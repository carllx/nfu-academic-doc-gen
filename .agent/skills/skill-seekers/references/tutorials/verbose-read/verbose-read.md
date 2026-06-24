# How To: Verbose Read

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test verbose read

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `pytest`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, capsys
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

**Verification:**
```python
assert 'Tokenization took:' in captured.out
```

### Step 2: Assign data = 'a,b,c,d\none,1,2,3\none,1,2,3\n,1,2,3\none,1,2,3\n,1,2,3\n,1,2,3\none,1,2,3\ntwo,1,2,3'

```python
data = 'a,b,c,d\none,1,2,3\none,1,2,3\n,1,2,3\none,1,2,3\n,1,2,3\n,1,2,3\none,1,2,3\ntwo,1,2,3'
```

**Verification:**
```python
assert 'Parser memory cleanup took:' in captured.out
```

### Step 3: Assign captured = capsys.readouterr(...)

```python
captured = capsys.readouterr()
```

**Verification:**
```python
assert captured.out == 'Filled 3 NA values in column a\n'
```

### Step 4: Assign msg = "The 'verbose' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'verbose' option is not supported with the 'pyarrow' engine"
```

### Step 5: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), verbose=True)
```

**Verification:**
```python
assert 'Tokenization took:' in captured.out
```

### Step 6: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), verbose=True)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, capsys

# Workflow
parser = all_parsers
data = 'a,b,c,d\none,1,2,3\none,1,2,3\n,1,2,3\none,1,2,3\n,1,2,3\n,1,2,3\none,1,2,3\ntwo,1,2,3'
if parser.engine == 'pyarrow':
    msg = "The 'verbose' option is not supported with the 'pyarrow' engine"
    with pytest.raises(ValueError, match=msg):
        with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
            parser.read_csv(StringIO(data), verbose=True)
    return
with tm.assert_produces_warning(FutureWarning, match=depr_msg, check_stacklevel=False):
    parser.read_csv(StringIO(data), verbose=True)
captured = capsys.readouterr()
if parser.engine == 'c':
    assert 'Tokenization took:' in captured.out
    assert 'Parser memory cleanup took:' in captured.out
else:
    assert captured.out == 'Filled 3 NA values in column a\n'
```

## Next Steps


---

*Source: test_verbose.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*