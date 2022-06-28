--
-- PostgreSQL database dump
--

-- Dumped from database version 10.16
-- Dumped by pg_dump version 13.3

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

--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO taprete;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO taprete;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO taprete;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO taprete;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO taprete;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO taprete;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO taprete;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO taprete;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO taprete;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO taprete;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO taprete;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO taprete;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO taprete;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO taprete;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO taprete;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO taprete;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO taprete;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO taprete;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO taprete;

--
-- Name: exercises_dailyworkouts; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.exercises_dailyworkouts (
    id bigint NOT NULL,
    workout_date date NOT NULL,
    total_workouts integer NOT NULL,
    status character varying(8) NOT NULL
);


ALTER TABLE public.exercises_dailyworkouts OWNER TO taprete;

--
-- Name: exercises_dailyworkouts_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.exercises_dailyworkouts_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercises_dailyworkouts_id_seq OWNER TO taprete;

--
-- Name: exercises_dailyworkouts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.exercises_dailyworkouts_id_seq OWNED BY public.exercises_dailyworkouts.id;


--
-- Name: exercises_exercise; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.exercises_exercise (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    muscle_target character varying(20) NOT NULL,
    secondary_target character varying(20),
    push_pull character varying(20),
    muscle_group character varying(20),
    diffulty_level integer,
    equipment boolean,
    resistance_type character varying(50)
);


ALTER TABLE public.exercises_exercise OWNER TO taprete;

--
-- Name: exercises_exercise_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.exercises_exercise_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercises_exercise_id_seq OWNER TO taprete;

--
-- Name: exercises_exercise_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.exercises_exercise_id_seq OWNED BY public.exercises_exercise.id;


--
-- Name: exercises_workout; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.exercises_workout (
    id bigint NOT NULL,
    workout_date date NOT NULL,
    workout_target character varying(50),
    total_rounds integer
);


ALTER TABLE public.exercises_workout OWNER TO taprete;

--
-- Name: exercises_workout_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.exercises_workout_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercises_workout_id_seq OWNER TO taprete;

--
-- Name: exercises_workout_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.exercises_workout_id_seq OWNED BY public.exercises_workout.id;


--
-- Name: exercises_workoutexercise; Type: TABLE; Schema: public; Owner: taprete
--

CREATE TABLE public.exercises_workoutexercise (
    id bigint NOT NULL,
    "order" integer NOT NULL,
    exercise_id bigint NOT NULL,
    workout_id bigint NOT NULL
);


ALTER TABLE public.exercises_workoutexercise OWNER TO taprete;

--
-- Name: exercises_workoutexercise_id_seq; Type: SEQUENCE; Schema: public; Owner: taprete
--

CREATE SEQUENCE public.exercises_workoutexercise_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.exercises_workoutexercise_id_seq OWNER TO taprete;

--
-- Name: exercises_workoutexercise_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: taprete
--

ALTER SEQUENCE public.exercises_workoutexercise_id_seq OWNED BY public.exercises_workoutexercise.id;


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Name: exercises_dailyworkouts id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_dailyworkouts ALTER COLUMN id SET DEFAULT nextval('public.exercises_dailyworkouts_id_seq'::regclass);


--
-- Name: exercises_exercise id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_exercise ALTER COLUMN id SET DEFAULT nextval('public.exercises_exercise_id_seq'::regclass);


--
-- Name: exercises_workout id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_workout ALTER COLUMN id SET DEFAULT nextval('public.exercises_workout_id_seq'::regclass);


