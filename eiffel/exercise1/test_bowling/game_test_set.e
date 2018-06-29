note
	description: "[
		Eiffel tests that can be executed by testing tool.
	]"
	author: "EiffelStudio test wizard"
	date: "$Date$"
	revision: "$Revision$"
	testing: "type/manual"

class
	GAME_TEST_SET

inherit
	EQA_TEST_SET

feature

	test_gutter_game

		local
			g: GAME
		do
			create g.make
			across 0 |..| 19 as it loop
		    	g.roll(0)
		    end
			assert ("Gutter Game", g.score = 0)
		end

	test_all_ones

		local
			g: GAME
		do
			create g.make
			across 0 |..| 19 as it loop
		    	g.roll(1)
		    end
			assert ("All Ones", g.score = 20)
		end

	test_one_spare

		local
			g: GAME
		do
			create g.make
			g.roll_many(2, 5)
			g.roll(3)
			across 0 |..| 16 as it loop
		    	g.roll(0)
		    end
			assert ("One Spare", g.score = 16)
		end

	test_one_strike

		local
			g: GAME
		do
			create g.make
			g.roll(10)
			g.roll(3)
        	g.roll(4)
			across 0 |..| 15 as it loop
		    	g.roll(0)
		    end
			assert ("One Strike", g.score = 24)
		end

	test_perfect_game

		local
			g: GAME
		do
			create g.make
			across 0 |..| 11 as it loop
		    	g.roll(10)
		    end
			assert ("Perfect Game", g.score = 300)
		end

	test_last_spare
		local
			g: GAME
		do
			create g.make
			across 0 |..| 8 as it loop
		    	g.roll(10)
		    end
		    g.roll_many(2, 5)
		    g.roll(10)
			assert ("Last Spare", g.score = 275)
		end
end
