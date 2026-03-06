# Compiled Translation Files (.mo)

This directory should contain the compiled `.mo` (Machine Object) files generated from the corresponding `.po` files.

## How to Generate .mo Files

After editing the `.po` files, you need to compile them into `.mo` files for Flask-Babel to use them.

### Using pybabel (recommended):

```bash
# Compile all translations
pybabel compile -d translations

# Or compile a specific locale
pybabel compile -d translations -l en_IE
pybabel compile -d translations -l uk_UA
pybabel compile -d translations -l pt_BR
```

### Using msgfmt (alternative):

```bash
# From the project root directory
msgfmt translations/en_IE/LC_MESSAGES/messages.po -o translations/en_IE/LC_MESSAGES/messages.mo
msgfmt translations/uk_UA/LC_MESSAGES/messages.po -o translations/uk_UA/LC_MESSAGES/messages.mo
msgfmt translations/pt_BR/LC_MESSAGES/messages.po -o translations/pt_BR/LC_MESSAGES/messages.mo
```

## Note

The `.mo` files are binary files and are typically excluded from version control. They should be generated as part of your deployment process.

For development, run the compile command after making any changes to the `.po` files.
