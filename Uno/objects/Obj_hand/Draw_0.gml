
for (i = 0; i < hand_count; i++){
	if (hand[i] > 0) {
		draw_sprite(sprite_array[hand[i]], -1 , 123 + (.4 + card_width) * i , 493 - .4 * i );
	}
}
