-- Tickets por prioridad
SELECT priority, COUNT(*) 
FROM fact_tickets
GROUP BY priority;

-- Tiempo promedio de resolución
SELECT AVG(resolved_at - created_at)
FROM fact_tickets;

-- Tickets por agente
SELECT agent, COUNT(*)
FROM fact_tickets
GROUP BY agent;