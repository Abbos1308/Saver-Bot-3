from aiogram import Router
from aiogram.filters import Command
from filters import AdminIdFilter
from . import states
from . import admin

admin_router = Router()
admin_router.message.register(admin.admin_command,Command("admin"),AdminIdFilter)
admin_router.callback_query.register(admin.admin_callbacks,AdminIdFilter,states.AdminState.base)
admin_router.message.register(admin.reklama,AdminIdFilter,states.AdminState.reklama)
