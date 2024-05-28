REM Install Python packages using PIP

REM List of package names
set "packages=requests sys os requests Thread"

REM Install each package
for %%p in (%packages%) do (
    echo Installing %%p...
    pip install %%p
)

echo All packages installed
echo Press any key to exit...
pause