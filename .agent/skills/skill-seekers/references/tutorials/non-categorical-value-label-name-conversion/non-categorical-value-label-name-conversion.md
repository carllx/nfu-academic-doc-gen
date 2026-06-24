# How To: Non Categorical Value Label Name Conversion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non categorical value label name conversion

## Prerequisites

**Required Modules:**
- `bz2`
- `datetime`
- `datetime`
- `gzip`
- `io`
- `os`
- `struct`
- `tarfile`
- `zipfile`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.frame`
- `pandas.io.parsers`
- `pandas.io.stata`


## Step-by-Step Guide

### Step 1: Assign data = DataFrame(...)

```python
data = DataFrame({'invalid~!': [1, 1, 2, 3, 5, 8], '6_invalid': [1, 1, 2, 3, 5, 8], 'invalid_name_longer_than_32_characters': [8, 8, 9, 9, 8, 8], 'aggregate': [2, 5, 5, 6, 6, 9], (1, 2): [1, 2, 3, 4, 5, 6]})
```

**Verification:**
```python
assert reader_value_labels == expected
```

### Step 2: Assign value_labels = value

```python
value_labels = {'invalid~!': {1: 'label1', 2: 'label2'}, '6_invalid': {1: 'label1', 2: 'label2'}, 'invalid_name_longer_than_32_characters': {8: 'eight', 9: 'nine'}, 'aggregate': {5: 'five'}, (1, 2): {3: 'three'}}
```

### Step 3: Assign expected = value

```python
expected = {'invalid__': {1: 'label1', 2: 'label2'}, '_6_invalid': {1: 'label1', 2: 'label2'}, 'invalid_name_longer_than_32_char': {8: 'eight', 9: 'nine'}, '_aggregate': {5: 'five'}, '_1__2_': {3: 'three'}}
```

### Step 4: Call data.to_stata()

```python
data.to_stata(path, value_labels=value_labels)
```

### Step 5: Assign reader_value_labels = reader.value_labels(...)

```python
reader_value_labels = reader.value_labels()
```

**Verification:**
```python
assert reader_value_labels == expected
```


## Complete Example

```python
# Workflow
data = DataFrame({'invalid~!': [1, 1, 2, 3, 5, 8], '6_invalid': [1, 1, 2, 3, 5, 8], 'invalid_name_longer_than_32_characters': [8, 8, 9, 9, 8, 8], 'aggregate': [2, 5, 5, 6, 6, 9], (1, 2): [1, 2, 3, 4, 5, 6]})
value_labels = {'invalid~!': {1: 'label1', 2: 'label2'}, '6_invalid': {1: 'label1', 2: 'label2'}, 'invalid_name_longer_than_32_characters': {8: 'eight', 9: 'nine'}, 'aggregate': {5: 'five'}, (1, 2): {3: 'three'}}
expected = {'invalid__': {1: 'label1', 2: 'label2'}, '_6_invalid': {1: 'label1', 2: 'label2'}, 'invalid_name_longer_than_32_char': {8: 'eight', 9: 'nine'}, '_aggregate': {5: 'five'}, '_1__2_': {3: 'three'}}
with tm.ensure_clean() as path:
    with tm.assert_produces_warning(InvalidColumnName):
        data.to_stata(path, value_labels=value_labels)
    with StataReader(path) as reader:
        reader_value_labels = reader.value_labels()
        assert reader_value_labels == expected
```

## Next Steps


---

*Source: test_stata.py:2266 | Complexity: Intermediate | Last updated: 2026-06-02*