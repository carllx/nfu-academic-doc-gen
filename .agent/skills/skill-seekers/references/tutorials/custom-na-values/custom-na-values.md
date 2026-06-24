# How To: Custom Na Values

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test custom na values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `numpy`
- `pytest`
- `pandas._libs.parsers`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_parsers, na_values
```

## Step-by-Step Guide

### Step 1: Assign parser = all_parsers

```python
parser = all_parsers
```

### Step 2: Assign data = 'A,B,C\nignore,this,row\n1,NA,3\n-1.#IND,5,baz\n7,8,NaN\n'

```python
data = 'A,B,C\nignore,this,row\n1,NA,3\n-1.#IND,5,baz\n7,8,NaN\n'
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame([[1.0, np.nan, 3], [np.nan, 5, np.nan], [7, 8, np.nan]], columns=['A', 'B', 'C'])
```

### Step 4: Assign result = parser.read_csv(...)

```python
result = parser.read_csv(StringIO(data), na_values=na_values, skiprows=[1])
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign msg = "skiprows argument must be an integer when using engine='pyarrow'"

```python
msg = "skiprows argument must be an integer when using engine='pyarrow'"
```

### Step 7: Call parser.read_csv()

```python
parser.read_csv(StringIO(data), na_values=na_values, skiprows=[1])
```


## Complete Example

```python
# Setup
# Fixtures: all_parsers, na_values

# Workflow
parser = all_parsers
data = 'A,B,C\nignore,this,row\n1,NA,3\n-1.#IND,5,baz\n7,8,NaN\n'
expected = DataFrame([[1.0, np.nan, 3], [np.nan, 5, np.nan], [7, 8, np.nan]], columns=['A', 'B', 'C'])
if parser.engine == 'pyarrow':
    msg = "skiprows argument must be an integer when using engine='pyarrow'"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(StringIO(data), na_values=na_values, skiprows=[1])
    return
result = parser.read_csv(StringIO(data), na_values=na_values, skiprows=[1])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_na_values.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*