--
-- Name: exercises_workoutexercise id; Type: DEFAULT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_workoutexercise ALTER COLUMN id SET DEFAULT nextval('public.exercises_workoutexercise_id_seq'::regclass);


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add exercise	7	add_exercise
26	Can change exercise	7	change_exercise
27	Can delete exercise	7	delete_exercise
28	Can view exercise	7	view_exercise
29	Can add workout	8	add_workout
30	Can change workout	8	change_workout
31	Can delete workout	8	delete_workout
32	Can view workout	8	view_workout
33	Can add workout exercise	9	add_workoutexercise
34	Can change workout exercise	9	change_workoutexercise
35	Can delete workout exercise	9	delete_workoutexercise
36	Can view workout exercise	9	view_workoutexercise
37	Can add daily workouts	10	add_dailyworkouts
38	Can change daily workouts	10	change_dailyworkouts
39	Can delete daily workouts	10	delete_dailyworkouts
40	Can view daily workouts	10	view_dailyworkouts
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$320000$P0JvqY9qU7tAIS9nzBl8AY$ymnvyKgWm/5B8ZI3ra5/wVwY88Axiwmn2c0ZXbxPveI=	2022-06-28 10:29:45.128069-05	t	taprete				t	t	2022-06-28 10:29:37.019594-05
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-06-28 10:44:51.28057-05	119	Standard push-ups	3		7	1
2	2022-06-28 10:47:14.624265-05	142	Step-back Lunges	3		7	1
3	2022-06-28 10:47:14.638703-05	141	Lunge Runner	3		7	1
4	2022-06-28 10:47:14.640535-05	140	pushup Jacks	3		7	1
5	2022-06-28 10:47:14.641777-05	139	Blast-off pushup	3		7	1
6	2022-06-28 10:47:14.642813-05	138	Long Jump backward Hop	3		7	1
7	2022-06-28 10:47:14.643816-05	137	Dumbell pull Over	3		7	1
8	2022-06-28 10:47:14.646697-05	136	One-Arm Balance push-ups	3		7	1
9	2022-06-28 10:47:14.647717-05	135	Front-to-back Tricep Extensions	3		7	1
10	2022-06-28 10:47:14.648564-05	134	Clap or Plyo push-ups	3		7	1
11	2022-06-28 10:47:14.649404-05	133	One Arm push-ups	3		7	1
12	2022-06-28 10:47:14.650267-05	132	Side-to-Side push-ups	3		7	1
13	2022-06-28 10:47:14.651055-05	131	Two Twitch Speed push-ups	3		7	1
14	2022-06-28 10:47:14.651851-05	130	Plange push-ups	3		7	1
15	2022-06-28 10:47:14.652731-05	129	Slow-Motion 3-in-1 push-ups	3		7	1
16	2022-06-28 10:47:14.653514-05	128	Switch Grip pull Ups	3		7	1
17	2022-06-28 10:47:14.654332-05	127	back flys	3		7	1
18	2022-06-28 10:47:14.657161-05	126	Dive-bomber push-ups	3		7	1
19	2022-06-28 10:47:14.658104-05	125	Diamond push-ups	3		7	1
20	2022-06-28 10:47:14.658922-05	124	Decline push-ups	3		7	1
21	2022-06-28 10:47:14.659708-05	123	Close Grip Overhand pull-ups	3		7	1
22	2022-06-28 10:47:14.660441-05	122	Wide Fly push-ups	3		7	1
23	2022-06-28 10:47:14.661231-05	121	Military push-ups	3		7	1
24	2022-06-28 10:47:14.661937-05	120	Wide Front pull-ups	3		7	1
25	2022-06-28 11:09:07.473538-05	194	Step-back Lunges	3		7	1
26	2022-06-28 11:09:07.476878-05	193	Lunge Runner	3		7	1
27	2022-06-28 11:09:07.477869-05	192	Push-Up Jacks	3		7	1
28	2022-06-28 11:09:07.478754-05	191	Blast-off Push-Ups	3		7	1
29	2022-06-28 11:09:07.479752-05	190	Long Jump backward Hop	3		7	1
30	2022-06-28 11:09:07.480625-05	189	Curl-Up/Hammer Downs	3		7	1
31	2022-06-28 11:09:07.481526-05	188	Chin-Ups	3		7	1
32	2022-06-28 11:09:07.482246-05	187	One-Arm Balance Push-Ups	3		7	1
33	2022-06-28 11:09:07.482964-05	186	Front-to-back Tricep Extensions	3		7	1
34	2022-06-28 11:09:07.483671-05	185	Clap or Plyo Push-Ups	3		7	1
35	2022-06-28 11:09:07.484635-05	184	One Arm Push-Ups	3		7	1
36	2022-06-28 11:09:07.485413-05	183	Side-to-Side Push-Ups	3		7	1
37	2022-06-28 11:09:07.486191-05	182	Two Twitch Speed Push-Ups	3		7	1
38	2022-06-28 11:09:07.489803-05	181	Plange Push-Ups	3		7	1
39	2022-06-28 11:09:07.490816-05	180	Slow-Motion 3-in-1 Push-Ups	3		7	1
40	2022-06-28 11:09:07.491692-05	179	Switch Grip pull Ups	3		7	1
41	2022-06-28 11:09:07.492566-05	178	Back Flys	3		7	1
42	2022-06-28 11:09:07.493429-05	177	Dive-bomber Push-Ups	3		7	1
43	2022-06-28 11:09:07.494259-05	176	Lawnmower Pull	3		7	1
44	2022-06-28 11:09:07.495218-05	175	Diamond Push-Ups	3		7	1
45	2022-06-28 11:09:07.496002-05	174	Decline Push-Ups	3		7	1
46	2022-06-28 11:09:07.496715-05	173	Close Grip Overhand Pull-Ups	3		7	1
47	2022-06-28 11:09:07.497425-05	172	Wide Fly Push-Ups	3		7	1
48	2022-06-28 11:09:07.498138-05	171	Military Push-Ups	3		7	1
49	2022-06-28 11:09:07.498875-05	170	Wide Front Pull-Ups	3		7	1
50	2022-06-28 11:09:07.499859-05	169	Standard Push-Ups	3		7	1
51	2022-06-28 11:09:07.500967-05	168	Side V-Up	3		7	1
52	2022-06-28 11:09:07.501999-05	167	Side Plank	3		7	1
53	2022-06-28 11:09:07.503518-05	166	Crunch	3		7	1
54	2022-06-28 11:09:07.504352-05	165	Spiderman Plank	3		7	1
55	2022-06-28 11:09:07.505097-05	164	Twist & Hold	3		7	1
56	2022-06-28 11:09:07.505915-05	163	Tornado	3		7	1
57	2022-06-28 11:09:07.506751-05	162	Bug Bicycle Crunch	3		7	1
58	2022-06-28 11:09:07.507631-05	161	Crunchy Frog	3		7	1
59	2022-06-28 11:09:07.508409-05	160	Abergnome	3		7	1
60	2022-06-28 11:09:07.509165-05	159	Scissors Clapper	3		7	1
61	2022-06-28 11:09:07.509884-05	158	Gate Bridge Lift	3		7	1
62	2022-06-28 11:09:07.510608-05	157	Roll V Hold	3		7	1
63	2022-06-28 11:09:07.511277-05	156	Hip Rock & Raise	3		7	1
64	2022-06-28 11:09:07.511947-05	155	Banana Knee Straight Leg Crunch	3		7	1
65	2022-06-28 11:09:07.512615-05	154	Row the Boat	3		7	1
66	2022-06-28 11:09:07.51328-05	153	Oblique Roll Crunch	3		7	1
67	2022-06-28 11:09:07.513968-05	152	V-Up/Roll Up	3		7	1
68	2022-06-28 11:09:07.514632-05	151	Pulse Ups	3		7	1
69	2022-06-28 11:09:07.515298-05	150	Side Arm Balance Crunch	3		7	1
70	2022-06-28 11:09:07.515964-05	149	Cross Leg / Wide Leg Sit-ups	3		7	1
71	2022-06-28 11:09:07.517443-05	148	Scissor Twist	3		7	1
72	2022-06-28 11:09:07.518282-05	147	Bicycles	3		7	1
73	2022-06-28 11:09:07.519182-05	146	Banana Two Crunch	3		7	1
74	2022-06-28 11:09:07.51996-05	145	Calf Raises	3		7	1
75	2022-06-28 11:09:07.520699-05	144	Adductor Lunge	3		7	1
76	2022-06-28 11:09:07.521452-05	143	Albanian Squat	3		7	1
77	2022-06-28 11:09:07.522247-05	118	Single Leg Wall Squat	3		7	1
78	2022-06-28 11:09:07.522987-05	117	Alternating Side Lunges	3		7	1
79	2022-06-28 11:09:07.523732-05	116	Step-Back Lunges	3		7	1
80	2022-06-28 11:09:07.524451-05	115	Wall Squat	3		7	1
81	2022-06-28 11:09:07.52516-05	114	Toe Tap 360	3		7	1
82	2022-06-28 11:09:07.525876-05	113	1-Leg Squat	3		7	1
83	2022-06-28 11:09:07.526613-05	112	1-Leg Slalom	3		7	1
84	2022-06-28 11:09:07.527387-05	111	Burpee Knee Tuck	3		7	1
85	2022-06-28 11:09:07.528108-05	110	Slalom Line Jump	3		7	1
86	2022-06-28 11:09:07.528808-05	109	Fast Feet Chair Jump	3		7	1
87	2022-06-28 11:09:07.529512-05	108	Wide Leg Tiptoe Squat	3		7	1
88	2022-06-28 11:09:07.530408-05	107	Speed Walkout	3		7	1
89	2022-06-28 11:09:07.531214-05	106	Foot Tuck Jump	3		7	1
90	2022-06-28 11:09:07.531938-05	105	Knee Tuck Jump	3		7	1
91	2022-06-28 11:09:07.532663-05	104	Tuck Jump	3		7	1
92	2022-06-28 11:09:07.533452-05	103	T-Rotation	3		7	1
93	2022-06-28 11:09:07.534135-05	102	Lunge  Runner	3		7	1
94	2022-06-28 11:09:07.534918-05	101	Plank Toe Tap	3		7	1
95	2022-06-28 11:09:07.535893-05	100	Plank Knee Tap	3		7	1
96	2022-06-28 11:09:07.536875-05	99	Plank Hip Tap	3		7	1
97	2022-06-28 11:09:07.53764-05	98	Plank Shoulder Tap	3		7	1
98	2022-06-28 11:09:07.538432-05	97	Plank Elbow Tap	3		7	1
99	2022-06-28 11:09:07.539134-05	96	Plank Hand Tap	3		7	1
100	2022-06-28 11:09:07.53989-05	95	Side to Side Hops	3		7	1
101	2022-06-28 11:09:07.540608-05	94	Pogo Jump	3		7	1
102	2022-06-28 11:09:07.542431-05	93	Single Leg Pogo Jump	3		7	1
103	2022-06-28 11:09:07.543127-05	92	Alternating Fast Feed	3		7	1
104	2022-06-28 11:09:07.543828-05	91	Lateral 3-Step	3		7	1
105	2022-06-28 11:09:07.544515-05	90	Burpee	3		7	1
106	2022-06-28 11:09:07.54519-05	89	Low Box Lateral Runner	3		7	1
107	2022-06-28 11:09:07.545923-05	88	360 Ball Runner / Soccor	3		7	1
108	2022-06-28 11:09:07.546606-05	87	Low Box Runner / Soccor	3		7	1
109	2022-06-28 11:09:07.547284-05	86	Pushup Jacks	3		7	1
110	2022-06-28 11:09:07.547956-05	85	Plank Jacks	3		7	1
111	2022-06-28 11:09:07.548627-05	84	Preditor Jacks	3		7	1
112	2022-06-28 11:09:07.549358-05	83	Cross-Body Jumping Jack	3		7	1
113	2022-06-28 11:09:07.550106-05	82	Jumping Jacks	3		7	1
114	2022-06-28 11:09:07.550963-05	81	Seal Jack	3		7	1
115	2022-06-28 11:09:07.55186-05	80	Blast-off Pushup	3		7	1
116	2022-06-28 11:09:07.552832-05	79	Low Jumping Mountain Climber	3		7	1
117	2022-06-28 11:09:07.553832-05	78	Jumping Mountain Climber	3		7	1
118	2022-06-28 11:09:07.554752-05	77	Semicircle Mountain Climber	3		7	1
119	2022-06-28 11:09:07.555522-05	76	Diagonal Mountain Climber	3		7	1
120	2022-06-28 11:09:07.556348-05	75	Spider Mountain Climber	3		7	1
121	2022-06-28 11:09:07.55722-05	74	Running Mountain Climber	3		7	1
122	2022-06-28 11:09:07.557928-05	73	Mountain Climber Switch	3		7	1
123	2022-06-28 11:09:07.558613-05	72	Low Rotational Chop	3		7	1
124	2022-06-28 11:09:07.559296-05	71	Single-leg Swing	3		7	1
125	2022-06-28 11:09:07.560723-05	70	In-and-Out Squat	3		7	1
126	2022-06-28 11:09:07.561582-05	69	Long Jump Backward Hop	3		7	1
127	2022-06-28 11:09:07.56237-05	68	Runner Lunge	3		7	1
128	2022-06-28 11:09:07.563156-05	67	Sprinter Skip	3		7	1
129	2022-06-28 11:09:07.563891-05	66	Super Skater Jump	3		7	1
130	2022-06-28 11:09:07.564603-05	65	Skater Jump	3		7	1
131	2022-06-28 11:09:07.565316-05	64	Butt Kicker	3		7	1
132	2022-06-28 11:09:07.566-05	63	High-Knee Run	3		7	1
133	2022-06-28 11:09:07.566678-05	62	Split Jump	3		7	1
134	2022-06-28 11:09:07.567433-05	61	Sit Squat Jump	3		7	1
135	2022-06-28 11:09:07.568159-05	60	Drop Squat	3		7	1
136	2022-06-28 11:09:07.568943-05	59	Incline chest Press	3		7	1
137	2022-06-28 11:09:07.56974-05	58	Elevated Plank Row Hold	3		7	1
138	2022-06-28 11:09:07.570488-05	57	Dumbell Pull Over	3		7	1
139	2022-06-28 11:09:07.571469-05	56	In-Out Hammer Curls	3		7	1
140	2022-06-28 11:09:07.572256-05	55	Strip-Set Curls	3		7	1
141	2022-06-28 11:09:07.573024-05	54	Superman	3		7	1
142	2022-06-28 11:09:07.573815-05	53	Curl-up/Hammer Downs	3		7	1
143	2022-06-28 11:09:07.575238-05	52	Hammer Curls	3		7	1
144	2022-06-28 11:09:07.576013-05	51	Chin-ups	3		7	1
145	2022-06-28 11:09:07.576764-05	50	Alternating Bent-over pull	3		7	1
146	2022-06-28 11:09:07.577434-05	49	Open Arm Curls	3		7	1
147	2022-06-28 11:09:07.578099-05	48	Reverse Grip Bent-over Rows	3		7	1
148	2022-06-28 11:09:07.578764-05	47	Concentration Curls	3		7	1
149	2022-06-28 11:09:07.579432-05	46	Elbows-Out Lawnmower pull	3		7	1
150	2022-06-28 11:09:07.580179-05	45	Twenty-Ones	3		7	1
151	2022-06-28 11:09:07.580858-05	44	Dumbbell Cross-Body Blows	3		7	1
152	2022-06-28 11:09:07.581529-05	43	Fly-Row Presses	3		7	1
153	2022-06-28 11:09:07.582194-05	42	One-Arm Balance Push-ups	3		7	1
154	2022-06-28 11:09:07.582858-05	41	Front-to-Back Tricep Extensions	3		7	1
155	2022-06-28 11:09:07.583745-05	40	Clap or Plyo Push-ups	3		7	1
156	2022-06-28 11:09:07.584556-05	39	Weighted Circles	3		7	1
157	2022-06-28 11:09:07.585287-05	38	One Arm Push-ups	3		7	1
158	2022-06-28 11:09:07.585962-05	37	Side-to-Side Push-ups	3		7	1
159	2022-06-28 11:09:07.586656-05	36	Y-Presses	3		7	1
160	2022-06-28 11:09:07.587442-05	35	Two Twitch Speed Push-ups	3		7	1
161	2022-06-28 11:09:07.588218-05	34	Overhead Tricep Extensions	3		7	1
162	2022-06-28 11:09:07.58891-05	33	Floor Flys	3		7	1
163	2022-06-28 11:09:07.58959-05	32	Pike Presses	3		7	1
164	2022-06-28 11:09:07.590366-05	31	Plange Push-ups	3		7	1
165	2022-06-28 11:09:07.591126-05	30	Slow-Motion 3-in-1 Push-ups	3		7	1
166	2022-06-28 11:09:07.591906-05	29	Switch Grip Pull Ups	3		7	1
167	2022-06-28 11:09:07.592632-05	28	Side Tri-Rises	3		7	1
168	2022-06-28 11:09:07.593335-05	27	In & Out Straight Arm Shoulder Flys	3		7	1
169	2022-06-28 11:09:07.594042-05	26	Lying-down Tricep Extensions	3		7	1
170	2022-06-28 11:09:07.594709-05	25	Tricep Extensions	3		7	1
171	2022-06-28 11:09:07.595404-05	24	Alternating Curls	3		7	1
172	2022-06-28 11:09:07.596075-05	23	Standing Curls	3		7	1
173	2022-06-28 11:09:07.596794-05	22	Flip-grip Twist Tricep Kickbacks	3		7	1
174	2022-06-28 11:09:07.597547-05	21	Static Arm Curls	3		7	1
175	2022-06-28 11:09:07.598326-05	20	Upright Rows	3		7	1
176	2022-06-28 11:09:07.59905-05	19	Chair Dips	3		7	1
177	2022-06-28 11:09:07.599795-05	18	Full Suspension Concentration Curls	3		7	1
178	2022-06-28 11:09:07.601074-05	17	Deep Swimmer's Press	3		7	1
179	2022-06-28 11:09:07.60184-05	16	Two-Arm Tricep Kickbacks	3		7	1
180	2022-06-28 11:09:07.602746-05	15	In & Out Bicep Curls	3		7	1
181	2022-06-28 11:09:07.603708-05	14	Alternating Shoulder Press	3		7	1
182	2022-06-28 11:09:07.604639-05	13	Shoulder Press	3		7	1
183	2022-06-28 11:09:07.605418-05	12	Back flys	3		7	1
184	2022-06-28 11:09:07.606209-05	11	Dive-bomber Push-ups	3		7	1
185	2022-06-28 11:09:07.606988-05	10	Lawnmower pull	3		7	1
186	2022-06-28 11:09:07.607692-05	9	Diamond Push-ups	3		7	1
187	2022-06-28 11:09:07.608415-05	8	Heavy Pants	3		7	1
188	2022-06-28 11:09:07.609193-05	7	Decline Push-ups	3		7	1
189	2022-06-28 11:09:07.609958-05	6	Close Grip Overhand Pull-ups	3		7	1
190	2022-06-28 11:09:07.610735-05	5	Wide Fly Push-ups	3		7	1
191	2022-06-28 11:09:07.611486-05	4	Reverse Grip Chin-ups	3		7	1
192	2022-06-28 11:09:07.612253-05	3	Military Push-ups	3		7	1
193	2022-06-28 11:09:07.612966-05	2	Wide Front Pull-ups	3		7	1
194	2022-06-28 11:09:07.613677-05	1	Standard Push-ups	3		7	1
195	2022-06-28 11:10:40.068339-05	74	2022-06-28: cardio-core	3		8	1
196	2022-06-28 11:10:40.071518-05	73	2022-06-29: chest-back	3		8	1
197	2022-06-28 11:10:40.072732-05	72	2022-06-28: cardio-core	3		8	1
198	2022-06-28 11:11:59.571789-05	71	2022-06-27: shoulders-biceps-triceps	3		8	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	exercises	exercise
8	exercises	workout
9	exercises	workoutexercise
10	exercises	dailyworkouts
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	exercises	0001_initial	2022-06-01 20:16:30.876867-05
2	exercises	0002_exercise_diffulty_level_workout_workout_target	2022-06-01 20:16:30.88558-05
3	exercises	0003_alter_exercise_diffulty_level	2022-06-01 20:16:30.891671-05
4	exercises	0004_exercise_equipment_exercise_resistance_type	2022-06-01 20:16:30.897302-05
5	exercises	0005_workout_exercises	2022-06-01 20:16:30.902325-05
6	contenttypes	0001_initial	2022-06-22 19:15:08.619395-05
7	auth	0001_initial	2022-06-22 19:15:08.708119-05
8	admin	0001_initial	2022-06-22 19:15:08.758693-05
9	admin	0002_logentry_remove_auto_add	2022-06-22 19:15:08.767211-05
10	admin	0003_logentry_add_action_flag_choices	2022-06-22 19:15:08.775268-05
11	contenttypes	0002_remove_content_type_name	2022-06-22 19:15:08.794497-05
12	auth	0002_alter_permission_name_max_length	2022-06-22 19:15:08.802975-05
13	auth	0003_alter_user_email_max_length	2022-06-22 19:15:08.810692-05
14	auth	0004_alter_user_username_opts	2022-06-22 19:15:08.8178-05
15	auth	0005_alter_user_last_login_null	2022-06-22 19:15:08.825985-05
16	auth	0006_require_contenttypes_0002	2022-06-22 19:15:08.827996-05
17	auth	0007_alter_validators_add_error_messages	2022-06-22 19:15:08.835427-05
18	auth	0008_alter_user_username_max_length	2022-06-22 19:15:08.848436-05
19	auth	0009_alter_user_last_name_max_length	2022-06-22 19:15:08.856666-05
20	auth	0010_alter_group_name_max_length	2022-06-22 19:15:08.86668-05
21	auth	0011_update_proxy_permissions	2022-06-22 19:15:08.875096-05
22	auth	0012_alter_user_first_name_max_length	2022-06-22 19:15:08.882598-05
23	exercises	0006_alter_workout_workout_date	2022-06-22 19:15:08.886651-05
24	sessions	0001_initial	2022-06-22 19:15:08.896799-05
25	exercises	0007_dailyworkouts	2022-06-23 20:43:01.992951-05
26	exercises	0008_alter_dailyworkouts_workout_date	2022-06-23 20:49:50.736543-05
27	exercises	0009_rename_count_dailyworkouts_total_workouts	2022-06-23 20:55:24.587656-05
28	exercises	0010_dailyworkouts_status	2022-06-24 13:33:57.049582-05
29	exercises	0011_workout_total_rounds	2022-06-27 14:39:56.908622-05
30	exercises	0012_alter_workout_total_rounds	2022-06-27 14:40:09.224185-05
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
68plw0mbp6k0lf9zzobk5kulfh3ci7qu	.eJxVjMsOwiAUBf-FtSFAuYW6dO83kPtAqRqalHZl_HdD0oVuz8yct0q4byXtLa9pFnVWVp1-N0J-5tqBPLDeF81L3daZdFf0QZu-LpJfl8P9OyjYSq8NDSEMntFFH4UdWA4eQDIgmeydm4B4NN4FtATGxugwkviRJ7hJUJ8vz6A3Zw:1o6D9t:B7lYF1ae7YwznJEy1QZHj0CMfQtWAdgsnQRM9Omy5xQ	2022-07-12 10:29:45.252436-05
\.


