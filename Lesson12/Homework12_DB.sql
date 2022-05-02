CREATE TABLE public."user" (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"name" varchar(54) NOT NULL,
	age int4 NOT NULL,
	gender varchar(30) NOT NULL,
	nationality varchar(60) NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (id)
);

insert into public."user" ("name","age",gender,nationality) values ('Andrei',14,'m','R');
insert into public."user" ("name","age",gender,nationality) values ('Grigorii',20,'m','R');
insert into public."user" ("name","age",gender,nationality) values ('Kirill',19,'m','S');
insert into public."user" ("name","age",gender,nationality) values ('Fedor',40,'m','S');
insert into public."user" ("name","age",gender,nationality) values ('Vikor',90,'m','U');

CREATE TABLE public.posts (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	title varchar NOT NULL,
	description varchar NOT NULL,
	user_id int4 NOT NULL,
	CONSTRAINT posts_pk PRIMARY KEY (id),
	CONSTRAINT posts_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE ON UPDATE CASCADE
);


insert into public.posts  ("title","description",user_id) values ('Hi','sql',1);
insert into public.posts  ("title","description",user_id) values ('Hi1','sql1',3);
insert into public.posts  ("title","description",user_id) values ('Hi2','sql2 ',2);
insert into public.posts  ("title","description",user_id) values ('Hi3','sql3',4);
insert into public.posts  ("title","description",user_id) values ('Hi4','sql4',5);
insert into public.posts  ("title","description",user_id) values ('Hi5','sql5',1);
insert into public.posts  ("title","description",user_id) values ('Hi6','sql6',4);


CREATE TABLE public.likes (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	user_id int4 NOT NULL,
	post_id int4 NOT NULL,
	CONSTRAINT likes_pk PRIMARY KEY (id),
	CONSTRAINT likes_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT likes_fk_1 FOREIGN KEY (post_id) REFERENCES public.posts(id) ON DELETE CASCADE ON UPDATE CASCADE
);

insert into public.likes (user_id, post_id) values (4,1);
insert into public.likes (user_id, post_id) values (2,3);
insert into public.likes (user_id, post_id) values (4,2);
insert into public.likes (user_id, post_id) values (4,5);

CREATE TABLE public."comments" (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"text" varchar NOT NULL,
	user_id int4 NOT NULL,
	post_id int4 NOT NULL,
	CONSTRAINT comments_pk PRIMARY KEY (id),
	CONSTRAINT comments_fk FOREIGN KEY (user_id) REFERENCES public."user"(id) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT comments_fk_1 FOREIGN KEY (post_id) REFERENCES public.posts(id) ON DELETE CASCADE ON UPDATE CASCADE
);

insert into public."comments" ("text",user_id, post_id) values ('lalala',1,5);
insert into public."comments" ("text",user_id, post_id) values ('blabla',2,1);
insert into public."comments" ("text",user_id, post_id) values ('lilili',3,5);
insert into public."comments" ("text",user_id, post_id) values ('kurlak',1,2);
insert into public."comments" ("text",user_id, post_id) values ('gnomiki',4,5);