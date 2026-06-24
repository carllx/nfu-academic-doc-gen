# How To: Copy Skill Md Content Preserved

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test copy skill md content preserved

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `unittest.mock`
- `pytest`
- `skill_seekers.mcp.marketplace_publisher`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `skill_seekers.mcp.marketplace_manager`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `skill_seekers.mcp.git_repo`
- `git`
- `skill_seekers.mcp.marketplace_manager`
- `skill_seekers.mcp.git_repo`
- `pathlib`

**Setup Required:**
```python
# Fixtures: skill_dir, tmp_path
```

## Step-by-Step Guide

### Step 1: Assign plugin_dir = value

```python
plugin_dir = tmp_path / 'plugin_output'
```

**Verification:**
```python
assert original == copied
```

### Step 2: Assign publisher = MarketplacePublisher.__new__(...)

```python
publisher = MarketplacePublisher.__new__(MarketplacePublisher)
```

### Step 3: Call publisher._copy_skill_to_plugin()

```python
publisher._copy_skill_to_plugin(skill_dir, plugin_dir, 'test-skill')
```

### Step 4: Assign original = unknown.read_text(...)

```python
original = (skill_dir / 'SKILL.md').read_text()
```

### Step 5: Assign copied = unknown.read_text(...)

```python
copied = (plugin_dir / 'skills' / 'test-skill' / 'SKILL.md').read_text()
```

**Verification:**
```python
assert original == copied
```


## Complete Example

```python
# Setup
# Fixtures: skill_dir, tmp_path

# Workflow
plugin_dir = tmp_path / 'plugin_output'
publisher = MarketplacePublisher.__new__(MarketplacePublisher)
publisher._copy_skill_to_plugin(skill_dir, plugin_dir, 'test-skill')
original = (skill_dir / 'SKILL.md').read_text()
copied = (plugin_dir / 'skills' / 'test-skill' / 'SKILL.md').read_text()
assert original == copied
```

## Next Steps


---

*Source: test_marketplace_publisher.py:102 | Complexity: Intermediate | Last updated: 2026-06-02*