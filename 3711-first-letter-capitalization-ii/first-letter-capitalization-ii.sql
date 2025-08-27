WITH RECURSIVE
  -- Step 1: Pre-process the text to handle hyphens consistently.
  -- We convert the text to lowercase and pad hyphens with spaces on both sides.
  -- This allows us to treat parts of a hyphenated word like regular words.
  -- e.g., 'the QUICK-brown fox' -> 'the quick - brown fox'
  PreprocessedText AS (
    SELECT
      content_id,
      content_text AS original_text,
      REPLACE(LOWER(content_text), '-', ' - ') AS processed_text
    FROM
      user_content
  ),

  -- Step 2: Recursively build the converted string, word by word.
  TextConverter AS (
    -- Anchor member: Sets up the initial state for the recursion.
    SELECT
      content_id,
      original_text,
      CAST('' AS CHAR(2000)) AS converted_text,
      -- Append a space to the end to ensure the last word is processed correctly.
      CONCAT(processed_text, ' ') AS remaining_text
    FROM
      PreprocessedText

    UNION ALL

    -- Recursive member: Processes one word in each iteration.
    SELECT
      content_id,
      original_text,
      -- Append the next word, properly capitalized, to the result.
      -- The expression below finds the next word, capitalizes its first letter,
      -- and adds it to the string being built.
      TRIM(CONCAT(converted_text, ' ',
        CONCAT(
          UPPER(SUBSTRING(remaining_text, 1, 1)),
          SUBSTRING(remaining_text, 2, LOCATE(' ', remaining_text) - 2)
        )
      )) AS converted_text,
      -- Remove the processed word from the remaining text to continue the loop.
      SUBSTRING(remaining_text, LOCATE(' ', remaining_text) + 1) AS remaining_text
    FROM
      TextConverter
    WHERE
      -- The recursion continues as long as there are words left to process.
      LENGTH(remaining_text) > 0
  )

-- Step 3: Select the final results and perform cleanup.
SELECT
  t.content_id,
  t.original_text,
  -- The recursion produces a row for each word processed. We need the final,
  -- longest version of the converted_text for each original content_id.
  -- Finally, we replace the padded hyphens (' - ') back to a single hyphen ('-').
  REPLACE(MAX(t.converted_text), ' - ', '-') AS converted_text
FROM
  TextConverter t
GROUP BY
  t.content_id,
  t.original_text
ORDER BY
  t.content_id;