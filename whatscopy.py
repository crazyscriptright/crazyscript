from ctypes import sizeof
from tkinter import Y
import pyautogui as pg
import time
time.sleep(5)

A='''.
      /\\
    /    \\
  /===\\
/            \\'''

AA="****************"
B='''.
 ________
!             )
!--------
!             )
"""""""""'''
C = '''.
  _________
.'
!
!
'. _________'''
D='''.
  ____
|          ' .
|             !
|            .'
'.____ . '  '''

E = '''.
  _________
!
!__________
!
'. _________'''
F = '''.
  _________
!
!__________
!
!'''
G = '''.
   _________
.'
!
!       """""""".
!               !   !
'. _______.'    !'''
H='''.
!             !
!_______ !
!             !
!             !'''
I='''.
________
       |
       |
____!____'''
J = '''.
 _______
       |
       |
 ___.' '''
K = '''.
!        ,'
!___,'
!      '.
!        '. '''
L = '''.
!
!
!
!________'''
M = '''.
! \\\  // !
!  \\\//  !
!          !
!          !'''
N = '''.
! \\\       !
!   \\\     !
!     \\\   !
!       \\\ !'''
O = '''.
   _____
.'          '.
!            !
!            !
'. _____ .' '''
P = '''.   ____
.'         '.
!           |
! _____.'
!            
!'''
Q = '''.
  _____
.'          '.
!            !
!            !
!            !
'. _____\_\ '''
R = '''.
   _____
!            !
! ______.'
!         \          
!            \ '''
S='''.
   ________
.'
'.________
               '.
________.' '''
T = '''.
________
      |
      |
      !'''
U = '''.
!            !
!            !
!            !
 '. ____ .' '''
V = '''.
\              /
  \          /
    \      /
      '.  .' '''
W = '''.
\                    / 
  \                / 
    \     /\    /
      '. .'   '. .'  '''
X = '''.
 \        /
   '. _ .'           
   .'   '.
 /        \ '''
Y = '''.
\        /
  '.   .'   
     !
     ! '''
Z = '''.
_______
          .  '
     .  '
.  '
"""""""""  '''

k=[H,A,P,P,Y,AA,B,I,R,T,H,D,A,Y,AA,M,U,N,N,A]
#j=[A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]


for i in range (0,len(k)):
    pg.typewrite(k[i])
    pg.press("enter")
