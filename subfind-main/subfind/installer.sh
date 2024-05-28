#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    # Get Python version
    python_version=$(python3 -c 'import sys; print(sys.version_info[:3])')
    echo "Python version: $python_version"

    packages=("requests" "sys" "os" "requests" "Thread")

    # Install each package
    for package in "${packages[@]}"; do
        echo "Installing $package..."
        pip3 install "$package"
    done

    echo "All packages installed successfully!"

else
    echo "Python is not installed. Please install python firstly "
fi



