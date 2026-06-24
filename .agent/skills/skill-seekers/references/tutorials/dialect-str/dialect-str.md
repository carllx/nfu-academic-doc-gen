# How To: Dialect Str

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dialect str

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `csv`
- `io`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.io.parsers.base_parser`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign dialect_name = 'mydialect'

```python
dialect_name = 'mydialect'
```

### Step 2: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 3: Assign data = 'fruit:vegetable\napple:broccoli\npear:tomato\n'

```python
data = 'fruit:vegetable\napple:broccoli\npear:tomato\n'
```

### Step 4: Assign exp = DataFrame(...)

```python
exp = DataFrame({'fruit': ['apple', 'pear'], 'vegetable': ['broccoli', 'tomato']})
```

### Step 5: Assign df = parser.read_csv(...)

```python
df = parser.read_csv(StringIO(data), dialect=dialect_name)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, exp)
```

### Step 7: Assign msg = "The 'dialect' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'dialect' option is not supported with the 'pyarrow' engine"
```

### Step 8: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), dialect=dialect_name)
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
dialect_name = 'mydialect'
parser = all_parsers
data = 'fruit:vegetable\napple:broccoli\npear:tomato\n'
exp = DataFrame({'fruit': ['apple', 'pear'], 'vegetable': ['broccoli', 'tomato']})
with tm.with_csv_dialect(dialect_name, delimiter=':'):
    if parser.engine == 'pyarrow':
        msg = "The 'dialect' option is not supported with the 'pyarrow' engine"
        with pytest.raises(ValueError, match=msg):
            parser.read_csv(StringIO(data), dialect=dialect_name)
        return
    df = parser.read_csv(StringIO(data), dialect=dialect_name)
    tm.assert_frame_equal(df, exp)
```

## Next Steps


---

*Source: test_dialect.py:64 | Complexity: Advanced | Last updated: 2026-06-02*