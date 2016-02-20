if exists("current_compiler")
    finish
endif
let current_compiler = "nose"

"CompilerSet efm=%-C\ %.%#,%A*\ \ File\ \"%f\"\\,\ line\ %l%.%#,%Z%[%^\ ]%\\@=%m,%-G%.%#
CompilerSet efm=%Epyerror:%f:%l,%C~%m,%Zpyerrorend,%f:%l:%m

let s:nose="python ".expand("<sfile>:p:h")."/nose.py"
let &l:makeprg=s:nose
