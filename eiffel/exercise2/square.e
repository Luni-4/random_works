note
	description: "Summary description for {SQUARE}."
	author: ""
	date: "$Date$"
	revision: "$Revision$"

class
	SQUARE

inherit

	RECTANGLE

create
	make_with_edge

feature

	make_with_edge (width: REAL)
		do
			make (width, width)
		end

invariant
	x = y

end
