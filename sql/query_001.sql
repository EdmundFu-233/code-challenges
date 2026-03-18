-- Query 001
SELECT 
    id,
    name,
    created_at
FROM users
WHERE status = 'active'
ORDER BY created_at DESC
LIMIT 100;