--
-- Data for Name: exercises_dailyworkouts; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.exercises_dailyworkouts (id, workout_date, total_workouts, status) FROM stdin;
15	2022-06-23	43	started
17	2022-06-24	10	started
18	2022-06-24	9	finished
19	2022-06-27	1	finished
\.


--
-- Data for Name: exercises_exercise; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.exercises_exercise (id, name, muscle_target, secondary_target, push_pull, muscle_group, diffulty_level, equipment, resistance_type) FROM stdin;
195	Standard Push-Ups	chest	triceps	push	upper	0	\N	\N
196	Wide Front Pull-Ups	back	biceps	pull	upper	0	\N	\N
197	Military Push-Ups	chest	triceps	push	upper	0	\N	\N
198	Reverse Grip Chin-ups	back	biceps	pull	upper	0	\N	\N
199	Wide Fly Push-Ups	chest	triceps	push	upper	0	\N	\N
200	Close Grip Overhand Pull-Ups	back	biceps	pull	upper	0	\N	\N
201	Decline Push-Ups	chest	triceps	push	upper	0	\N	\N
202	Heavy Pants	back		pull	upper	0	\N	\N
203	Diamond Push-Ups	chest	triceps	push	upper	0	\N	\N
204	Lawnmower Pull	back		pull	upper	0	\N	\N
205	Dive-bomber Push-Ups	chest		push	upper	0	\N	\N
206	Back Flys	back		pull	upper	0	\N	\N
207	Shoulder Press	shoulders		push	upper	0	\N	\N
208	Alternating Shoulder Press	shoulders		push	upper	0	\N	\N
209	In & Out Bicep Curls	biceps		pull	upper	0	\N	\N
210	Two-Arm Tricep Kickbacks	triceps		push	upper	0	\N	\N
211	Deep Swimmer's Press	shoulders		push	upper	0	\N	\N
212	Full Suspension Concentration Curls	biceps		pull	upper	0	\N	\N
213	Chair Dips	triceps	shoulders	push	upper	0	\N	\N
214	Upright Rows	shoulders		pull	upper	0	\N	\N
215	Static Arm Curls	biceps		pull	upper	0	\N	\N
216	Flip-grip Twist Tricep Kickbacks	triceps		push	upper	0	\N	\N
217	Standing Curls	biceps		pull	upper	0	\N	\N
218	Alternating Curls	biceps		pull	upper	0	\N	\N
219	Tricep Extensions	triceps		push	upper	0	\N	\N
220	Lying-down Tricep Extensions	triceps		push	upper	0	\N	\N
221	In & Out Straight Arm Shoulder Flys	shoulders		push	upper	0	\N	\N
222	Side Tri-Rises	triceps		push	upper	0	\N	\N
223	Switch Grip pull Ups	back	biceps	pull	upper	0	\N	\N
224	Slow-Motion 3-in-1 Push-Ups	chest	triceps	push	upper	0	\N	\N
225	Plange Push-Ups	chest	triceps	push	upper	0	\N	\N
226	Pike Presses	shoulders	triceps	push	upper	0	\N	\N
227	Floor Flys	chest	triceps	push	upper	0	\N	\N
228	Overhead Tricep Extensions	triceps		push	upper	0	\N	\N
229	Two Twitch Speed Push-Ups	chest	triceps	push	upper	0	\N	\N
230	Y-Presses	shoulders		push	upper	0	\N	\N
231	Side-to-Side Push-Ups	chest	triceps	push	upper	0	\N	\N
232	One Arm Push-Ups	chest	triceps	push	upper	0	\N	\N
233	Weighted Circles	shoulders		N/A	upper	0	\N	\N
234	Clap or Plyo Push-Ups	chest	triceps	push	upper	0	\N	\N
235	Front-to-Back Tricep Extensions	triceps		push	upper	0	\N	\N
236	One-Arm Balance Push-Ups	chest	triceps	push	upper	0	\N	\N
237	Fly-Row Presses	shoulders		Both	upper	0	\N	\N
238	Dumbbell Cross-Body Blows	triceps	biceps	push	upper	0	\N	\N
239	Twenty-Ones	biceps		pull	upper	0	\N	\N
240	Elbows-Out Lawnmower pull	back		pull	upper	0	\N	\N
241	Concentration Curls	biceps		pull	upper	0	\N	\N
242	Reverse Grip Bent-over Rows	back	biceps	pull	upper	0	\N	\N
243	Open Arm Curls	biceps		pull	upper	0	\N	\N
244	Alternating Bent-over pull	back	biceps	pull	upper	0	\N	\N
245	Chin-Ups	back	biceps	pull	upper	0	\N	\N
246	Hammer Curls	biceps		pull	upper	0	\N	\N
247	Curl-Up/Hammer Downs	biceps		pull	upper	0	\N	\N
248	Superman	back		N/A	upper	0	\N	\N
249	Strip-Set Curls	biceps		pull	upper	0	\N	\N
250	In-Out Hammer Curls	biceps		pull	upper	0	\N	\N
251	Dumbell Pull Over	back		pull	upper	0	\N	\N
252	Elevated Plank Row Hold	back	core	N/A	upper	0	\N	\N
253	Incline chest Press	chest		push	upper	0	\N	\N
254	Drop Squat	legs	cardio	N/A	lower	0	\N	\N
255	Sit Squat Jump	legs	cardio	N/A	lower	0	\N	\N
256	Split Jump	legs	cardio	N/A	lower	0	\N	\N
257	High-Knee Run	cardio	legs	N/A	lower	0	\N	\N
258	Butt Kicker	cardio	legs	N/A	lower	0	\N	\N
259	Skater Jump	cardio	legs	N/A	lower	0	\N	\N
260	Super Skater Jump	cardio	legs	N/A	lower	0	\N	\N
261	Sprinter Skip	cardio	legs		lower	0	\N	\N
262	Runner Lunge	legs	cardio		lower	0	\N	\N
263	Long Jump Backward Hop	cardio	legs		lower	0	\N	\N
264	In-and-Out Squat	legs	cardio		lower	0	\N	\N
265	Single-leg Swing	legs	cardio		lower	0	\N	\N
266	Low Rotational Chop	legs	cardio		lower	0	\N	\N
267	Mountain Climber Switch	cardio	legs		lower	0	\N	\N
268	Running Mountain Climber	cardio	legs		lower	0	\N	\N
269	Spider Mountain Climber	cardio	legs		lower	0	\N	\N
270	Diagonal Mountain Climber	cardio	legs		lower	0	\N	\N
271	Semicircle Mountain Climber	cardio	legs		lower	0	\N	\N
272	Jumping Mountain Climber	cardio	legs		lower	0	\N	\N
273	Low Jumping Mountain Climber	cardio	legs		lower	0	\N	\N
274	Blast-off Push-Ups	chest	legs		lower	0	\N	\N
275	Seal Jack	cardio			lower	0	\N	\N
276	Jumping Jacks	cardio			lower	0	\N	\N
277	Cross-Body Jumping Jack	cardio			lower	0	\N	\N
278	Preditor Jacks	cardio	legs		lower	0	\N	\N
279	Plank Jacks	cardio	core		lower	0	\N	\N
280	Push-Up Jacks	chest	triceps		lower	0	\N	\N
281	Low Box Runner / Soccor	cardio			lower	0	\N	\N
282	360 Ball Runner / Soccor	cardio			lower	0	\N	\N
283	Low Box Lateral Runner	cardio			lower	0	\N	\N
284	Burpee	cardio			lower	0	\N	\N
285	Lateral 3-Step	cardio			lower	0	\N	\N
286	Alternating Fast Feed	cardio			lower	0	\N	\N
287	Single Leg Pogo Jump	cardio			lower	0	\N	\N
288	Pogo Jump	cardio			lower	0	\N	\N
289	Side to Side Hops	cardio			lower	0	\N	\N
290	Plank Hand Tap	core	chest		core	0	\N	\N
291	Plank Elbow Tap	core	chest		core	0	\N	\N
292	Plank Shoulder Tap	core	chest		core	0	\N	\N
293	Plank Hip Tap	core	chest		core	0	\N	\N
294	Plank Knee Tap	core	chest		core	0	\N	\N
295	Plank Toe Tap	core	chest		core	0	\N	\N
296	Lunge Runner	legs	cardio		lower	0	\N	\N
297	T-Rotation	core	chest		core	0	\N	\N
298	Tuck Jump	legs	cardio		lower	0	\N	\N
299	Knee Tuck Jump	legs	cardio		lower	0	\N	\N
300	Foot Tuck Jump	legs	cardio		lower	0	\N	\N
301	Speed Walkout	core	cardio		lower	0	\N	\N
302	Wide Leg Tiptoe Squat	legs			lower	0	\N	\N
303	Fast Feet Chair Jump	legs	cardio		lower	0	\N	\N
304	Slalom Line Jump	legs	cardio		lower	0	\N	\N
305	Burpee Knee Tuck	legs	cardio		lower	0	\N	\N
306	1-Leg Slalom	legs			lower	0	\N	\N
307	1-Leg Squat	legs			lower	0	\N	\N
308	Toe Tap 360	cardio			lower	0	\N	\N
309	Wall Squat	legs	cardio		lower	0	\N	\N
310	Step-Back Lunges	legs			lower	0	\N	\N
311	Alternating Side Lunges	legs			lower	0	\N	\N
312	Single Leg Wall Squat	legs			lower	0	\N	\N
313	Albanian Squat	legs			lower	0	\N	\N
314	Adductor Lunge	legs			lower	0	\N	\N
315	Calf Raises	legs			lower	0	\N	\N
316	Banana Two Crunch	abs			core	0	\N	\N
317	Bicycles	abs			core	0	\N	\N
318	Scissor Twist	abs			core	0	\N	\N
319	Cross Leg / Wide Leg Sit-ups	abs			core	0	\N	\N
320	Side Arm Balance Crunch	abs			core	0	\N	\N
321	Pulse Ups	abs			core	0	\N	\N
322	V-Up/Roll Up	abs			core	0	\N	\N
323	Oblique Roll Crunch	abs			core	0	\N	\N
324	Row the Boat	abs			core	0	\N	\N
325	Banana Knee Straight Leg Crunch	abs			core	0	\N	\N
326	Hip Rock & Raise	abs			core	0	\N	\N
327	Roll V Hold	abs			core	0	\N	\N
328	Gate Bridge Lift	abs			core	0	\N	\N
329	Scissors Clapper	abs			core	0	\N	\N
330	Abergnome	abs			core	0	\N	\N
331	Crunchy Frog	abs			core	0	\N	\N
332	Bug Bicycle Crunch	abs			core	0	\N	\N
333	Tornado	abs			core	0	\N	\N
334	Twist & Hold	abs			core	0	\N	\N
335	Spiderman Plank	abs			core	0	\N	\N
336	Crunch	abs			core	0	\N	\N
337	Side Plank	abs			core	0	\N	\N
338	Side V-Up	abs			core	0	\N	\N
\.


