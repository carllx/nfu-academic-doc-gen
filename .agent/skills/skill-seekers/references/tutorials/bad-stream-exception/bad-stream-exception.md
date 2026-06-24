# How To: Bad Stream Exception

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bad stream exception

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `csv`
- `io`
- `os`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, csv_dir_path
```

## Step-by-Step Guide

### Step 1: Assign path = os.path.join(...)

```python
path = os.path.join(csv_dir_path, 'sauron.SHIFT_JIS.csv')
```

### Step 2: Assign codec = codecs.lookup(...)

```python
codec = codecs.lookup('utf-8')
```

### Step 3: Assign utf8 = codecs.lookup(...)

```python
utf8 = codecs.lookup('utf-8')
```

### Step 4: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 5: Assign msg = "'utf-8' codec can't decode byte"

```python
msg = "'utf-8' codec can't decode byte"
```

### Step 6: Call parser.read_csv()

```python
parser.read_csv(stream)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, csv_dir_path

# Workflow
path = os.path.join(csv_dir_path, 'sauron.SHIFT_JIS.csv')
codec = codecs.lookup('utf-8')
utf8 = codecs.lookup('utf-8')
parser = all_parsers
msg = "'utf-8' codec can't decode byte"
with open(path, 'rb') as handle, codecs.StreamRecoder(handle, utf8.encode, utf8.decode, codec.streamreader, codec.streamwriter) as stream:
    with pytest.raises(UnicodeDecodeError, match=msg):
        parser.read_csv(stream)
```

## Next Steps


---

*Source: test_read_errors.py:47 | Complexity: Intermediate | Last updated: 2026-06-02*