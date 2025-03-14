import asyncpg
import logging
from config import settings

logger = logging.getLogger(__name__)


async def create_db_pool() -> asyncpg.Pool:
    """Creates a PostgreSQL connection pool"""
    try:
        pool = await asyncpg.create_pool(
            dsn=(f"postgresql://{settings.db_user}:{settings.db_password.get_secret_value()}@"
                 f"{settings.db_host}:{settings.db_port}/{settings.db_name}"
                 ),
            min_size=settings.db_min_pool_size,
            max_size=settings.db_max_pool_size
        )
        logger.info("Database connection pool created successfully.")
        return pool
    except asyncpg.PostgresError as e:
        logger.error(f"Database connection pool creation failed: {e}", exc_info=True)
        raise


async def close_db_pool(pool: asyncpg.Pool):
    """Closes the connection pool (called when the application stops)."""
    if pool:
        await pool.close()
        logger.info("Database connection pool closed.")
