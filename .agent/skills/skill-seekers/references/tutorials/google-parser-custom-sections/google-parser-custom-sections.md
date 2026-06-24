# How To: Google Parser Custom Sections

**Difficulty**: Beginner
**Estimated Time**: 5 minutes

## Overview

Instantiate GoogleParser: Test parsing an unknown section with custom GoogleParser
configuration.

## Prerequisites

**Required Modules:**
- `typing`
- `pytest`
- `docstring_parser.common`
- `docstring_parser.google`


## Step-by-Step Guide

### Step 1: Assign parser = GoogleParser(...)

```python
parser = GoogleParser([Section('DESCRIPTION', 'desc', SectionType.SINGULAR), Section('ARGUMENTS', 'param', SectionType.MULTIPLE), Section('ATTRIBUTES', 'attribute', SectionType.MULTIPLE), Section('EXAMPLES', 'examples', SectionType.SINGULAR)], title_colon=False)
```


## Complete Example

```python
# Workflow
parser = GoogleParser([Section('DESCRIPTION', 'desc', SectionType.SINGULAR), Section('ARGUMENTS', 'param', SectionType.MULTIPLE), Section('ATTRIBUTES', 'attribute', SectionType.MULTIPLE), Section('EXAMPLES', 'examples', SectionType.SINGULAR)], title_colon=False)
```

## Next Steps


---

*Source: test_google.py:58 | Complexity: Beginner | Last updated: 2026-06-02*