@echo off

cls

setlocal

ECHO.
ECHO.
ECHO This batch script will launch folder browsers prompting you to
ECHO select a source directory of the .geojsons you wish to split.
ECHO.
ECHO Then this script will launch the Split_CRC_GeoJSON_Feature_Types
ECHO Python script and process all .geojson files within the selected
ECHO source directory and output the cleaned files to that same directory.
ECHO.
ECHO The python script will:
ECHO     Iterate through the features in the GeoJSON file and separates
ECHO     them based on their types (LineString, MultiLineString, Point with text,
ECHO     and Point for symbols).
ECHO     It also places isDefault features for lines, symbols, and text at the
ECHO     beginning of the respective new file.
ECHO.
ECHO     For example, example.geojson contains lines, symbols, and text features.
ECHO     The following will be created:
ECHO             * example_lines.geojson
ECHO             * example_symbols.geojson
ECHO             * example_text.geojson
ECHO.
ECHO Press any key to begin...
pause>nul

:: Get the source directory

cls

echo Select the source directory containing the .geojson files:
set "sourceDir="
for /f "usebackq tokens=*" %%i in (`powershell "Add-Type -AssemblyName System.Windows.Forms; $f = New-Object System.Windows.Forms.FolderBrowserDialog; [void]$f.ShowDialog(); $f.SelectedPath"`) do set "sourceDir=%%i"
if "%sourceDir%"=="" (
    echo No source directory selected. Exiting.
    exit /b 1
)

:: Process each .geojson file in the source directory
for %%f in ("%sourceDir%\*.geojson") do (
    echo Processing "%%f"
    python Split_CRC_GeoJSON_Feature_Types.py "%%f" --pretty
	
)

echo All files processed. Press any key to exit...
pause>nul
exit /b 1
