# How To: Passes When All Set

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: mock

## Overview

Configuration example: test passes when all set

## Prerequisites

**Required Modules:**
- `__future__`
- `os`
- `unittest.mock`
- `skill_seekers.cli.doctor`


## Step-by-Step Guide

### Step 1: Assign env = value

```python
env = {'ANTHROPIC_API_KEY': 'sk-ant-test123456789', 'GITHUB_TOKEN': 'ghp_test123456789', 'GOOGLE_API_KEY': 'AIza_test123456789', 'OPENAI_API_KEY': 'sk-test123456789', 'MOONSHOT_API_KEY': 'sk-moon-test123456789'}
```


## Complete Example

```python
# Workflow
env = {'ANTHROPIC_API_KEY': 'sk-ant-test123456789', 'GITHUB_TOKEN': 'ghp_test123456789', 'GOOGLE_API_KEY': 'AIza_test123456789', 'OPENAI_API_KEY': 'sk-test123456789', 'MOONSHOT_API_KEY': 'sk-moon-test123456789'}
```

## Next Steps


---

*Source: test_doctor.py:86 | Complexity: Beginner | Last updated: 2026-06-02*