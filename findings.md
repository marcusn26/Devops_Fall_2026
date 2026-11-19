## Step 1 — Inspect the supplied broken configuration (10 minutes)

1. Which entry has an invalid data type? ANSWER: APP_PORT has an invalid data type. Rather than the current value of 'hello', it should instead hold a numerical value.
2. Which entry violates the deployment debug policy? ANSWER: The DEBUG entry of 'true' violates the deployment debug policy. This is because debugging in a production environment can expose private data.
3. Which required setting is empty? ANSWER: DB_PASSWORD
4. Which two names appear to represent the same concept, and which spelling does the contract require? ANSWER: Both dbhost and DB_HOST appear to represent the same concept -- the database host.  The DB_HOST spelling is the one that the contract requires.

