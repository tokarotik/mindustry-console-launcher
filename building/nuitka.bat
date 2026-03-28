# start from the root of the project
# pip install nuitka

python -m nuitka --onefile --standalone --lto=yes --follow-imports --remove-output --include-package=src.libs --output-dir=builds src/main.py