# How To: Raise On Passed Int Dtype With Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test raise on passed int dtype with nas

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `io`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: all_parsers
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'YEAR, DOY, a\n2001,106380451,10\n2001,,11\n2001,106380451,67'

```python
data = 'YEAR, DOY, a\n2001,106380451,10\n2001,,11\n2001,106380451,67'
```

### Step 3: Assign msg = 'Integer column has NA values'

```python
msg = 'Integer column has NA values'
```

### Step 4: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), dtype={'DOY': np.int64}, skipinitialspace=True)
```

### Step 5: Assign msg = "The 'skipinitialspace' option is not supported with the 'pyarrow' engine"

```python
msg = "The 'skipinitialspace' option is not supported with the 'pyarrow' engine"
```

### Step 6: Assign msg = 'Unable to convert column DOY'

```python
msg = 'Unable to convert column DOY'
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers

# Workflow
parser = all_parsers
data = 'YEAR, DOY, a\n2001,106380451,10\n2001,,11\n2001,106380451,67'
if parser.engine == 'c':
    msg = 'Integer column has NA values'
elif parser.engine == 'pyarrow':
    msg = "The 'skipinitialspace' option is not supported with the 'pyarrow' engine"
else:
    msg = 'Unable to convert column DOY'
with pytest.raises(ValueError, match=msg):
    parser.read_csv(StringIO(data), dtype={'DOY': np.int64}, skipinitialspace=True)
```

## Next Steps


---

*Source: test_dtypes_basic.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*