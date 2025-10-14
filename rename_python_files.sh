#!/bin/bash
echo "--- Python File Renamer (Kebab-case to Snake_case) ---"
find . -type f -name "*.py" -print0 | while IFS= read -r -d $'\0' old_path; do
    dir_name=$(dirname "$old_path")
    base_name=$(basename "$old_path")

    if [[ "$base_name" == *-* ]]; then
        new_base_name="${base_name//-/_}"
        new_path="$dir_name/$new_base_name"

        if [ "$old_path" != "$new_path" ]; then
            echo "Renaming: $old_path -> $new_path"
            mv "$old_path" "$new_path"
        fi
    fi
done
echo "--- Renaming complete. ---"