--
-- Data for Name: exercises_workout; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.exercises_workout (id, workout_date, workout_target, total_rounds) FROM stdin;
54	2022-06-21	legs-cardio	1
55	2022-06-23	back-biceps	1
56	2022-06-22	shoulders-biceps-triceps	1
57	2022-06-22	shoulders-biceps-triceps	1
58	2022-06-24	cardio-core	1
59	2022-06-25	cardio	1
60	2022-06-26	cardio-core	1
52	2022-06-20	chest-back	1
75	2022-06-27	shoulders-chest-triceps	1
76	2022-06-28	cardio-core	3
77	2022-06-29	back-biceps	2
\.


--
-- Data for Name: exercises_workoutexercise; Type: TABLE DATA; Schema: public; Owner: taprete
--

COPY public.exercises_workoutexercise (id, "order", exercise_id, workout_id) FROM stdin;
1127	1	226	75
1128	2	201	75
1129	3	222	75
1130	4	237	75
1131	5	195	75
1132	6	210	75
1133	7	221	75
1134	8	225	75
1135	9	235	75
1136	10	207	75
1137	11	205	75
1138	12	228	75
1139	13	214	75
1140	14	236	75
1141	15	220	75
1142	16	230	75
1143	17	227	75
1144	18	219	75
1145	19	208	75
1146	20	274	75
1147	21	216	75
1148	1	268	76
1149	2	297	76
1150	3	263	76
1151	4	290	76
1152	5	275	76
1153	6	301	76
1154	7	276	76
1155	8	295	76
1156	9	268	76
1157	10	297	76
1158	11	263	76
1159	12	290	76
1160	13	275	76
1161	14	301	76
1162	15	276	76
1163	16	295	76
1164	17	268	76
1165	18	297	76
1166	19	263	76
1167	20	290	76
1168	21	275	76
1169	22	301	76
1170	23	276	76
1171	24	295	76
1172	1	245	77
1173	2	241	77
1174	3	240	77
1175	4	212	77
1176	5	223	77
1177	6	246	77
1178	7	252	77
1179	8	249	77
1180	9	248	77
1181	10	243	77
1182	11	245	77
1183	12	241	77
1184	13	240	77
1185	14	212	77
1186	15	223	77
1187	16	246	77
1188	17	252	77
1189	18	249	77
1190	19	248	77
1191	20	243	77
\.


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 198, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 30, true);


