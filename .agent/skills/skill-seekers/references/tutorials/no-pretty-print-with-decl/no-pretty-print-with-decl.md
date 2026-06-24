# How To: No Pretty Print With Decl

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test no pretty print with decl

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `io`
- `os`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.io.common`
- `pandas.io.xml`

**Setup Required:**
```python
# Fixtures: parser, geom_df
```

## Step-by-Step Guide

### Step 1: Assign expected = "<?xml version='1.0' encoding='utf-8'?>\n<data><row><index>0</index><shape>square</shape><degrees>360</degrees><sides>4.0</sides></row><row><index>1</index><shape>circle</shape><degrees>360</degrees><sides/></row><row><index>2</index><shape>triangle</shape><degrees>180</degrees><sides>3.0</sides></row></data>"

```python
expected = "<?xml version='1.0' encoding='utf-8'?>\n<data><row><index>0</index><shape>square</shape><degrees>360</degrees><sides>4.0</sides></row><row><index>1</index><shape>circle</shape><degrees>360</degrees><sides/></row><row><index>2</index><shape>triangle</shape><degrees>180</degrees><sides>3.0</sides></row></data>"
```

**Verification:**
```python
assert output == expected
```

### Step 2: Assign output = geom_df.to_xml(...)

```python
output = geom_df.to_xml(pretty_print=False, parser=parser)
```

### Step 3: Assign output = equalize_decl(...)

```python
output = equalize_decl(output)
```

**Verification:**
```python
assert output == expected
```

### Step 4: Assign output = output.replace(...)

```python
output = output.replace(' />', '/>')
```


## Complete Example

```python
# Setup
# Fixtures: parser, geom_df

# Workflow
expected = "<?xml version='1.0' encoding='utf-8'?>\n<data><row><index>0</index><shape>square</shape><degrees>360</degrees><sides>4.0</sides></row><row><index>1</index><shape>circle</shape><degrees>360</degrees><sides/></row><row><index>2</index><shape>triangle</shape><degrees>180</degrees><sides>3.0</sides></row></data>"
output = geom_df.to_xml(pretty_print=False, parser=parser)
output = equalize_decl(output)
if output is not None:
    output = output.replace(' />', '/>')
assert output == expected
```

## Next Steps


---

*Source: test_to_xml.py:923 | Complexity: Intermediate | Last updated: 2026-06-02*