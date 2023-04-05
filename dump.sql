--
-- PostgreSQL database dump
-- "psql recipease < dump.sql" to re-seed

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
salsa	test	packaged	\N
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
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.users (username, email, password, first_name, last_name, photo_url, bio) FROM stdin;
\.


--
-- Data for Name: recipes; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipes (id, name, user_username, meal_name, type_name, private, photo_url) FROM stdin;
\.


--
-- Data for Name: recipe_comments; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipe_comments (id, user_username, recipe_id, comment, time_stamp) FROM stdin;
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
jar	jar	jars
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
-- Data for Name: recipes_ingredients_search; Type: TABLE DATA; Schema: public; Owner: nicom
--

COPY public.recipes_ingredients_search (id, recipe_id, ingredient_name) FROM stdin;
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
-- PostgreSQL database dump complete
--

