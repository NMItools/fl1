-- FUNCTION: public.cnt_within_dist(text, text, integer)

-- DROP FUNCTION public.cnt_within_dist(text, text, integer);

CREATE OR REPLACE FUNCTION public.cnt_within_dist(
    lon text,
    lat text,
	miles integer)
    RETURNS TABLE(row_count bigint)
    LANGUAGE 'plpgsql'
    COST 100
    VOLATILE PARALLEL UNSAFE
	ROWS 1
AS $BODY$
DECLARE
	query_ text :=  'SELECT COUNT(*) FROM test_table WHERE ST_DWithin(geom, ''SRID=4326;POINT(' || $1 || ' ' || $2 || ')'', 0.0212*' || $3 || ')';
BEGIN 
    RAISE NOTICE 'query_: %', query_;
 	RETURN QUERY 
 	EXECUTE query_ USING $1, $2, $3;
END
$BODY$;

ALTER FUNCTION public.cnt_within_dist(text, text, integer)
    OWNER TO postgres;
