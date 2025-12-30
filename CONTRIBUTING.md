# Contributing to Kiro Pro Free

First off, thank you for considering contributing to this project! 🎉

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **System information** (OS, Python version, Kiro version)
- **Error messages** or logs
- **Screenshots** if applicable

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** - why is this enhancement useful?
- **Proposed solution** - how should it work?
- **Alternatives considered**

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/AmazingFeature`)
3. **Make your changes**
4. **Test thoroughly** on your system
5. **Commit with clear messages** (`git commit -m 'Add some AmazingFeature'`)
6. **Push to your branch** (`git push origin feature/AmazingFeature`)
7. **Open a Pull Request**

#### Pull Request Guidelines

- Follow the existing code style
- Add comments for complex logic
- Update documentation if needed
- Test on multiple platforms if possible
- Keep changes focused and atomic
- Reference related issues

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/kiro-pro-free.git
cd kiro-pro-free

# Install dependencies
pip install -r requirements.txt

# Run tests (if available)
python kiro_config.py
```

## Code Style

- Follow PEP 8 for Python code
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Handle errors gracefully

### Example

```python
def backup_file(file_path):
    """
    Create timestamped backup of file
    
    Args:
        file_path (str): Path to file to backup
        
    Returns:
        str: Path to backup file, or None if failed
    """
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return None
    
    # Implementation...
```

## Testing

Before submitting:

1. Test on your target platform
2. Verify all features work
3. Check for error handling
4. Ensure backups are created
5. Test restoration process

## Documentation

- Update README.md if adding features
- Add to docs/ if significant changes
- Include usage examples
- Document any new dependencies

## Version Compatibility

When contributing, consider:

- Python 3.8+ compatibility
- Cross-platform support (Windows, macOS, Linux)
- Different Kiro versions
- Backward compatibility

## Commit Messages

Use clear, descriptive commit messages:

```
Good:
- "Add automatic backup cleanup feature"
- "Fix permission error on Linux systems"
- "Update documentation for token bypass"

Bad:
- "fix bug"
- "update"
- "changes"
```

## Legal Considerations

By contributing, you agree that:

- Your contributions will be licensed under the MIT License
- You have the right to submit the contributions
- Your contributions are for educational purposes
- You understand the ethical implications

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion
- Contact maintainers

## Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Credited in release notes
- Appreciated by the community! 🙏

---

Thank you for contributing to Kiro Pro Free! 🚀
