@echo on

set FULLNAME=Voice Training.wav

:: Remove extension from filename
for %%A in ("%FULLNAME%") do set "FILENAME=%%~nA"

:: Create the output directory if it does not exist
if not exist "output/%FILENAME%" mkdir "output/%FILENAME%"

whisper "input/%FULLNAME%" --model small.en --language en --fp16 False --task transcribe --output_dir "output/%FILENAME%"