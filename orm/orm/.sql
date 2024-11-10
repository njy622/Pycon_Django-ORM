CREATE TABLE "myapp_customuser"
    (
        "id"         integer      NOT NULL PRIMARY KEY comment "PK",
        "username"   varchar(50)  NOT NULL UNIQUE comment "사용자 이름",
        "password"   varchar(255) NOT NULL  comment "비밀번호",
        "email"      varchar(100) NOT NULL UNIQUE comment "이메일",
        "created_at" datetime     NOT NULL comment "생성일",
        "updated_at" datetime     NOT NULL comment "수정일"
    ) comment "유저목록"


    --
-- Change Meta options on customuser
--
-- (no-op)
--
-- Alter field email on customuser
--
-- (no-op)
--
-- Alter field is_activate on customuser
--
-- (no-op)
--
-- Alter field password on customuser
--
-- (no-op)
--
-- Alter field username on customuser
--
-- (no-op)



CREATE TABLE "new__myapp_customuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "is_activate" bool DEFAULT 1 NOT NULL, "username" varchar(50) NOT NULL UNIQUE, "password" varINSERT INTO "new__myapp_customuser" ("id", "username", "password", "email", "created_at", "updated_at") SELECT "id", "username", "password", "email", "created_at", "updated_at" FROM "myapp_customuser"; (params ())
DROP TABLE "myapp_customuser"; (params ())
ALTER TABLE "new__myapp_customuser" RENAME TO "myapp_customuser"; (params ())
(0.000) PRAGMA foreign_key_check; args=None; alias=default
(0.000) COMMIT; args=None; alias=default
(0.000) PRAGMA foreign_keys = ON; args=None; alias=default
BEGIN;
--
-- Add field is_activate to customuser
--
CREATE TABLE "new__myapp_customuser" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "is_activate" bool DEFAULT 1 NOT NULL, "username" varchar(50) NOT NULL UNIQUE, "password" varchar(255) NOT NULL, "email" varchar(100) NOT NULL UNIQUE, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL);
INSERT INTO "new__myapp_customuser" ("id", "username", "password", "email", "created_at", "updated_at") SELECT "id", "username", "password", "email", "created_at", "updated_at" FROM "myapp_customuser";
DROP TABLE "myapp_customuser";
ALTER TABLE "new__myapp_customuser" RENAME TO "myapp_customuser";
COMMIT;
