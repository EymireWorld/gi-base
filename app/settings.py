from dotenv import dotenv_values


env = dotenv_values()


DB_HOST: str = env.get('DB_HOST')  # type: ignore
DB_NAME: str = env.get('DB_NAME')  # type: ignore
DB_USER: str = env.get('DB_USER')  # type: ignore
DB_PASSWORD: str = env.get('DB_PASSWORD')  # type: ignore

REDIS_HOST: str = env.get('REDIS_HOST')  # type: ignore
REDIS_PORT: int = int(env.get('REDIS_PORT'))  # type: ignore
