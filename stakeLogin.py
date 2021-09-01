from stake import StakeClient, CredentialsLoginRequest
import asyncio

loginRequest = CredentialsLoginRequest(
    username="p.louka13@gmail.com",
    password=input("password:"),)

async def print_user():
    async with StakeClient(request=loginRequest) as stake_session:
        print(stake_session)

asyncio.run(print_user())
