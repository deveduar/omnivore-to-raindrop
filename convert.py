#!/usr/bin/env python3

# MIT License
# 
# Copyright 2024 deveduar
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import csv
import sys
import glob
import codecs

def convert_files(pattern):
    # Abrir archivo con codecs para manejar UTF-8 correctamente
    with codecs.open('metadata.csv', 'w', encoding='utf-8') as output_file:
        writer = csv.writer(output_file, 
                          quoting=csv.QUOTE_MINIMAL,
                          delimiter=',',
                          lineterminator='\n')
        
        # Escribir encabezados
        writer.writerow(['url', 'title', 'tags', 'note', 'created'])
        
        # Procesar archivos
        files = glob.glob(pattern)
        if not files:
            print(f"No files found: {pattern}", file=sys.stderr)
            return
        
        total_rows = 0
        for file in files:
            try:
                with codecs.open(file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    print(f"Processing {file}... ({len(data)} records)", file=sys.stderr)
                    
                    for item in data:
                        # Verificar y limpiar datos
                        title = (item.get('title') or '').replace('"', '""')
                        description = (item.get('description') or '').replace('"', '""')
                        tags = ','.join(tag.replace('"', '""') for tag in (item.get('labels') or []))
                        url = item.get('url', '')
                        created = item.get('savedAt', '')
                        
                        # Escribir fila
                        writer.writerow([url, title, tags, description, created])
                        total_rows += 1
                        
            except Exception as e:
                print(f"Error processing {file}: {e}", file=sys.stderr)
                continue
        
        print(f"\nA total of {total_rows} records were processed.", file=sys.stderr)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} \"metadata_*.json\"", file=sys.stderr)
        sys.exit(1)
    
    convert_files(sys.argv[1])
    print("\nConversion completed! The metadata.csv file has been created.", file=sys.stderr)

if __name__ == "__main__":
    main()