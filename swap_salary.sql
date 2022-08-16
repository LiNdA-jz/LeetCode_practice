-- UPDATE Salary
-- SET sex = (
--     CASE
--         WHEN sex = "m" THEN "f"
--         WHEN sex = "f" THEN "m"
--     END
-- );

-- "official" solution (faster)
UPDATE Salary
SET sex = (
    CASE
        WHEN sex = "m" THEN "f"
        ELSE "m"
    END
);

-- IF
UPDATE Salary
SET sex = IF (sex = "m", "f", "m");