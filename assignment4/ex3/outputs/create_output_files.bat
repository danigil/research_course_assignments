: '
	Program to create empty text output files for comparison with an algorithm's output.
	creates: output1.txt, output2.txt, ...
'

set n=1 

:loop
	type nul >> "output%n%.txt" # touch equivalent

	set /a n=%n%+1 # n++
 
	if "%n%"=="10" goto exit
goto loop

:exit