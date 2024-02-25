
card_width = 64;
card_height = 64;
hand_count = 0;


for (i = 0; i < 6; i++) {
	hand[i] = 0;
}
i = 0;

hand[i++] = 4;
hand[i++] = 3;
hand[i++] = 2;
hand[i++] = 1;


hand_count = i;

i = 0;

sprite_array[i++] = Spr_Card1;
sprite_array[i++] = Spr_Card1;
sprite_array[i++] = SprCard2;
sprite_array[i++] = SprCard3;
sprite_array[i++] = SprCard4;


scr_init_sprite_array();


