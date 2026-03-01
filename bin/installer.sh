#!/usr/bin/sh

pip3 install -r requirements.txt

pyinstaller --noconsole --onefile --name="Notes" --icon=../src/design/icons/icon.ico ../src/main.py

chmod +x installer.sh

echo "Сборка завершена успешно!"
read
