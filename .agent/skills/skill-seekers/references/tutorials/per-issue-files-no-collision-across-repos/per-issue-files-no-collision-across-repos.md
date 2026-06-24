# How To: Per Issue Files No Collision Across Repos

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: unittest, mock, workflow, integration

## Overview

Workflow: Two repos sharing a skill_dir + issue number write distinct files.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `json`
- `os`
- `shutil`
- `tempfile`
- `unittest`
- `datetime`
- `pathlib`
- `unittest.mock`
- `github`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`
- `skill_seekers.cli.github_scraper`

**Setup Required:**
```python
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()
```

## Step-by-Step Guide

### Step 1: 'Two repos sharing a skill_dir + issue number write distinct files.'

```python
'Two repos sharing a skill_dir + issue number write distinct files.'
```

### Step 2: Assign issues = value

```python
issues = [{'number': 1, 'title': 'Same number', 'state': 'open', 'labels': [], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/alpha/proj/issues/1', 'body': 'Issue from alpha/proj', 'comments': []}]
```

### Step 3: Assign skill_dir = os.path.join(...)

```python
skill_dir = os.path.join(self.temp_dir, 'shared-skill')
```

### Step 4: Call os.makedirs()

```python
os.makedirs(os.path.join(skill_dir, 'references'), exist_ok=True)
```

### Step 5: Assign config_a = value

```python
config_a = {'repo': 'alpha/proj', 'name': 'shared-skill', 'per_issue_files': True}
```

### Step 6: Assign converter_a.data = value

```python
converter_a.data = {'issues': issues}
```

### Step 7: Assign converter_a.skill_dir = skill_dir

```python
converter_a.skill_dir = skill_dir
```

### Step 8: Call converter_a._generate_issues_reference()

```python
converter_a._generate_issues_reference()
```

### Step 9: Assign issues_b = value

```python
issues_b = [{**issues[0], 'url': 'https://github.com/beta/proj/issues/1'}]
```

### Step 10: Assign config_b = value

```python
config_b = {'repo': 'beta/proj', 'name': 'shared-skill', 'per_issue_files': True}
```

### Step 11: Assign converter_b.data = value

```python
converter_b.data = {'issues': issues_b}
```

### Step 12: Assign converter_b.skill_dir = skill_dir

```python
converter_b.skill_dir = skill_dir
```

### Step 13: Call converter_b._generate_issues_reference()

```python
converter_b._generate_issues_reference()
```

### Step 14: Assign alpha_file = os.path.join(...)

```python
alpha_file = os.path.join(skill_dir, 'references', 'issues', 'alpha-proj-1.md')
```

### Step 15: Assign beta_file = os.path.join(...)

```python
beta_file = os.path.join(skill_dir, 'references', 'issues', 'beta-proj-1.md')
```

### Step 16: Call self.assertTrue()

```python
self.assertTrue(os.path.exists(alpha_file))
```

### Step 17: Call self.assertTrue()

```python
self.assertTrue(os.path.exists(beta_file))
```

### Step 18: Assign converter_a = self.GitHubToSkillConverter(...)

```python
converter_a = self.GitHubToSkillConverter(config_a)
```

### Step 19: Assign converter_b = self.GitHubToSkillConverter(...)

```python
converter_b = self.GitHubToSkillConverter(config_b)
```


## Complete Example

```python
# Setup
if not PYGITHUB_AVAILABLE:
    self.skipTest('PyGithub not installed')
from skill_seekers.cli.github_scraper import GitHubToSkillConverter
self.GitHubToSkillConverter = GitHubToSkillConverter
self.temp_dir = tempfile.mkdtemp()

# Workflow
'Two repos sharing a skill_dir + issue number write distinct files.'
issues = [{'number': 1, 'title': 'Same number', 'state': 'open', 'labels': [], 'created_at': '2023-01-01T00:00:00', 'updated_at': '2023-01-02T00:00:00', 'closed_at': None, 'url': 'https://github.com/alpha/proj/issues/1', 'body': 'Issue from alpha/proj', 'comments': []}]
skill_dir = os.path.join(self.temp_dir, 'shared-skill')
os.makedirs(os.path.join(skill_dir, 'references'), exist_ok=True)
config_a = {'repo': 'alpha/proj', 'name': 'shared-skill', 'per_issue_files': True}
with patch.object(self.GitHubToSkillConverter, '_load_data', return_value={}):
    converter_a = self.GitHubToSkillConverter(config_a)
converter_a.data = {'issues': issues}
converter_a.skill_dir = skill_dir
converter_a._generate_issues_reference()
issues_b = [{**issues[0], 'url': 'https://github.com/beta/proj/issues/1'}]
config_b = {'repo': 'beta/proj', 'name': 'shared-skill', 'per_issue_files': True}
with patch.object(self.GitHubToSkillConverter, '_load_data', return_value={}):
    converter_b = self.GitHubToSkillConverter(config_b)
converter_b.data = {'issues': issues_b}
converter_b.skill_dir = skill_dir
converter_b._generate_issues_reference()
alpha_file = os.path.join(skill_dir, 'references', 'issues', 'alpha-proj-1.md')
beta_file = os.path.join(skill_dir, 'references', 'issues', 'beta-proj-1.md')
self.assertTrue(os.path.exists(alpha_file))
self.assertTrue(os.path.exists(beta_file))
```

## Next Steps


---

*Source: test_github_scraper.py:1398 | Complexity: Advanced | Last updated: 2026-06-02*