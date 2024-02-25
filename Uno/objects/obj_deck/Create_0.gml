deck_x = 345 ; //deck x coordinate 
deck_y = 306; //y coordinate
card_width = 64;
card_height = 64;
deckCount = 0;
deckPoint = 0;

for (i = 0; i < 108; i++) {
	deck[i] = 0;
}
i = 0;

deck[i++] = 1;
deck[i++] = 2;
deck[i++] = 3;
deck[i++] = 4;



deckCount = i;

i = 0;


#macro CARDMAX i

scr_init_sprite_array();

i=0;

