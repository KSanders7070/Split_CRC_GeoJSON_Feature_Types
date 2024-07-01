import json
import argparse
import os

def split_geojson(input_file, pretty_print):
    with open(input_file, 'r', encoding='utf-8') as f:
        geojson_data = json.load(f)

    if 'features' not in geojson_data or not isinstance(geojson_data['features'], list):
        raise ValueError("Invalid GeoJSON format: 'features' array not found or not a list.")

    base_name = os.path.splitext(os.path.basename(input_file))[0]
    dir_name = os.path.dirname(input_file)
    
    line_features = []
    symbol_features = []
    text_features = []

    line_defaults = None
    symbol_defaults = None
    text_defaults = None

    for feature in geojson_data['features']:
        if 'properties' in feature:
            if 'isLineDefaults' in feature['properties']:
                line_defaults = feature
            elif 'isSymbolDefaults' in feature['properties']:
                symbol_defaults = feature
            elif 'isTextDefaults' in feature['properties']:
                text_defaults = feature
            else:
                if feature['geometry']['type'] == 'LineString' or feature['geometry']['type'] == 'MultiLineString':
                    line_features.append(feature)
                elif feature['geometry']['type'] == 'Point':
                    if 'text' in feature['properties']:
                        text_features.append(feature)
                    else:
                        symbol_features.append(feature)

    def write_geojson(features, output_file, defaults, pretty_print):
        with open(output_file, 'w', encoding='utf-8') as f:
            cleaned_features = [defaults] + features if defaults else features
            if pretty_print:
                json.dump({'type': 'FeatureCollection', 'features': cleaned_features}, f, indent=4)
            else:
                json.dump({'type': 'FeatureCollection', 'features': cleaned_features}, f)
        print(f"GeoJSON written to {output_file}")

    if line_features:
        write_geojson(line_features, os.path.join(dir_name, f"{base_name}_lines.geojson"), line_defaults, pretty_print)
    if symbol_features:
        write_geojson(symbol_features, os.path.join(dir_name, f"{base_name}_symbols.geojson"), symbol_defaults, pretty_print)
    if text_features:
        write_geojson(text_features, os.path.join(dir_name, f"{base_name}_text.geojson"), text_defaults, pretty_print)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split GeoJSON file into separate files based on feature types.')
    parser.add_argument('source', help='Source GeoJSON file to split')
    parser.add_argument('--pretty', action='store_true', help='Pretty-print output with indent of 4 spaces')
    
    args = parser.parse_args()
    
    split_geojson(args.source, args.pretty)
