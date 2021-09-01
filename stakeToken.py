from stake import CredentialsLoginRequest, StakeClient, SessionTokenLoginRequest
import asyncio
from currency_converter import CurrencyConverter

async def show_portfolio():
    async with StakeClient() as stake_session:
        myEquities = await stake_session.equities.list()
        c = CurrencyConverter()
        total = 0
        for equity in myEquities.equity_positions:
            market_val = c.convert(equity.market_value, 'USD', 'AUD')
            total += market_val
            print(equity.symbol + "     $" + str("{:.2f}".format(market_val)))
        print(equity)
        print("Total:   $" + str("{:.2f}".format(total)))
        return myEquities

if __name__ == "__main__":
    login_request = SessionTokenLoginRequest()
    asyncio.run(show_portfolio())
