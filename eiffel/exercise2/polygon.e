note
	description: "Summary description for {POLYGON}."
	author: ""
	date: "$Date$"
	revision: "$Revision$"

deferred class
	POLYGON

feature

	area: REAL
		deferred
		ensure
			Result >= 0.0
		end

	perimeter: REAL
		deferred
		ensure
			Result >= 0.0
		end

	n_vertices: INTEGER
		deferred
		ensure
			Result >= 3
		end

	max_edge: REAL
		deferred
		ensure
			Result >= 0.0
		end

	min_edge: REAL
		deferred
		ensure
			Result >= 0.0
		end

end
