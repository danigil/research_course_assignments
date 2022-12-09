: '
	Program to create empty text input files for to feed into an algorithm.
	creates: input1.txt, input2.txt, ...
'

set n=1 

:loop
	type nul >> "input%n%.txt" # touch equivalent

	set /a n=%n%+1 # n++
 
	if "%n%"=="10" goto exit
goto loop

:exit