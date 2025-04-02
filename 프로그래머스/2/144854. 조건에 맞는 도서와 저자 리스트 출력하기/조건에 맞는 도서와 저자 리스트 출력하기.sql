SELECT b.book_id, a.author_name, TO_CHAR(b.published_date, 'YYYY-MM-DD') as PUBLISHED_DATE
FROM author a
JOIN (
    SELECT *
    FROM book
    WHERE category = '경제'
) b
ON b.author_id = a.author_id
ORDER BY PUBLISHED_DATE