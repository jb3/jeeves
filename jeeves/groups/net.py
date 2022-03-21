from ansi.colour import fg, bg
from ansi.colour.fx import reset
from discord import app_commands, Interaction, Embed, Colour
from icmplib import ping
from tabulate import tabulate


class Network(app_commands.Group):
    """Commands for interacting with the network."""

    @app_commands.command()
    @app_commands.describe(target="The target to send pings to")
    async def ping(self, interaction: Interaction, target: str):
        """Run a ping to a given target."""
        await interaction.response.defer()

        host = ping(target, privileged=False)

        if not host.is_alive:
            em = Embed(
                title=f"Ping results to {target}",
                description="The selected host was not up",
                color=Colour.red(),
            )
        else:
            table = [
                ("Address", host.address),
                ("Min RTT", host.min_rtt),
                ("Avg RTT", host.avg_rtt),
                ("Max RTT", host.max_rtt),
                ("Packet loss", f"{host.packet_loss * 100}%"),
                ("Jitter", host.jitter),
            ]

            for i, item in enumerate(table):
                table[i] = (f"{fg.yellow}{item[0]}{reset}", f"{fg.red}{item[1]}{reset}")

            em = Embed(
                title=f"Ping results to {target}",
                description=f"```ansi\n{tabulate(table, tablefmt='psql')}\n```",
                color=Colour.green(),
            )

        await interaction.followup.send(embed=em)
