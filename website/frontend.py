import aiohttp_session
import discord
from aiohttp.web import HTTPFound, Request, RouteTableDef, json_response
from aiohttp_jinja2 import template

import markdown2
from cogs import utils
from website import utils as webutils

import random

routes = RouteTableDef()


@routes.get("/")
@template('index.j2')
@webutils.add_output_args()
async def index(request: Request):
    """Index of the website, has "login with Discord" button
    If not logged in, all pages should redirect here"""

    return {}


@routes.get('/settings')
@template('settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def settings(request: Request):
    """Handles the main settings page for the bot"""

    return {}


@routes.get('/user_settings')
@template('user_settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def user_settings(request: Request):
    """Handles the users' individual settings pages"""

    # See if they're logged in
    # session = await aiohttp_session.get_session(request)
    
    return {}


@routes.get("/logout")
async def logout(request:Request):
    """Index of the website"""

    session = await aiohttp_session.get_session(request)
    session.invalidate()
    return HTTPFound(location='/')


@routes.get("/guilds")
@template('guild_picker.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def guild_picker(request: Request):
    """Shows the guilds that the user has permission to change"""

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    try:
        guilds = [i for i in all_guilds if i['owner'] or i['permissions'] & 40 > 0]
    except TypeError:
        # No guilds provided - did they remove the scope? who knows
        guilds = []

    return {'guilds': guilds}


@routes.get('/guild_settings')
@template('guild_settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def guild_settings(request: Request):
    """Shows the settings for a particular guild"""

    # See if they're logged in
    guild_id = request.query.get('guild_id')
    if not guild_id:
        return HTTPFound(location='/')

    # Get the bot object
    bot = request.app['bot']
    owner_list = request.app['config']['owners']
    session = await aiohttp_session.get_session(request)
    logged_in_user = session['user_id']

    # See if the bot is in the guild
    try:
        guild_object = await bot.fetch_guild(int(guild_id))
    except discord.Forbidden:
        # We get here? Bot's not in the server
        location = bot.get_invite_link(
            redirect_uri='https://marriagebot.xyz/guild_settings',
            response_type='code',
            scope='bot identify guilds guilds.join',
            read_messages=True,
            send_messages=True,
            attach_files=True,
            embed_links=True,
            guild_id=guild_id,
        )
        return HTTPFound(location=location)

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    oauth_guild_data = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not oauth_guild_data:
        return HTTPFound(location='/')

    return {"guild": guild_object}


@routes.get('/custom_role_settings')
@template('custom_role_settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def custom_role_settings(request: Request):

    bot = request.app['bot']
    guild = await bot.fetch_guild(request.query.get('guild_id'))
    guild_roles = await guild.fetch_roles()
    role_master = "blah"
    xfix = "blah"

    return {"guild": guild, "guild_roles": guild_roles, "role_master": role_master, "xfix": xfix}


@routes.get('/moderation_settings')
@template('moderation_settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def moderation_settings(request: Request):

    bot = request.app['bot']
    guild = await bot.fetch_guild(request.query.get('guild_id'))
    guild_roles = await guild.fetch_roles()
    guild_channels = await guild.fetch_channels()

    guild_roles_test = [[i, random.choice([True, False])] for i in guild_roles]

    # not_touched_roles = [item for item in guild_roles if item not in removed_roles]

    verfied_role = "Placeholder Text"
    muted_role = "Placeholder Text"
    moderator_role = "Placeholder Text"
    kick_archive_channel = "Placeholder Text"
    ban_archive_channel = "Placeholder Text"
    mute_archive_channel = "Placeholder Text"
    warns_archive_channel = "Placeholder Text"
    edited_message_archive_channel = "Placeholder Text"
    delete_message_archive_channel = "Placeholder Text"
    vc_update_archive_channel = "Placeholder Text"

    return {
        "guild": guild,
        "guild_roles": guild_roles,
        "muted_role": muted_role,
        "verfied_role": verfied_role,
        "guild_roles_test": guild_roles_test,
        "moderator_role": moderator_role,
        "guild_channels": guild_channels,
        "kick_archive_channel": kick_archive_channel,
        "ban_archive_channel": ban_archive_channel,
        "mute_archive_channel": mute_archive_channel,
        "warns_archive_channel": warns_archive_channel,
        "edited_message_archive_channel": edited_message_archive_channel,
        "delete_message_archive_channel": delete_message_archive_channel,
        "vc_update_archive_channel": vc_update_archive_channel,
    }


@routes.get('/fursona_settings')
@template('fursona_settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def fursona_settings(request: Request):

    bot = request.app['bot']
    guild = await bot.fetch_guild(request.query.get('guild_id'))
    guild_channels = await guild.fetch_channels()
    is_nsfw_allowed = "Placeholder Text"
    fursona_modmail_channel = "Placeholder Text"
    fursona_decline_archive_channel = "Placeholder Text"
    fursona_accept_archive_channel = "Placeholder Text"
    nsfw_fursona_archive_channel = "Placeholder Text"


    return {
        "guild": guild,
        "guild_channels": guild_channels,
        "is_nsfw_allowed": is_nsfw_allowed,
        "fursona_modmail_channel": fursona_modmail_channel,
        "fursona_decline_archive_channel": fursona_decline_archive_channel,
        "fursona_accept_archive_channel": fursona_accept_archive_channel,
        "nsfw_fursona_archive_channel": nsfw_fursona_archive_channel,
    }


@routes.get('/interaction_cooldowns')
@template('interaction_cooldowns.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def interaction_cooldowns(request: Request):

    guild_id = request.query.get('guild_id')
    app = request.app

    # No access to DATABASE

    # async with app['database']() as db:
    #     data_rows = await db("SELECT role_id, value FROM role_list WHERE guild_id=$1 and key='Interactions'", guild_id)

    # interaction_cooldowns = [{"role_id": row['role_id'], "role_name": guild.get_role(row['role_id']).name, "value": utils.TimeValue(int(row['value'])).clean_spaced} for row in data_rows]

    interaction_cooldowns = [{'role_id': 668341949127852042, 'role_name': 'Developer', 'value': '7m'},
                             {'role_id': 744513853055827978, 'role_name': 'new roleA', 'value': '9h'},
                             {'role_id': 744513868243664966, 'role_name': 'new roleS', 'value': '1s'},
                             {'role_id': 744513876942651473, 'role_name': 'new roleD', 'value': '5m'},
                             {'role_id': 744513898262298675, 'role_name': 'new roleE', 'value': '1m'}]

    guild = await app['bot'].fetch_guild(guild_id)
    guild_roles = await guild.fetch_roles()

    return {"guild": guild, "guild_roles": guild_roles, "interaction_cooldowns": interaction_cooldowns}


@routes.get('/shop_settings')
@template('shop_settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def shop_settings(request: Request):

    paintbrush_price = 0
    cooldown_token_price = 0
    
    return {}


@routes.get('/command_disabling')
@template('command_disabling.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def command_disabling(request:Request):

    return {}


@routes.get('/miscellaneous_settings')
@template('miscellaneous_settings.j2')
@webutils.add_output_args()
@webutils.requires_login()
async def miscellaneous_settings(request:Request):

    return {}


@routes.get("/discord_oauth_login")
async def login(request:Request):
    """Index of the website"""

    bot = request.app['bot']
    login_url = bot.get_invite_link(
        redirect_uri='http://203.51.8.92:8080/login_redirect',
        response_type='code',
        scope='identify guilds guilds.join',
        read_messages=True,
        send_messages=True,
        attach_files=True,
        embed_links=True,
    )
    return HTTPFound(location=login_url)
