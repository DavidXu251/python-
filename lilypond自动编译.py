
from os import system
code=r'''


% 标题部分
\header {
  title = "欢乐颂"
  composer = "贝多芬 曲"
  tagline = ##f
}

\relative c'{
    c4 c g' g a a g2 f4 f e e d d c2
}
'''

file=open('test.ly', 'wb')
file.write(code.encode('utf-8') )
file.close()

system('lilypond test.ly & test.pdf & pause')

