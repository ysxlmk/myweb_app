import asyncio
import orm
from models import User,Blog,Comment

async def test(loop):
    await orm.create_pool(loop,user='root',password='ysxaaa111',db='awesome')
    u =User(name='moy_yang',email='289859426@qq.com',passwd='aaa111',image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.run_forever()