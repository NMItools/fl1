CREATE EXTENSION postgis;

CREATE TABLE IF NOT EXISTS public.test_table
(
    id uuid NOT NULL,
    zip text COLLATE pg_catalog."default",
    type smallint,
    lon double precision,
    lat double precision,
    geom geometry,
    CONSTRAINT test_table_pkey PRIMARY KEY (id),
    CONSTRAINT enforce_dims_geom CHECK (st_ndims(geom) = 2),
    CONSTRAINT enforce_geotype_geom CHECK (geometrytype(geom) = 'POINT'::text OR geom IS NULL),
    CONSTRAINT enforce_srid_geom CHECK (st_srid(geom) = 4326)
) TABLESPACE pg_default;
ALTER TABLE IF EXISTS public.test_table OWNER to postgres;
CREATE INDEX test_table_geom_gist ON public.test_table USING gist (geom);