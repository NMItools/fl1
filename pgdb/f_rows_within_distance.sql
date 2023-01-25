-- FUNCTION: public.rows_within_dist(text, text, integer)

-- DROP FUNCTION public.rows_within_dist(text, text, integer);

CREATE OR REPLACE FUNCTION public.rows_within_dist(
	longitude text,
    latitude text,
	miles integer
)
    RETURNS TABLE(
		uid uuid,
		zip text,
		stype smallint,
		lon double precision,
		lat double precision,
		geom geometry)
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
AS $BODY$
DECLARE
	query_ text :=  'SELECT * FROM test_table WHERE ST_DWithin(geom, ''SRID=4326;POINT(' || $1 || ' ' || $2 || ')'', 0.0212*' || $3 || ')';
BEGIN 
--     RAISE NOTICE 'query_: %', query_;
  	RETURN QUERY 
 	EXECUTE query_ USING $1, $2, $3;
END
$BODY$;

ALTER FUNCTION public.rows_within_dist(text, text, integer)
    OWNER TO postgres;
