@echo off
echo Building optimized Docker image for housing rates app...
echo.

echo Step 1: Building the image...
docker build -t housingrates:optimized .

echo.
echo Step 2: Checking image size...
docker images housingrates:optimized

echo.
echo Step 3: Running the container...
echo Container will be available at http://localhost:8501
echo Press Ctrl+C to stop the container
echo.
docker run -p 8501:8501 housingrates:optimized

pause
