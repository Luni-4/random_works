note
	description: "Summary description for {RECTANGLE}."
	author: ""
	date: "$Date$"
	revision: "$Revision$"

class
	RECTANGLE

inherit

	POLYGON
		redefine
			area,
			perimeter,
			n_vertices,
			max_edge,
			min_edge
		end

create
	make

feature

	make (height, width: REAL)
		do
			x := width
			y := height
		end

	n_vertices: INTEGER
		do
			Result := 4
		end

	area: REAL
		do
			Result := x * y
		ensure then
			area_is_not_negative: Result >= 0
			area_equal: Result = x * y
		end

	perimeter: REAL
		do
			Result := 2 * (x + y)
		ensure then
			perimeter_is_not_negative: Result >= 0
			permiter_equal: Result = 2*(x+y)
		end

	rotate (angle: REAL)
		require
			angle_is_multiple_90: (angle.floor \\ 90) = 0
		local
			a, tmp: REAL
		do
			a := angle.abs
			from
				a := angle.abs
			until
				a <= 0
			loop
				a := a - 90.
				tmp := x
				x := y
				y := tmp
			end
		ensure
			same_or_swapped_width: x = old x or x = old y
			same_or_swapped_height: y = old y or y = old x
			equal_perimeter: perimeter = old perimeter
			equal_area: area = old area
		end

	max_edge: REAL
		do
			Result := x.max (y)
		end

	min_edge: REAL
		do
			Result := x.min (y)
		end

feature {NONE}

	x, y: REAL

invariant
	non_negative_edges: x >= 0.0 and y >= 0.0

end