--
-- Name: exercises_dailyworkouts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.exercises_dailyworkouts_id_seq', 19, true);


--
-- Name: exercises_exercise_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.exercises_exercise_id_seq', 338, true);


--
-- Name: exercises_workout_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.exercises_workout_id_seq', 77, true);


--
-- Name: exercises_workoutexercise_id_seq; Type: SEQUENCE SET; Schema: public; Owner: taprete
--

SELECT pg_catalog.setval('public.exercises_workoutexercise_id_seq', 1191, true);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: exercises_dailyworkouts exercises_dailyworkouts_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_dailyworkouts
    ADD CONSTRAINT exercises_dailyworkouts_pkey PRIMARY KEY (id);


--
-- Name: exercises_exercise exercises_exercise_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_exercise
    ADD CONSTRAINT exercises_exercise_pkey PRIMARY KEY (id);


--
-- Name: exercises_workout exercises_workout_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_workout
    ADD CONSTRAINT exercises_workout_pkey PRIMARY KEY (id);


--
-- Name: exercises_workoutexercise exercises_workoutexercise_pkey; Type: CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_workoutexercise
    ADD CONSTRAINT exercises_workoutexercise_pkey PRIMARY KEY (id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: exercises_workoutexercise_exercise_id_ee96df00; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX exercises_workoutexercise_exercise_id_ee96df00 ON public.exercises_workoutexercise USING btree (exercise_id);


--
-- Name: exercises_workoutexercise_workout_id_017f1179; Type: INDEX; Schema: public; Owner: taprete
--

CREATE INDEX exercises_workoutexercise_workout_id_017f1179 ON public.exercises_workoutexercise USING btree (workout_id);


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: exercises_workoutexercise exercises_workoutexe_exercise_id_ee96df00_fk_exercises; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_workoutexercise
    ADD CONSTRAINT exercises_workoutexe_exercise_id_ee96df00_fk_exercises FOREIGN KEY (exercise_id) REFERENCES public.exercises_exercise(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: exercises_workoutexercise exercises_workoutexe_workout_id_017f1179_fk_exercises; Type: FK CONSTRAINT; Schema: public; Owner: taprete
--

ALTER TABLE ONLY public.exercises_workoutexercise
    ADD CONSTRAINT exercises_workoutexe_workout_id_017f1179_fk_exercises FOREIGN KEY (workout_id) REFERENCES public.exercises_workout(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--

