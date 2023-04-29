 
 
 
 #include < curses.h > 
 
 #include " window.c " 
 
 
 
 
 
 
 
 
 
 void jump ( struct Player * player ) { 
 memset ( player - > moves , 1 , 4 ) ; 
 
 player - > is_standing = false ; 
 player - > is_rising = true ; 
 player - > move_iterator = 0 ; 
 player - > change_iterator = 0 ; 
 } 
 
 
 void change_y ( struct Player * player ) { 
 player - > move_iterator + + ; 
 if ( player - > move_iterator > 4 ) { 
 player - > move_iterator = 0 ; 
 player - > change_iterator + + ; 
 if ( player - > change_iterator = = 4 ) 
 player - > is_rising = false ; 
 
 player - > moves [ player - > change_iterator ] - = 1 ; 
 } 
 player - > y + = player - > moves [ player - > move_iterator ] ; 
 player - > is_reset = false ; 
 } 
 
 
 
 void reset_mv_buffer ( struct Player * player ) { 
 memset ( player - > moves , 0 , 4 ) ; 
 player - > is_reset = true ; 
 } 
 
 
 void draw_player ( struct Player * player ) { 
 mvaddch ( WINDOW_HEIGHT - player - > previous_y , 10 , player - > bg_element_buffer ) ; 
 player - > bg_element_buffer = mvwinch ( stdscr , WINDOW_HEIGHT - player - > y , 10 ) ; 
 mvaddch ( WINDOW_HEIGHT - player - > y , 10 , player - > skin + player - > is_standing * 32 ) ; 
 } 
 
 
 
