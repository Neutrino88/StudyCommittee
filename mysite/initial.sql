BEGIN;
--
-- Create model Discipline
--
CREATE TABLE "app_discipline" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "control_form" varchar(2) NOT NULL, "lecture_hours" integer unsigned NOT NULL CHECK ("lecture_hours" >= 0), "practice_hours" integer unsigned NOT NULL CHECK ("practice_hours" >= 0));
--
-- Create model Faculty
--
CREATE TABLE "app_faculty" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "short_name" varchar(100) NOT NULL, "name" varchar(200) NOT NULL);
--
-- Create model PersonalInfo
--
CREATE TABLE "app_personal_info" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "patronymic_name" varchar(30) NOT NULL, "birthday" date NOT NULL);
--
-- Create model Speciality
--
CREATE TABLE "app_speciality" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "study_format" varchar(2) NOT NULL, "faculty_id" bigint NOT NULL REFERENCES "app_faculty" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model University
--
CREATE TABLE "app_university" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "short_name" varchar(100) NOT NULL, "name" varchar(200) NOT NULL UNIQUE, "creation_year" smallint unsigned NOT NULL CHECK ("creation_year" >= 0));
--
-- Create model StudyGroup
--
CREATE TABLE "app_study_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "course_number" smallint unsigned NOT NULL CHECK ("course_number" >= 0), "number" varchar(10) NOT NULL UNIQUE, "speciality_id" bigint NOT NULL REFERENCES "app_speciality" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Student
--
CREATE TABLE "app_student" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" bigint NOT NULL REFERENCES "app_study_group" ("id") DEFERRABLE INITIALLY DEFERRED, "info_id" bigint NOT NULL UNIQUE REFERENCES "app_personal_info" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model Lecturer
--
CREATE TABLE "app_lecturer" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "degree" varchar(30) NOT NULL, "faculty_id" bigint NOT NULL REFERENCES "app_faculty" ("id") DEFERRABLE INITIALLY DEFERRED, "info_id" bigint NOT NULL UNIQUE REFERENCES "app_personal_info" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Add field university to faculty
--
CREATE TABLE "new__app_faculty" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "short_name" varchar(100) NOT NULL, "name" varchar(200) NOT NULL, "university_id" bigint NOT NULL REFERENCES "app_university" ("id") DEFERRABLE INITIALLY DEFERRED);
INSERT INTO "new__app_faculty" ("id", "short_name", "name", "university_id") SELECT "id", "short_name", "name", NULL FROM "app_faculty";
DROP TABLE "app_faculty";
ALTER TABLE "new__app_faculty" RENAME TO "app_faculty";
CREATE UNIQUE INDEX "app_speciality_name_faculty_id_88c55e89_uniq" ON "app_speciality" ("name", "faculty_id");
CREATE INDEX "app_speciality_faculty_id_2d7e4e04" ON "app_speciality" ("faculty_id");
CREATE INDEX "app_study_group_speciality_id_6dd10d94" ON "app_study_group" ("speciality_id");
CREATE INDEX "app_student_group_id_c92fca5d" ON "app_student" ("group_id");
CREATE INDEX "app_lecturer_faculty_id_382fa491" ON "app_lecturer" ("faculty_id");
CREATE INDEX "app_faculty_university_id_a7eee60b" ON "app_faculty" ("university_id");
--
-- Create model SpecialityDiscipline
--
CREATE TABLE "app_speciality_discipline" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "discipline_id" bigint NOT NULL REFERENCES "app_discipline" ("id") DEFERRABLE INITIALLY DEFERRED, "speciality_id" bigint NOT NULL REFERENCES "app_speciality" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Create model LecturerGroupDiscipline
--
CREATE TABLE "app_lecturer_group_discipline" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "discipline_id" bigint NOT NULL REFERENCES "app_discipline" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" bigint NOT NULL REFERENCES "app_study_group" ("id") DEFERRABLE INITIALLY DEFERRED, "lecturer_id" bigint NOT NULL REFERENCES "app_lecturer" ("id") DEFERRABLE INITIALLY DEFERRED);
--
-- Alter unique_together for faculty (1 constraint(s))
--
CREATE UNIQUE INDEX "app_faculty_name_university_id_e9ed2341_uniq" ON "app_faculty" ("name", "university_id");
CREATE UNIQUE INDEX "app_speciality_discipline_speciality_id_discipline_id_e9be6d80_uniq" ON "app_speciality_discipline" ("speciality_id", "discipline_id");
CREATE INDEX "app_speciality_discipline_discipline_id_6ee7e1b0" ON "app_speciality_discipline" ("discipline_id");
CREATE INDEX "app_speciality_discipline_speciality_id_f7b9177b" ON "app_speciality_discipline" ("speciality_id");
CREATE UNIQUE INDEX "app_lecturer_group_discipline_lecturer_id_group_id_discipline_id_c5388f5a_uniq" ON "app_lecturer_group_discipline" ("lecturer_id", "group_id", "discipline_id");
CREATE INDEX "app_lecturer_group_discipline_discipline_id_22f599f7" ON "app_lecturer_group_discipline" ("discipline_id");
CREATE INDEX "app_lecturer_group_discipline_group_id_ba4dea73" ON "app_lecturer_group_discipline" ("group_id");
CREATE INDEX "app_lecturer_group_discipline_lecturer_id_12be19c0" ON "app_lecturer_group_discipline" ("lecturer_id");
COMMIT;
