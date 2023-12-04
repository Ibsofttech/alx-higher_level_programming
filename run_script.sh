#!/bin/bash

# Check if changes are present
if [[ -n $(git status -s) ]]; then
    # Add all changes
    git add .

    # Commit changes
    echo "Enter your commit message:"
    read commit_message
    git commit -m "$commit_message"

    # Push changes
    git push origin main  # Change 'main' to your branch name if needed
else
    echo "No changes to commit."
fi

