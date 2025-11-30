@echo off
echo ==========================================
echo      RTL LAB MANUAL - AUTO DEPLOYER
echo ==========================================

:: 1. Clean and Build
echo.
echo [1/5] Cleaning and Rebuilding HTML...
call .\make.bat clean
call .\make.bat html
if %errorlevel% neq 0 goto :error

:: 2. Prepare docs folder
echo.
echo [2/5] Updating docs/ folder...
if exist docs rmdir /s /q docs
mkdir docs
:: Copy all files from build/html to docs
xcopy /s /e /y build\html\* docs\ > nul
:: Create .nojekyll file
type nul > docs\.nojekyll

:: 3. Git Stage
echo.
echo [3/5] Staging files...
git add .

:: 4. Git Commit (Ask for message)
echo.
echo [4/5] Committing...
set /p commit_msg="Enter commit message (or press Enter for default): "
if "%commit_msg%"=="" set commit_msg="Auto-update website content"
git commit -m "%commit_msg%"

:: 5. Git Push
echo.
echo [5/5] Pushing to GitHub...
git push
if %errorlevel% neq 0 goto :error

echo.
echo ==========================================
echo      SUCCESS! Website is updating...
echo ==========================================
echo.
pause
exit

:error
echo.
echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
echo      ERROR OCCURRED! Please check logs.
echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
pause