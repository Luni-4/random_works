note
	description: "tester application root class"
	date: "$Date$"
	revision: "$Revision$"

class
	APPLICATION

inherit
	ARGUMENTS

create
	make

feature {NONE} -- Initialization

	make
		local b: RECTANGLE
		-- Run application.
		do
			create b.make(1,2)
			b.rotate(0)
			--| Add your code here
			print ("Hello Eiffel World!%N")
		end

end
