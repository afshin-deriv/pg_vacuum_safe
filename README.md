# PG Vacuum Safe

## Overview
The health and performance of [PostgreSQL](https://github.com/postgres/postgres/tree/master) are very important prerequisites, particularly in critical production environments where database unavailability and slow response time have severe consequences. [VACUUM](https://github.com/postgres/postgres/blob/master/src/backend/commands/vacuum.c) command is one of the most crucial maintenance operations in PostgreSQL. This command frees space used by dead tuples in the table and resets statistics for the query planner.

However, using `VACUUM` in a production environment is quite a gamble. It increases disk usage and can result in a service outage; active tables get locked, which may degrade performance. From the guidelines and the experiences that we have gained during the real production, we have designed such a tool to perform `VACUUM` safely.

## Requirements
- **Python**: 3.1 or above
- **Python Packages**:
    - `psycopg2`
    - `psutil`
    - `requests`
- **OS**: Linux
- **PostgreSQL**: Versions 14 and up

## Examples
