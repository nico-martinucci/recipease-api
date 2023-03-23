--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ingredient_categories; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.ingredient_categories (
    name text NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.ingredient_categories OWNER TO nicom;

--
-- Name: ingredients; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.ingredients (
    name text NOT NULL,
    description text NOT NULL,
    category text NOT NULL,
    photo_url text
);


ALTER TABLE public.ingredients OWNER TO nicom;

--
-- Name: meals; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.meals (
    name text NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.meals OWNER TO nicom;

--
-- Name: recipe_comments; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.recipe_comments (
    id integer NOT NULL,
    user_username text NOT NULL,
    recipe_id integer NOT NULL,
    comment text NOT NULL,
    time_stamp timestamp with time zone NOT NULL
);


ALTER TABLE public.recipe_comments OWNER TO nicom;

--
-- Name: recipe_comments_id_seq; Type: SEQUENCE; Schema: public; Owner: nicom
--

CREATE SEQUENCE public.recipe_comments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipe_comments_id_seq OWNER TO nicom;

--
-- Name: recipe_comments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicom
--

ALTER SEQUENCE public.recipe_comments_id_seq OWNED BY public.recipe_comments.id;


--
-- Name: recipe_items; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.recipe_items (
    id integer NOT NULL,
    recipe_id integer NOT NULL,
    "order" integer NOT NULL,
    amount integer NOT NULL,
    short_unit text,
    ingredient text NOT NULL,
    description text
);


ALTER TABLE public.recipe_items OWNER TO nicom;

--
-- Name: recipe_items_id_seq; Type: SEQUENCE; Schema: public; Owner: nicom
--

CREATE SEQUENCE public.recipe_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipe_items_id_seq OWNER TO nicom;

--
-- Name: recipe_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicom
--

ALTER SEQUENCE public.recipe_items_id_seq OWNED BY public.recipe_items.id;


--
-- Name: recipe_steps; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.recipe_steps (
    id integer NOT NULL,
    recipe_id integer NOT NULL,
    "order" integer NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.recipe_steps OWNER TO nicom;

--
-- Name: recipe_steps_id_seq; Type: SEQUENCE; Schema: public; Owner: nicom
--

CREATE SEQUENCE public.recipe_steps_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipe_steps_id_seq OWNER TO nicom;

--
-- Name: recipe_steps_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicom
--

ALTER SEQUENCE public.recipe_steps_id_seq OWNED BY public.recipe_steps.id;


--
-- Name: recipe_types; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.recipe_types (
    name text NOT NULL,
    description text NOT NULL
);


ALTER TABLE public.recipe_types OWNER TO nicom;

--
-- Name: recipes; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.recipes (
    id integer NOT NULL,
    name text NOT NULL,
    user_username text NOT NULL,
    meal_name text NOT NULL,
    type_name text NOT NULL,
    private boolean NOT NULL,
    photo_url text
);


ALTER TABLE public.recipes OWNER TO nicom;

--
-- Name: recipes_id_seq; Type: SEQUENCE; Schema: public; Owner: nicom
--

CREATE SEQUENCE public.recipes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipes_id_seq OWNER TO nicom;

--
-- Name: recipes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicom
--

ALTER SEQUENCE public.recipes_id_seq OWNED BY public.recipes.id;


--
-- Name: recipes_ingredients_search; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.recipes_ingredients_search (
    id integer NOT NULL,
    recipe_id integer,
    ingredient_name text
);


ALTER TABLE public.recipes_ingredients_search OWNER TO nicom;

--
-- Name: recipes_ingredients_search_id_seq; Type: SEQUENCE; Schema: public; Owner: nicom
--

CREATE SEQUENCE public.recipes_ingredients_search_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipes_ingredients_search_id_seq OWNER TO nicom;

--
-- Name: recipes_ingredients_search_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicom
--

ALTER SEQUENCE public.recipes_ingredients_search_id_seq OWNED BY public.recipes_ingredients_search.id;


--
-- Name: units; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.units (
    short text NOT NULL,
    singular text NOT NULL,
    plural text NOT NULL
);


ALTER TABLE public.units OWNER TO nicom;

--
-- Name: users; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.users (
    username text NOT NULL,
    email text NOT NULL,
    password text NOT NULL,
    first_name text NOT NULL,
    last_name text NOT NULL,
    photo_url text,
    bio text
);


ALTER TABLE public.users OWNER TO nicom;

--
-- Name: users_recipes; Type: TABLE; Schema: public; Owner: nicom
--

CREATE TABLE public.users_recipes (
    id integer NOT NULL,
    user_username text NOT NULL,
    recipe_id integer NOT NULL,
    notes text,
    is_starred boolean,
    is_made boolean,
    rating integer
);


ALTER TABLE public.users_recipes OWNER TO nicom;

--
-- Name: users_recipes_id_seq; Type: SEQUENCE; Schema: public; Owner: nicom
--

CREATE SEQUENCE public.users_recipes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_recipes_id_seq OWNER TO nicom;

--
-- Name: users_recipes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: nicom
--

ALTER SEQUENCE public.users_recipes_id_seq OWNED BY public.users_recipes.id;


--
-- Name: recipe_comments id; Type: DEFAULT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_comments ALTER COLUMN id SET DEFAULT nextval('public.recipe_comments_id_seq'::regclass);


--
-- Name: recipe_items id; Type: DEFAULT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_items ALTER COLUMN id SET DEFAULT nextval('public.recipe_items_id_seq'::regclass);


--
-- Name: recipe_steps id; Type: DEFAULT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_steps ALTER COLUMN id SET DEFAULT nextval('public.recipe_steps_id_seq'::regclass);


--
-- Name: recipes id; Type: DEFAULT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes ALTER COLUMN id SET DEFAULT nextval('public.recipes_id_seq'::regclass);


--
-- Name: recipes_ingredients_search id; Type: DEFAULT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes_ingredients_search ALTER COLUMN id SET DEFAULT nextval('public.recipes_ingredients_search_id_seq'::regclass);


--
-- Name: users_recipes id; Type: DEFAULT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.users_recipes ALTER COLUMN id SET DEFAULT nextval('public.users_recipes_id_seq'::regclass);


--
-- Data for Name: ingredient_categories; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.ingredient_categories (name, description) FROM stdin;
meat	test
seafood	test
vegetable	test
fruit	test
dairy	test
grain	test
spice	test
packaged	test
other	test
\.


--
-- Data for Name: ingredients; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.ingredients (name, description, category, photo_url) FROM stdin;
chicken, boneless/skinless thighs	test	meat	\N
chicken, boneless/skinless breasts	test	meat	\N
chicken, whole	test	meat	\N
pork, chop	test	meat	\N
pork, boneless shoulder	test	meat	\N
beef, ribeye steak	test	meat	\N
beef, chuck roast	test	meat	\N
salmon, filets	test	seafood	\N
salmon, whole	test	seafood	\N
shrimp, peeled/deveined	test	seafood	\N
crab	test	seafood	\N
crab, picked meat	test	seafood	\N
kale	test	vegetable	\N
broccoli	test	vegetable	\N
arugula	test	vegetable	\N
romaine lettuce	test	vegetable	\N
brussel sprouts	test	vegetable	\N
tomatoes, cherry	test	vegetable	\N
tomatoes, slicing	test	vegetable	\N
apples, fuji	test	fruit	\N
orange, navel	test	fruit	\N
pear, bartlett	test	fruit	\N
blueberries	test	fruit	\N
strawberries	test	fruit	\N
banana	test	fruit	\N
milk, skim	test	dairy	\N
milk, 2%	test	dairy	\N
milk, whole	test	dairy	\N
cheese, jack	test	dairy	\N
cheese, gouda	test	dairy	\N
eggs	test	dairy	\N
heavy cream	test	dairy	\N
bread	test	grain	\N
rice, white long-grain	test	grain	\N
rice, brown	test	grain	\N
tortillas, corn	test	grain	\N
tortillas, flour	test	grain	\N
salt	test	spice	\N
pepper	test	spice	\N
paprika	test	spice	\N
ginger, ground	test	spice	\N
soy sauce	test	packaged	\N
fish sauce	test	packaged	\N
tomato, canned	test	packaged	\N
tomato, paste	test	packaged	\N
\.


--
-- Data for Name: meals; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.meals (name, description) FROM stdin;
breakfast	the first (and arguably) most important meal of the day
brunch	it's all the rage
lunch	salads, sandwiches, and leftovers
dinner	it's dinner, what do you want from me
dessert	the last (and arguably) also most important meal of the day
snack	be it midnight or middle-of-the-day, sometimes you need a little nosh
\.


--
-- Data for Name: recipe_comments; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipe_comments (id, user_username, recipe_id, comment, time_stamp) FROM stdin;
\.


--
-- Data for Name: recipe_items; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipe_items (id, recipe_id, "order", amount, short_unit, ingredient, description) FROM stdin;
\.


--
-- Data for Name: recipe_steps; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipe_steps (id, recipe_id, "order", description) FROM stdin;
\.


--
-- Data for Name: recipe_types; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipe_types (name, description) FROM stdin;
main dish	test
side dish	test
salad	test
beverage	test
condiment	test
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipes (id, name, user_username, meal_name, type_name, private, photo_url) FROM stdin;
\.


--
-- Data for Name: recipes_ingredients_search; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipes_ingredients_search (id, recipe_id, ingredient_name) FROM stdin;
\.


--
-- Data for Name: units; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.units (short, singular, plural) FROM stdin;
c	cup	cups
tbsp	tablespoon	tablespoons
tsp	teaspoon	teaspoons
fl oz	fluid ounce	fluid ounces
pt	pint	pints
qt	quart	quarts
gal	gallon	gallons
oz	ounce	ounces
lb	pound	pounds
g	gram	grams
kg	kilogram	kilograms
pinch	pinch	pinches
dash	dash	dashes
bunch	bunch	bunches
slice	slice	slices
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.users (username, email, password, first_name, last_name, photo_url, bio) FROM stdin;
\.


--
-- Data for Name: users_recipes; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.users_recipes (id, user_username, recipe_id, notes, is_starred, is_made, rating) FROM stdin;
\.


--
-- Name: recipe_comments_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicom
--

SELECT pg_catalog.setval('public.recipe_comments_id_seq', 1, false);


--
-- Name: recipe_items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicom
--

SELECT pg_catalog.setval('public.recipe_items_id_seq', 1, false);


--
-- Name: recipe_steps_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicom
--

SELECT pg_catalog.setval('public.recipe_steps_id_seq', 1, false);


--
-- Name: recipes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicom
--

SELECT pg_catalog.setval('public.recipes_id_seq', 1, false);


--
-- Name: recipes_ingredients_search_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicom
--

SELECT pg_catalog.setval('public.recipes_ingredients_search_id_seq', 1, false);


--
-- Name: users_recipes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: nicom
--

SELECT pg_catalog.setval('public.users_recipes_id_seq', 1, false);


--
-- Name: ingredient_categories ingredient_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.ingredient_categories
    ADD CONSTRAINT ingredient_categories_pkey PRIMARY KEY (name);


--
-- Name: ingredients ingredients_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.ingredients
    ADD CONSTRAINT ingredients_pkey PRIMARY KEY (name);


--
-- Name: meals meals_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.meals
    ADD CONSTRAINT meals_pkey PRIMARY KEY (name);


--
-- Name: recipe_comments recipe_comments_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_comments
    ADD CONSTRAINT recipe_comments_pkey PRIMARY KEY (id);


--
-- Name: recipe_items recipe_items_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_items
    ADD CONSTRAINT recipe_items_pkey PRIMARY KEY (id);


--
-- Name: recipe_steps recipe_steps_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_steps
    ADD CONSTRAINT recipe_steps_pkey PRIMARY KEY (id);


--
-- Name: recipe_types recipe_types_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_types
    ADD CONSTRAINT recipe_types_pkey PRIMARY KEY (name);


--
-- Name: recipes_ingredients_search recipes_ingredients_search_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes_ingredients_search
    ADD CONSTRAINT recipes_ingredients_search_pkey PRIMARY KEY (id);


--
-- Name: recipes recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_pkey PRIMARY KEY (id);


--
-- Name: units units_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.units
    ADD CONSTRAINT units_pkey PRIMARY KEY (short);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users_recipes users_recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.users_recipes
    ADD CONSTRAINT users_recipes_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: ingredients ingredients_category_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.ingredients
    ADD CONSTRAINT ingredients_category_fkey FOREIGN KEY (category) REFERENCES public.ingredient_categories(name);


--
-- Name: recipe_comments recipe_comments_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_comments
    ADD CONSTRAINT recipe_comments_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: recipe_comments recipe_comments_user_username_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_comments
    ADD CONSTRAINT recipe_comments_user_username_fkey FOREIGN KEY (user_username) REFERENCES public.users(username);


--
-- Name: recipe_items recipe_items_ingredient_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_items
    ADD CONSTRAINT recipe_items_ingredient_fkey FOREIGN KEY (ingredient) REFERENCES public.ingredients(name);


--
-- Name: recipe_items recipe_items_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_items
    ADD CONSTRAINT recipe_items_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: recipe_items recipe_items_short_unit_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_items
    ADD CONSTRAINT recipe_items_short_unit_fkey FOREIGN KEY (short_unit) REFERENCES public.units(short);


--
-- Name: recipe_steps recipe_steps_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipe_steps
    ADD CONSTRAINT recipe_steps_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: recipes_ingredients_search recipes_ingredients_search_ingredient_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes_ingredients_search
    ADD CONSTRAINT recipes_ingredients_search_ingredient_name_fkey FOREIGN KEY (ingredient_name) REFERENCES public.ingredients(name);


--
-- Name: recipes_ingredients_search recipes_ingredients_search_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes_ingredients_search
    ADD CONSTRAINT recipes_ingredients_search_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: recipes recipes_meal_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_meal_name_fkey FOREIGN KEY (meal_name) REFERENCES public.meals(name);


--
-- Name: recipes recipes_type_name_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_type_name_fkey FOREIGN KEY (type_name) REFERENCES public.recipe_types(name);


--
-- Name: recipes recipes_user_username_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.recipes
    ADD CONSTRAINT recipes_user_username_fkey FOREIGN KEY (user_username) REFERENCES public.users(username);


--
-- Name: users_recipes users_recipes_recipe_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.users_recipes
    ADD CONSTRAINT users_recipes_recipe_id_fkey FOREIGN KEY (recipe_id) REFERENCES public.recipes(id);


--
-- Name: users_recipes users_recipes_user_username_fkey; Type: FK CONSTRAINT; Schema: public; Owner: nicom
--

ALTER TABLE ONLY public.users_recipes
    ADD CONSTRAINT users_recipes_user_username_fkey FOREIGN KEY (user_username) REFERENCES public.users(username);


--
-- PostgreSQL database dump complete
--

