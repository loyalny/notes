pip install -r requirements.txt

pyinstaller --noconsole --onefile --name="Notes" --icon=..\src\design\icons\icon.ico ..\src\main.py

echo "Сборка завершена успешно!"
pause