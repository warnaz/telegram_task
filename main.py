from src.core.loader import client
from src.handlers import register_client_handlers
from src.services import funnel


async def main() -> None:
    await client.start()
    register_client_handlers(client)
    await funnel.run()


if __name__ == "__main__":
    client.run(main())
