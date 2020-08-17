import json
from datetime import datetime as dt

import aiohttp_session
from aiohttp.web import HTTPFound, Request, Response, RouteTableDef

from cogs import utils
from website import utils as webutils

"""
All pages on this website that implement the base.j2 file should return two things:
Firstly, the original request itself under the name 'request'.
Secondly, it should return the user info from the user as gotten from the login under 'user_info'
This is all handled by a decorator below, but I'm just putting it here as a note
"""


routes = RouteTableDef()


@routes.get("/r/{code}")
async def redirect(request:Request):
    """Handles redirects using codes stored in the db"""

    code = request.match_info['code']
    async with request.app['database']() as db:
        data = await db("SELECT location FROM redirects WHERE code=$1", code)
    if not data:
        return HTTPFound(location='/')
    return HTTPFound(location=data[0]['location'])


# --------------------------------------------
# Custom Role Settings
# --------------------------------------------


@routes.post('/set_master_role')
async def set_master_role(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    custom_role_master_role_id = post_data["custom_role_master_role_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_custom_role_position')
async def set_custom_role_position(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    custom_role_position_role_id = post_data["custom_role_position_role_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_custom_role_name_xfix')
async def set_custom_role_name_xfix(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    custom_role_name_xfix = post_data["custom_role_name_xfix"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


# --------------------------------------------
# Moderation Settings
# --------------------------------------------


@routes.post('/set_verify_role')
async def set_verify_role(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    verified_role_id = post_data["verified_role_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_mute_role')
async def set_mute_role(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    muted_role_id = post_data["muted_role_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_roles_to_be_removed')
async def set_roles_to_be_removed(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    removed_roles_ids = post_data.getall("removed_roles_ids")
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_moderator_role')
async def set_moderator_role(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    moderator_role_id = post_data["moderator_role_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_kick_archive_channel')
async def set_kick_archive_channel(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    kick_archive_channel_channel_id = post_data["kick_archive_channel_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_ban_archive_channel')
async def set_ban_archive_channel(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    ban_archive_channel_id = post_data["ban_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_mute_archive_channel')
async def set_mute_archive_channel(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    mute_archive_channel_id = post_data["mute_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_warn_archive_channel')
async def set_warn_archive_channel(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    warn_archive_channel_id = post_data["warn_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_edited_message_archive_channel')
async def set_edited_message_archive_channel(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    edited_message_archive_channel_id = post_data["edited_message_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_delete_message_archive_channel')
async def set_delete_message_archive_channel(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    delete_message_archive_channel_id = post_data["delete_message_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_vc_update_archive_channel')
async def set_vc_update_archive_channel(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    vc_update_archive_channel_id = post_data["vc_update_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


# --------------------------------------------
# Fursona settings
# --------------------------------------------


@routes.post('/set_allow_nsfw')
async def set_allow_nsfw(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    allow_nsfw_fursonas = post_data["allow_nsfw_fursonas"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_fursona_modmail')
async def set_fursona_modmail(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    fursona_modmail_channel_id = post_data["fursona_modmail_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_fursona_decline_archive')
async def set_fursona_decline_archive(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    fursona_decline_archive_channel_id = post_data["fursona_decline_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_fursona_accept_archive')
async def set_fursona_accept_archive(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    fursona_accept_archive_channel_id = post_data["fursona_accept_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/set_nsfw_fursona_archive')
async def set_nsfw_fursona_archive(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    fursona_accept_nsfw_archive_channel_id = post_data["fursona_accept_nsfw_archive_channel_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


# --------------------------------------------
# Interaction cooldowns
# --------------------------------------------


@routes.post('/delete_role_interaction_cooldown')
async def delete_role_interaction_cooldown(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    remove_role_interation_role_id = post_data["remove_role_interation_role_id"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


@routes.post('/add_role_interaction_cooldown')
async def add_role_interaction_cooldown(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    add_role_interation_role_id = post_data["add_role_interation_role_id"]
    cooldown_length = post_data["cooldown_length"]
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


# --------------------------------------------
# Shop settings
# --------------------------------------------


@routes.post('/template')
async def template(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    info = post_data
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


# --------------------------------------------
# Command disabling
# --------------------------------------------


@routes.post('/template')
async def template(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    info = post_data
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")


# --------------------------------------------
# Misc settings
# --------------------------------------------


@routes.post('/template')
async def template(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    logged_in_user = session.get('user_id')
    if not logged_in_user:
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    owner_list = request.app['config']['owners']
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0 or logged_in_user in owner_list) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    info = post_data
    
    referer = request.headers["Referer"]
    return HTTPFound(location=f"{referer[23:]}")




@routes.post('/set_prefix')
async def set_prefix(request: Request):
    """Sets the prefix for a given guild"""

    # See if they're logged in
    session = await aiohttp_session.get_session(request)
    post_data = await request.post()
    if not session.get('user_id'):
        return HTTPFound(location='/')
    guild_id = post_data['guild_id']
    if not guild_id:
        return HTTPFound(location='/')

    # Get the guilds they're valid to alter
    all_guilds = await webutils.get_user_guilds(request)
    if all_guilds is None:
        return HTTPFound(location='/discord_oauth_login')
    guild = [i for i in all_guilds if (i['owner'] or i['permissions'] & 40 > 0) and guild_id == i['id']]
    if not guild:
        return HTTPFound(location='/')

    # Grab the prefix they gave
    prefix = post_data['prefix'][0:30]
    if len(prefix) == 0:
        prefix = request.app['config']['prefix']['default_prefix']

    # Update prefix in DB
    async with request.app['database']() as db:
        key = 'prefix'
        await db(f'INSERT INTO guild_settings (guild_id, {key}) VALUES ($1, $2) ON CONFLICT (guild_id) DO UPDATE SET {key}=$2', int(guild_id), prefix)
    async with request.app['redis']() as re:
        redis_data = {'guild_id': int(guild_id)}
        redis_data['prefix'] = prefix
        await re.publish_json('UpdateGuildPrefix', redis_data)

    # Redirect to page
    location = f'/guild_settings?guild_id={guild_id}'
    return HTTPFound(location=location)


@routes.get('/login_redirect')
async def login_redirect(request:Request):
    """Page the discord login redirects the user to when successfully logged in with Discord"""

    await webutils.process_discord_login(request, ['identify', 'guilds'])
    session = await aiohttp_session.get_session(request)
    return HTTPFound(location=session.pop('redirect_on_login', '/'))