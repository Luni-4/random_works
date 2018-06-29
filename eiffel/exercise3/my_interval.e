note
	description: "Esame di Sviluppo software in gruppi di lavoro complessi"
	author: "Mattia Monga"

	-- Dopo aver analizzato la classe MY_INTERVAL, rispondere editando il codice
	-- o il file risposte.txt a seconda del caso:
	-- 1. modificare la post-condizione di make, in modo che rispecchi il
	-- commento che ne descrive il comportamento.
	-- 2. la feature is_empty non ha nessuna post-condizione. Discuterne i
	-- motivi.
	-- 3. dopo averne definito il contratto, implementare la feature extend_to
	-- che estende l'intervallo fino a includere l'intero passato come
	-- parametro.

class
	MY_INTERVAL

create
	make

feature

	make (l, u: INTEGER)
		do
			-- Set bounds to l and u;make interval empty if l > u.	
			lower := l
			upper := u
		ensure
		    not_void: l < u and (lower = l and upper = u)
		    void_condition: l > u = is_empty
		end

feature -- Access

	lower: INTEGER

	upper: INTEGER

feature -- Comparison

	is_comparable (other: like Current): BOOLEAN
			-- Is either one of current interval and other
			-- strictly contained in the other?
		do
			Result := (Current < other) or (Current ~ other) or (Current > other)
		ensure
			definition: Result = (Current < other) or (Current ~ other) or (Current > other)
		end

	is_subinterval alias "<" (other: like Current): BOOLEAN
			-- Is current interval strictly included in other?
		do
			Result := lower > other.lower and upper < other.upper
		ensure
			definition: Result =  (lower > other.lower and upper < other.upper)
		end

	is_superinterval alias ">" (other: like Current): BOOLEAN
			-- Does current interval strictly include other?
		do
			Result := other < Current
		ensure
			definition: Result = (other < Current)
		end

	extend_to (i: INTEGER)
		do
			if i < lower then
				lower := i
			end
			if i > upper then
				upper := i
			end
		ensure
			equal_or_bigger: (Current ~ old Current) or else (Current > old Current)
		end

feature -- Status report

	is_empty: BOOLEAN
			-- Does interval contain no values?
		do
			Result := lower > upper
		end

invariant
	empty_if_no_values: is_empty = (lower > upper)

end
