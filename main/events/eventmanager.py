import events.censor as censor
import events.linkremover as linkremover
import events.setrolejoin as setrolejoin
import events.welcomemessage as welcomemessage
import events.joinaudit as joinaudit
import events.leaveaudit as leaveaudit

# Events are ordered like "event_name": "file.py"

message_events = {
    "censoring": censor.on_message,
    "linkremoer": linkremover.on_message
}

join_events = {
    "setrolejoin": setrolejoin.on_join,
    "welcomemessage": welcomemessage.on_join,
    "joinaudit": joinaudit.on_join
}

leave_events = {
    "leaveaudit": leaveaudit.on_leave
}

async def runEvent(bot, guild, message, event_type):

    if event_type == "message":
        for event in message_events:
            await wrapper(message_events[event], bot, guild, message)

    if event_type == "join":
        for event in join_events:
            await wrapper(join_events[event], bot, guild, message)

    if event_type == "leave":
        for event in leave_events:
            await wrapper(leave_events[event], bot, guild, message)


async def wrapper(function, bot, guild, message):
    await function(bot, guild, message)
