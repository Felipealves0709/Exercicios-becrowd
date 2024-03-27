SELECT m.id, m.name
FROM movies m
JOIN prices p ON m.id_PRICES = P.ID
WHERE p.value <2.00;