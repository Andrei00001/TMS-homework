--
-- PostgreSQL database dump
--

-- Dumped from database version 14.2
-- Dumped by pg_dump version 14.2

-- Started on 2022-04-20 10:51:46

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: -
--

CREATE SCHEMA public;


--
-- TOC entry 3345 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 217 (class 1259 OID 16713)
-- Name: comments; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.comments (
    id integer NOT NULL,
    text character varying NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


--
-- TOC entry 216 (class 1259 OID 16712)
-- Name: comments_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.comments ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.comments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 215 (class 1259 OID 16697)
-- Name: likes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.likes (
    id integer NOT NULL,
    user_id integer NOT NULL,
    post_id integer NOT NULL
);


--
-- TOC entry 214 (class 1259 OID 16696)
-- Name: likes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.likes ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.likes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 213 (class 1259 OID 16684)
-- Name: posts; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.posts (
    id integer NOT NULL,
    title character varying NOT NULL,
    description character varying NOT NULL,
    user_id integer NOT NULL
);


--
-- TOC entry 212 (class 1259 OID 16683)
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public.posts ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.posts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 16678)
-- Name: user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    name character varying(54) NOT NULL,
    age integer NOT NULL,
    gender character varying(30) NOT NULL,
    nationality character varying(60) NOT NULL
);


--
-- TOC entry 210 (class 1259 OID 16677)
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

ALTER TABLE public."user" ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3339 (class 0 OID 16713)
-- Dependencies: 217
-- Data for Name: comments; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (1, 'lalala', 1, 5);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (2, 'blabla', 2, 1);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (3, 'lilili', 3, 5);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (4, 'kurlak', 1, 2);
INSERT INTO public.comments OVERRIDING SYSTEM VALUE VALUES (5, 'gnomiki', 4, 5);


--
-- TOC entry 3337 (class 0 OID 16697)
-- Dependencies: 215
-- Data for Name: likes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (1, 4, 1);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (2, 2, 3);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (3, 4, 2);
INSERT INTO public.likes OVERRIDING SYSTEM VALUE VALUES (4, 4, 5);


--
-- TOC entry 3335 (class 0 OID 16684)
-- Dependencies: 213
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (1, 'Hi', 'sql', 1);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (2, 'Hi1', 'sql1', 3);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (3, 'Hi2', 'sql2 ', 2);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (4, 'Hi3', 'sql3', 4);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (5, 'Hi4', 'sql4', 5);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (6, 'Hi5', 'sql5', 1);
INSERT INTO public.posts OVERRIDING SYSTEM VALUE VALUES (7, 'Hi6', 'sql6', 4);


--
-- TOC entry 3333 (class 0 OID 16678)
-- Dependencies: 211
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public."user" OVERRIDING SYSTEM VALUE VALUES (1, 'Andrei', 14, 'm', 'R');
INSERT INTO public."user" OVERRIDING SYSTEM VALUE VALUES (2, 'Grigorii', 20, 'm', 'R');
INSERT INTO public."user" OVERRIDING SYSTEM VALUE VALUES (3, 'Kirill', 19, 'm', 'S');
INSERT INTO public."user" OVERRIDING SYSTEM VALUE VALUES (4, 'Fedor', 40, 'm', 'S');
INSERT INTO public."user" OVERRIDING SYSTEM VALUE VALUES (5, 'Vikor', 90, 'm', 'U');


--
-- TOC entry 3346 (class 0 OID 0)
-- Dependencies: 216
-- Name: comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.comments_id_seq', 5, true);


--
-- TOC entry 3347 (class 0 OID 0)
-- Dependencies: 214
-- Name: likes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.likes_id_seq', 4, true);


--
-- TOC entry 3348 (class 0 OID 0)
-- Dependencies: 212
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.posts_id_seq', 7, true);


--
-- TOC entry 3349 (class 0 OID 0)
-- Dependencies: 210
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_id_seq', 5, true);


--
-- TOC entry 3187 (class 2606 OID 16719)
-- Name: comments comments_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pk PRIMARY KEY (id);


--
-- TOC entry 3185 (class 2606 OID 16701)
-- Name: likes likes_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_pk PRIMARY KEY (id);


--
-- TOC entry 3183 (class 2606 OID 16690)
-- Name: posts posts_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pk PRIMARY KEY (id);


--
-- TOC entry 3181 (class 2606 OID 16682)
-- Name: user user_pk; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pk PRIMARY KEY (id);


--
-- TOC entry 3191 (class 2606 OID 16720)
-- Name: comments comments_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3192 (class 2606 OID 16725)
-- Name: comments comments_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_fk_1 FOREIGN KEY (post_id) REFERENCES public.posts(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3189 (class 2606 OID 16702)
-- Name: likes likes_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3190 (class 2606 OID 16707)
-- Name: likes likes_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.likes
    ADD CONSTRAINT likes_fk_1 FOREIGN KEY (post_id) REFERENCES public.posts(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3188 (class 2606 OID 16691)
-- Name: posts posts_fk; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2022-04-20 10:51:47

--
-- PostgreSQL database dump complete
--

