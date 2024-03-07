#!bin/bash

echo "Formatting django templates ..."

djlint . --reformat --format-js --indent-js 2 --format-css --indent-css 2 --indent 2 --use-gitignore --profile "jinja2"

echo "Formatting python files ..."

black . --check
black .