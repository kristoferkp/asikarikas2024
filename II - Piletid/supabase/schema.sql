
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

CREATE SCHEMA IF NOT EXISTS "public";

ALTER SCHEMA "public" OWNER TO "pg_database_owner";

SET default_tablespace = '';

SET default_table_access_method = "heap";

CREATE TABLE IF NOT EXISTS "public"."tickets" (
    "from" "text" DEFAULT ''::"text",
    "to" "text" DEFAULT ''::"text",
    "stops" "jsonb",
    "price" double precision,
    "ticket_type" "text",
    "vehicle_type" "text",
    "start_time" time without time zone,
    "end_time" time without time zone,
    "ticket_id" "uuid" DEFAULT "gen_random_uuid"() NOT NULL,
    "date" "date"
);

ALTER TABLE "public"."tickets" OWNER TO "postgres";

CREATE OR REPLACE FUNCTION "public"."get_tickets"("to_city" "text", "from_city" "text") RETURNS SETOF "public"."tickets"
    LANGUAGE "plpgsql"
    AS $$BEGIN
  RETURN QUERY
  select
  *
from
  tickets
where
  (
    "to" = to_city
    and (
      "from" = from_city
      or from_city = any (
        array (
          select
            jsonb_array_elements_text(stops)
        )
      )
    )
  )
  or (
    "from" = from_city
    and (
      "to" = to_city
      or to_city = any (
        array (
          select
            jsonb_array_elements_text(stops)
        )
      )
    )
  );
END;$$;

ALTER FUNCTION "public"."get_tickets"("to_city" "text", "from_city" "text") OWNER TO "postgres";

CREATE OR REPLACE FUNCTION "public"."handle_new_user"() RETURNS "trigger"
    LANGUAGE "plpgsql" SECURITY DEFINER
    AS $$
begin
  insert into public.profiles (id, full_name, avatar_url)
  values (new.id, new.raw_user_meta_data->>'full_name', new.raw_user_meta_data->>'avatar_url');
  return new;
end;
$$;

ALTER FUNCTION "public"."handle_new_user"() OWNER TO "postgres";

CREATE TABLE IF NOT EXISTS "public"."profiles" (
    "id" "uuid" NOT NULL,
    "updated_at" timestamp with time zone,
    "username" "text",
    "full_name" "text",
    "avatar_url" "text",
    CONSTRAINT "username_length" CHECK (("char_length"("username") >= 3))
);

ALTER TABLE "public"."profiles" OWNER TO "postgres";

CREATE TABLE IF NOT EXISTS "public"."purchases" (
    "purchase_id" "uuid" DEFAULT "gen_random_uuid"() NOT NULL,
    "created_at" timestamp with time zone DEFAULT "now"() NOT NULL,
    "user_id" "uuid" DEFAULT "auth"."uid"(),
    "ticket_id" "uuid",
    "validated" boolean DEFAULT false NOT NULL,
    "email" "text"
);

ALTER TABLE "public"."purchases" OWNER TO "postgres";

ALTER TABLE ONLY "public"."profiles"
    ADD CONSTRAINT "profiles_pkey" PRIMARY KEY ("id");

ALTER TABLE ONLY "public"."profiles"
    ADD CONSTRAINT "profiles_username_key" UNIQUE ("username");

ALTER TABLE ONLY "public"."purchases"
    ADD CONSTRAINT "purchases_pkey" PRIMARY KEY ("purchase_id");

ALTER TABLE ONLY "public"."purchases"
    ADD CONSTRAINT "purchases_purchase_id_key" UNIQUE ("purchase_id");

ALTER TABLE ONLY "public"."tickets"
    ADD CONSTRAINT "ticket_pkey" PRIMARY KEY ("ticket_id");

ALTER TABLE ONLY "public"."tickets"
    ADD CONSTRAINT "ticket_ticket_id_key" UNIQUE ("ticket_id");

ALTER TABLE ONLY "public"."profiles"
    ADD CONSTRAINT "profiles_id_fkey" FOREIGN KEY ("id") REFERENCES "auth"."users"("id") ON DELETE CASCADE;

ALTER TABLE ONLY "public"."purchases"
    ADD CONSTRAINT "public_purchases_ticket_id_fkey" FOREIGN KEY ("ticket_id") REFERENCES "public"."tickets"("ticket_id");

ALTER TABLE ONLY "public"."purchases"
    ADD CONSTRAINT "public_purchases_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "public"."profiles"("id") ON DELETE SET NULL;

CREATE POLICY "Allow users to see their own purchases" ON "public"."purchases" FOR SELECT USING (("user_id" = "auth"."uid"()));

CREATE POLICY "Enable insert for authenticated users only" ON "public"."purchases" FOR INSERT TO "authenticated" WITH CHECK (true);

CREATE POLICY "Public profiles are viewable by everyone." ON "public"."profiles" FOR SELECT USING (true);

CREATE POLICY "Ticket tables are readable to everyone" ON "public"."tickets" FOR SELECT USING (true);

CREATE POLICY "Users can insert their own profile." ON "public"."profiles" FOR INSERT WITH CHECK (("auth"."uid"() = "id"));

CREATE POLICY "Users can update own profile." ON "public"."profiles" FOR UPDATE USING (("auth"."uid"() = "id"));

ALTER TABLE "public"."profiles" ENABLE ROW LEVEL SECURITY;

ALTER TABLE "public"."purchases" ENABLE ROW LEVEL SECURITY;

ALTER TABLE "public"."tickets" ENABLE ROW LEVEL SECURITY;

GRANT USAGE ON SCHEMA "public" TO "postgres";
GRANT USAGE ON SCHEMA "public" TO "anon";
GRANT USAGE ON SCHEMA "public" TO "authenticated";
GRANT USAGE ON SCHEMA "public" TO "service_role";

GRANT ALL ON TABLE "public"."tickets" TO "anon";
GRANT ALL ON TABLE "public"."tickets" TO "authenticated";
GRANT ALL ON TABLE "public"."tickets" TO "service_role";

GRANT ALL ON FUNCTION "public"."get_tickets"("to_city" "text", "from_city" "text") TO "anon";
GRANT ALL ON FUNCTION "public"."get_tickets"("to_city" "text", "from_city" "text") TO "authenticated";
GRANT ALL ON FUNCTION "public"."get_tickets"("to_city" "text", "from_city" "text") TO "service_role";

GRANT ALL ON FUNCTION "public"."handle_new_user"() TO "anon";
GRANT ALL ON FUNCTION "public"."handle_new_user"() TO "authenticated";
GRANT ALL ON FUNCTION "public"."handle_new_user"() TO "service_role";

GRANT ALL ON TABLE "public"."profiles" TO "anon";
GRANT ALL ON TABLE "public"."profiles" TO "authenticated";
GRANT ALL ON TABLE "public"."profiles" TO "service_role";

GRANT ALL ON TABLE "public"."purchases" TO "anon";
GRANT ALL ON TABLE "public"."purchases" TO "authenticated";
GRANT ALL ON TABLE "public"."purchases" TO "service_role";

ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "postgres";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "anon";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "authenticated";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON SEQUENCES  TO "service_role";

ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "postgres";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "anon";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "authenticated";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON FUNCTIONS  TO "service_role";

ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "postgres";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "anon";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "authenticated";
ALTER DEFAULT PRIVILEGES FOR ROLE "postgres" IN SCHEMA "public" GRANT ALL ON TABLES  TO "service_role";

RESET ALL;
