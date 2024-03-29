SELECT *
FROM Patients
WHERE conditions LIKE "DIAB1%"
OR conditions LIKE "% DIAB1%";

-- regexp
select patient_id, patient_name, conditions from Patients
where conditions REGEXP "^DIAB1|[:space:]DIAB1"