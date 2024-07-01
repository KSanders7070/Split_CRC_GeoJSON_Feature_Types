# Split_CRC_GeoJSON_Feature_Types
Will separate your CRC GeoJSON into different files, grouping like-types (lines, symbols, text, etc...)  
The isDefaults will be placed at the beginning of the feature collection.

**The python script will:**
* Iterate through the features in the GeoJSON file and separates them based on their types (LineString, MultiLineString, Point with text, and Point for symbols).
* It also places isDefault features for lines, symbols, and text at the beginning of the respective new file.

**Run:**
1) Download the `Run_Split_CRC_GeoJSON_Feature_Types.bat` and `Split_CRC_GeoJSON_Feature_Types.py` and place them in the same directory.
2) Launch the .bat and follow the prompts.

_or..._

1) Download `Split_CRC_GeoJSON_Feature_Types.py`
2) Launch CMD prompt.
3) CD to the directory the .py is in.
4) Modify as needed and paste the following: `python Split_CRC_GeoJSON_Feature_Types.py "%USERPROFILE%\Desktop\test.geojson" --pretty`

Note: if you leave off the `--pretty`, it should export as a compressed geojson format.
