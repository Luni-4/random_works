note
	description: "TestingEiffel application root class"
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
		local
			s, m: MY_INTERVAL-- Run application.
		do
			--| Add your code here
			create s.make(1,2)
			create m.make(50,100)
			print(s.is_subinterval (m))
		end

end
