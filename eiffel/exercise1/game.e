note
	description: "Summary description for {GAME}."
	author: ""
	date: "$Date$"
	revision: "$Revision$"

class
	GAME

create
	make

feature

	index, nframe: INTEGER
	rolls: ARRAY[INTEGER]

	make
		do
			index := 0
			nframe := 20
			create rolls.make_filled(0,0,20)
		end

	roll (pins: INTEGER)
		require
			not_negative_pins: pins > -1
			not_greater_than_ten: pins < 11
		do
			rolls.put(pins, index)
			index := index + 1
		ensure
			index_check: index = old index + 1
			index_bound: index < 21
		end

	roll_many(n: INTEGER; pins: INTEGER)
		require
			not_negative_pins: pins > -1
			not_greater_than_ten: pins < 11
			not_negative_n: n > -1
			not_greater_than_twentyone: n < 22
		do
			across 0 |..| (n - 1) as it loop
				roll(pins)
			end
		end

	score : INTEGER
		local
			strike, scores: INTEGER
		do
			-- Check Strikes, Spares and Points
			across 0 |..| (nframe - 1) as it loop
				if rolls.item (it.item) = 10 then
					strike := strike + rolls.item (it.item + 1) + rolls.item (it.item + 2)
				end
				if rolls.item (it.item) /= 10 and it.item \\ 2 = 0 and (rolls.item (it.item) + rolls.item (it.item + 1)) = 10 then
					scores := scores + rolls.item (it.item + 2)
				end
				scores := scores + rolls.item(it.item)
			end

			-- It's a perfect game if strikes is greater than 200
			if strike > 200 then
				strike := 180
			end

			Result := strike + scores
		ensure
			return_not_void: Result /= Void
		end
end
