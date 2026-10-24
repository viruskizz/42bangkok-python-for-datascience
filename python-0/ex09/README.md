# ft_package

A small Python package that counts how many times a value appears in a list.

## Build

From the `ex09` directory:

```bash
python3 -m build
```

## Install

Install either distribution created in `dist/`:

```bash
python3 -m pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Or:

```bash
python3 -m pip install ./dist/ft_package-0.0.1.tar.gz
```

## Usage

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

## License

MIT. See `LICENSE`.