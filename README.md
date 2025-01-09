# py_wildcard2prompt
Convert any wildcard file to a dynamicprompt text entry..

Using this simple script it is possible to convert a wildcard listing of words to a dynamic prompt for ex. stable diffusion prompts..

Usage:
In this example we have a wildcard called ../blub/fruits.txt with the following words:

apple

mango

damaged apple

orange

...

If you select the file using the dialogbox of this simple script it will be converted to a new file showing it like this:

{apple|mango|damaged_apple|orange|...}

If you paste the result to the commandline to use with your diffusers script oder SD forge webui prompt it sometimes comes up with some more random outputs against the regular use of a normal wildcard file (IMHO).

Script Source: https://github.com/zeittresor/py_wildcard2prompt
