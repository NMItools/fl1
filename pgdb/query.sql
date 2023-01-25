-- SELECT st_distance(geom, 'SRID=4326;POINT(-88 46)'::geometry) as distance
-- FROM test_table
-- ORDER BY geom <-> 'SRID=4326;POINT(-88 46)'::geometry limit 100;

SELECT COUNT(*) FROM test_table
  WHERE ST_DWithin(geom, 'SRID=4326;POINT(-88 46)', 0.212);
  
SELECT * FROM test_table
  WHERE ST_DWithin(geom, 'SRID=4326;POINT(-88 46)', 0.212);
  
  
SELECT 'SELECT COUNT(*) FROM test_table WHERE ST_DWithin(geom, ''SRID=4326;POINT(' || -88 || ' ' || 46 || ')'', 0.0212*' || 10 || ')';

SELECT COUNT(*) FROM test_table WHERE ST_DWithin(geom, 'SRID=4326;POINT(-88 46)', 0.0212*10)